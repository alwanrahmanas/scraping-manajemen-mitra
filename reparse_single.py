"""
Script untuk re-parse ijazah spesifik yang gagal
"""

import os
import sys
import json
import logging
from ijazah_parser import IjazahParser

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def reparse_single_ijazah(nik):
    """Re-parse ijazah untuk NIK tertentu"""
    
    # Cari file ijazah
    ijazah_path = f"downloads_test/{nik}/ijazah.jpg"
    
    if not os.path.exists(ijazah_path):
        logger.error(f"File tidak ditemukan: {ijazah_path}")
        return
    
    logger.info(f"Re-parsing ijazah untuk NIK: {nik}")
    logger.info(f"File: {ijazah_path}")
    
    # Initialize parser
    try:
        parser = IjazahParser()
    except ValueError as e:
        logger.error(f"Error: {e}")
        return
    
    # Parse
    result = parser.parse_ijazah(ijazah_path)
    
    # Print hasil
    print("\n" + "="*60)
    print(f"HASIL PARSING - NIK {nik}")
    print("="*60)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("="*60)
    
    # Analisis
    if result.get('gelar'):
        logger.info(f"✓ Gelar ditemukan: {result['gelar']}")
    else:
        logger.warning("⚠ Gelar tidak ditemukan")
    
    if result.get('nama_gelar'):
        logger.info(f"✓ Nama + Gelar: {result['nama_gelar']}")
    else:
        logger.warning("⚠ Nama + Gelar kosong")

if __name__ == "__main__":
    # NIK yang gagal
    nik = "7410036005020001"
    
    # Bisa juga dari command line
    if len(sys.argv) > 1:
        nik = sys.argv[1]
    
    reparse_single_ijazah(nik)
