import os
import sys
import logging
import requests
import pandas as pd
from datetime import datetime
from playwright.sync_api import sync_playwright
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# Setup logging
log_filename = f"scraper_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class MitraScraper:
    def __init__(self):
        self.base_download_dir = "downloads"
        self.data_list = []
        self.stats = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'ktp_downloaded': 0,
            'ijazah_downloaded': 0
        }
        
        # Create downloads directory
        if not os.path.exists(self.base_download_dir):
            os.makedirs(self.base_download_dir)
            logger.info(f"Created downloads directory: {self.base_download_dir}")

    def download_image(self, url, folder, filename):
        """Download image from URL with detailed logging"""
        if not url:
            logger.warning(f"No URL provided for {filename}")
            return None
        
        try:
            logger.info(f"Downloading {filename} from {url[:100]}...")
            response = requests.get(url, timeout=15)
            
            if response.status_code == 200:
                path = os.path.join(folder, filename)
                with open(path, 'wb') as f:
                    f.write(response.content)
                
                file_size = len(response.content) / 1024  # KB
                logger.info(f"✓ Downloaded {filename} ({file_size:.2f} KB) -> {path}")
                return path
            else:
                logger.error(f"✗ Failed to download {filename}: HTTP {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"✗ Error downloading {filename}: {str(e)}")
            return None

    def extract_bank_info(self, page):
        """Extract bank information from Rekening tab"""
        logger.info("Extracting bank information...")
        
        nama_bank = "N/A"
        no_rekening = "N/A"
        nama_pemilik = "N/A"

        try:
            # Get modal text for fallback parsing
            modal_text = page.locator(".v--modal-box").inner_text()
            
            # Try structured extraction first
            try:
                # Method 1: Look for text following labels
                bank_locator = page.locator('text="Nama Bank"').locator('xpath=following-sibling::*').first
                if bank_locator.count():
                    nama_bank = bank_locator.inner_text().strip()
                    logger.info(f"Found Nama Bank: {nama_bank}")
            except:
                pass
            
            try:
                rek_locator = page.locator('text="Nomor Rekening"').locator('xpath=following-sibling::*').first
                if rek_locator.count():
                    no_rekening = rek_locator.inner_text().strip()
                    logger.info(f"Found Nomor Rekening: {no_rekening}")
            except:
                pass
            
            try:
                owner_locator = page.locator('text="Nama Pemilik"').locator('xpath=following-sibling::*').first
                if owner_locator.count():
                    nama_pemilik = owner_locator.inner_text().strip()
                    logger.info(f"Found Nama Pemilik: {nama_pemilik}")
            except:
                pass
            
            # Fallback: Parse from text dump
            if nama_bank == "N/A" or no_rekening == "N/A":
                logger.info("Using fallback text parsing...")
                lines = modal_text.split('\n')
                for i, line in enumerate(lines):
                    line = line.strip()
                    
                    if "Nama Bank" in line and i + 1 < len(lines):
                        potential_bank = lines[i + 1].strip()
                        if potential_bank and "BANK" in potential_bank.upper():
                            nama_bank = potential_bank
                            logger.info(f"Fallback found Nama Bank: {nama_bank}")
                    
                    if "Nomor Rekening" in line and i + 1 < len(lines):
                        potential_rek = lines[i + 1].strip()
                        if potential_rek and potential_rek.replace(' ', '').isdigit():
                            no_rekening = potential_rek
                            logger.info(f"Fallback found Nomor Rekening: {no_rekening}")
                    
                    if "Nama Pemilik" in line and i + 1 < len(lines):
                        potential_owner = lines[i + 1].strip()
                        if potential_owner and len(potential_owner) > 2:
                            nama_pemilik = potential_owner
                            logger.info(f"Fallback found Nama Pemilik: {nama_pemilik}")
            
        except Exception as e:
            logger.error(f"Error extracting bank info: {str(e)}")
        
        return nama_bank, no_rekening, nama_pemilik

    def process_row(self, row, index, page):
        """Process a single table row"""
        try:
            # Find NIK link
            nik_link = row.locator('span[title="Lihat Detail Mitra"]')
            if not nik_link.count():
                logger.debug(f"Row {index}: No NIK link found, skipping")
                return False
            
            nik_text = nik_link.inner_text().strip()
            logger.info(f"\n{'='*60}")
            logger.info(f"Processing Row {index + 1}: NIK {nik_text}")
            logger.info(f"{'='*60}")
            
            # Create user directory
            user_download_dir = os.path.join(self.base_download_dir, nik_text)
            if not os.path.exists(user_download_dir):
                os.makedirs(user_download_dir)
                logger.info(f"Created directory: {user_download_dir}")
            
            # Click NIK to open popup
            logger.info("Opening detail popup...")
            nik_link.click()
            page.wait_for_selector("text=Detail Informasi Mitra", timeout=5000)
            logger.info("✓ Popup opened")
            
            # === Tab 1: File Administrasi ===
            logger.info("\n--- Processing File Administrasi ---")
            page.get_by_text("File Administrasi").click()
            page.wait_for_timeout(1000)
            
            ktp_path = None
            ijazah_path = None
            
            # Find images
            images = page.locator(".v--modal-box img").all()
            logger.info(f"Found {len(images)} images in modal")
            
            if len(images) >= 1:
                ktp_src = images[0].get_attribute("src")
                ktp_path = self.download_image(ktp_src, user_download_dir, "ktp.jpg")
                if ktp_path:
                    self.stats['ktp_downloaded'] += 1
            
            if len(images) >= 2:
                ijazah_src = images[1].get_attribute("src")
                ijazah_path = self.download_image(ijazah_src, user_download_dir, "ijazah.jpg")
                if ijazah_path:
                    self.stats['ijazah_downloaded'] += 1
            
            # === Tab 2: Rekening ===
            logger.info("\n--- Processing Rekening ---")
            page.get_by_text("Rekening").click()
            page.wait_for_timeout(500)
            
            nama_bank, no_rekening, nama_pemilik = self.extract_bank_info(page)
            
            # Store data
            row_data = {
                "NIK": nik_text,
                "Nama Bank": nama_bank,
                "Nomor Rekening": no_rekening,
                "Nama Pemilik": nama_pemilik,
                "Path KTP": ktp_path if ktp_path else "Not Downloaded",
                "Path Ijazah": ijazah_path if ijazah_path else "Not Downloaded",
                "Status": "Success"
            }
            self.data_list.append(row_data)
            
            logger.info(f"\n✓ Successfully processed NIK {nik_text}")
            logger.info(f"  Bank: {nama_bank}")
            logger.info(f"  Rekening: {no_rekening}")
            logger.info(f"  Pemilik: {nama_pemilik}")
            
            # Close modal
            page.keyboard.press("Escape")
            page.wait_for_timeout(500)
            
            self.stats['success'] += 1
            return True
            
        except Exception as e:
            logger.error(f"✗ Error processing row {index}: {str(e)}", exc_info=True)
            self.stats['failed'] += 1
            
            # Try to close modal and recover
            try:
                page.keyboard.press("Escape")
                page.wait_for_timeout(500)
            except:
                pass
            
            # Store failed entry
            self.data_list.append({
                "NIK": "Unknown",
                "Nama Bank": "N/A",
                "Nomor Rekening": "N/A",
                "Nama Pemilik": "N/A",
                "Path KTP": "Failed",
                "Path Ijazah": "Failed",
                "Status": f"Failed: {str(e)[:100]}"
            })
            
            return False

    def save_to_excel(self, filename="mitra_data.xlsx"):
        """Save data to Excel with formatting"""
        logger.info(f"\nSaving data to Excel: {filename}")
        
        df = pd.DataFrame(self.data_list)
        
        # Save to Excel
        df.to_excel(filename, index=False, sheet_name='Data Mitra')
        
        # Apply formatting
        wb = load_workbook(filename)
        ws = wb.active
        
        # Header formatting
        header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
        header_font = Font(bold=True, color="FFFFFF", size=12)
        
        for cell in ws[1]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center', vertical='center')
        
        # Auto-adjust column widths
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter
            
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            
            adjusted_width = min(max_length + 2, 50)
            ws.column_dimensions[column_letter].width = adjusted_width
        
        # Add borders
        thin_border = Border(
            left=Side(style='thin'),
            right=Side(style='thin'),
            top=Side(style='thin'),
            bottom=Side(style='thin')
        )
        
        for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
            for cell in row:
                cell.border = thin_border
        
        wb.save(filename)
        logger.info(f"✓ Excel file saved with formatting: {filename}")

    def print_summary(self):
        """Print scraping summary"""
        logger.info(f"\n{'='*60}")
        logger.info("SCRAPING SUMMARY")
        logger.info(f"{'='*60}")
        logger.info(f"Total rows processed: {self.stats['total']}")
        logger.info(f"✓ Successful: {self.stats['success']}")
        logger.info(f"✗ Failed: {self.stats['failed']}")
        logger.info(f"📷 KTP downloaded: {self.stats['ktp_downloaded']}")
        logger.info(f"📷 Ijazah downloaded: {self.stats['ijazah_downloaded']}")
        logger.info(f"{'='*60}")

    def run(self):
        """Main scraping process"""
        logger.info("="*60)
        logger.info("MITRA BPS SCRAPER - STARTING")
        logger.info("="*60)
        logger.info(f"Log file: {log_filename}")
        
        with sync_playwright() as p:
            try:
                # Connect to browser
                logger.info("\nConnecting to Chrome (port 9222)...")
                browser = p.chromium.connect_over_cdp("http://localhost:9222")
                context = browser.contexts[0]
                page = context.pages[0]
                
                logger.info(f"✓ Connected to: {page.title()}")
                logger.info(f"✓ URL: {page.url}")
                
                # Wait for table
                logger.info("\nWaiting for table to load...")
                page.wait_for_selector("table#vgt-table tbody tr", timeout=10000)
                
                rows = page.locator("table#vgt-table tbody tr").all()
                self.stats['total'] = len(rows)
                
                logger.info(f"✓ Found {len(rows)} rows in table")
                logger.info("\nStarting data extraction...\n")
                
                # Process each row
                for i, row in enumerate(rows):
                    self.process_row(row, i, page)
                
                logger.info("\n✓ All rows processed")
                
            except Exception as e:
                logger.error(f"✗ Fatal error: {str(e)}", exc_info=True)
                return
        
        # Save results
        if self.data_list:
            self.save_to_excel()
            
            # Also save CSV for compatibility
            df = pd.DataFrame(self.data_list)
            df.to_csv("mitra_data.csv", index=False)
            logger.info("✓ CSV backup saved: mitra_data.csv")
        
        # Print summary
        self.print_summary()
        logger.info(f"\n✓ Scraping completed! Check {log_filename} for details.")

if __name__ == "__main__":
    scraper = MitraScraper()
    scraper.run()
