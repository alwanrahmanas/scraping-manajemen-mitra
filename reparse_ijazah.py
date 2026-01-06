"""
Script untuk re-parse ijazah yang sudah didownload
Berguna untuk testing parsing tanpa perlu download ulang
"""

import os
import sys
import logging
from ijazah_parser import IjazahParser

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def reparse_ijazah(folder="downloads"):
    """Re-parse semua ijazah yang sudah didownload"""
    
    logger.info("="*60)
    logger.info("RE-PARSING IJAZAH YANG SUDAH DIDOWNLOAD")
    logger.info("="*60)
    
    # Initialize parser
    try:
        parser = IjazahParser()
        logger.info("✓ IjazahParser initialized")
    except ValueError as e:
        logger.error(f"✗ {e}")
        logger.info("\nSetup .env file dengan OpenAI API key terlebih dahulu")
        return
    
    # Cari semua file ijazah
    ijazah_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower() in ["ijazah.jpg", "ijazah.jpeg", "ijazah.png"]:
                ijazah_files.append(os.path.join(root, file))
    
    if not ijazah_files:
        logger.warning(f"Tidak ada file ijazah ditemukan di folder {folder}")
        return
    
    logger.info(f"Ditemukan {len(ijazah_files)} file ijazah\n")
    
    # Parse semua
    success_count = 0
    failed_count = 0
    
    for i, ijazah_path in enumerate(ijazah_files, 1):
        nik = os.path.basename(os.path.dirname(ijazah_path))
        logger.info(f"\n[{i}/{len(ijazah_files)}] NIK: {nik}")
        logger.info(f"File: {ijazah_path}")
        
        try:
            result = parser.parse_ijazah(ijazah_path)
            
            # Print hasil
            logger.info("--- HASIL PARSING ---")
            logger.info(f"  Nama          : {result.get('nama', 'N/A')}")
            logger.info(f"  Gelar         : {result.get('gelar', 'N/A')}")
            logger.info(f"  Nama + Gelar  : {result.get('nama_gelar', 'N/A')}")
            logger.info(f"  NIM           : {result.get('nim', 'N/A')}")
            logger.info(f"  Program Studi : {result.get('program_studi', 'N/A')}")
            logger.info(f"  Fakultas      : {result.get('fakultas', 'N/A')}")
            logger.info(f"  Universitas   : {result.get('universitas', 'N/A')}")
            logger.info(f"  Tanggal       : {result.get('tanggal_ijazah', 'N/A')}")
            
            if result.get('nama_gelar'):
                success_count += 1
                logger.info("✓ Parsing berhasil")
            else:
                failed_count += 1
                logger.warning("⚠ nama_gelar kosong")
            
        except Exception as e:
            failed_count += 1
            logger.error(f"✗ Error: {e}")
    
    # Summary
    logger.info("\n" + "="*60)
    logger.info("SUMMARY")
    logger.info("="*60)
    logger.info(f"Total ijazah      : {len(ijazah_files)}")
    logger.info(f"✓ Berhasil parsed : {success_count}")
    logger.info(f"✗ Gagal/kosong    : {failed_count}")
    logger.info("="*60)

if __name__ == "__main__":
    # Bisa specify folder lain jika perlu
    folder = sys.argv[1] if len(sys.argv) > 1 else "downloads"
    reparse_ijazah(folder)
