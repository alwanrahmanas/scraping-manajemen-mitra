"""
Improved Ijazah Parser dengan prompt yang lebih baik untuk ijazah Indonesia
"""

import os
import base64
import json
import logging
from typing import Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


class IjazahParser:
    """Parser dengan prompt yang ditingkatkan untuk ijazah Indonesia"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key tidak ditemukan")
        self.client = OpenAI(api_key=self.api_key)
        logger.info("IjazahParser initialized")
    
    def encode_image(self, image_path: str) -> str:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    
    def parse_ijazah(self, image_path: str) -> Dict[str, Optional[str]]:
        """Parse ijazah dengan prompt yang ditingkatkan"""
        
        if not os.path.exists(image_path):
            logger.error(f"File tidak ditemukan: {image_path}")
            return self._empty_result()
        
        try:
            logger.info(f"Parsing ijazah: {image_path}")
            image_base64 = self.encode_image(image_path)
            
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert at reading Indonesian diplomas and certificates. "
                            "You can read blurry or low-quality images. "
                            "Extract ALL visible information accurately."
                        )
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": (
                                    "Parse this Indonesian diploma/certificate. The image may be blurry.\n\n"
                                    
                                    "CRITICAL INSTRUCTIONS:\n"
                                    "1. Identify if this is a HIGH SCHOOL (SMA/SMK) or UNIVERSITY diploma\n"
                                    "2. University degrees: S.Sos., S.Kom, S.T., S.E., S.Pd., A.Md., A.Md.Stat, S.H., etc.\n"
                                    "3. High school has NO degree (just diploma)\n"
                                    "4. Degrees are usually in parentheses: 'Name (S.Sos.)' or 'Name (AMd.)'\n"
                                    "5. Even if blurry, extract the degree from parentheses or degree title\n\n"
                                    
                                    "Return JSON:\n"
                                    "{\n"
                                    "  \"jenis_ijazah\": \"Perguruan Tinggi\" or \"SMA/SMK\",\n"
                                    "  \"nama\": \"Full name WITHOUT degree\",\n"
                                    "  \"gelar\": \"Degree only (S.Sos., A.Md., etc.) or null if high school\",\n"
                                    "  \"nama_gelar\": \"FULL NAME, DEGREE\" or just \"FULL NAME\" if no degree,\n"
                                    "  \"nim\": \"Student ID or null\",\n"
                                    "  \"program_studi\": \"Study program or null\",\n"
                                    "  \"fakultas\": \"Faculty or null\",\n"
                                    "  \"universitas\": \"University/school name or null\",\n"
                                    "  \"tanggal_ijazah\": \"Date or null\"\n"
                                    "}\n\n"
                                    
                                    "EXAMPLES:\n"
                                    "University: {\"jenis_ijazah\": \"Perguruan Tinggi\", \"gelar\": \"S.Sos.\", ...}\n"
                                    "High School: {\"jenis_ijazah\": \"SMA/SMK\", \"gelar\": null, ...}\n\n"
                                    
                                    "Return ONLY JSON. No explanations."
                                )
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_base64}"
                                }
                            }
                        ]
                    }
                ],
            )
            
            content = response.choices[0].message.content
            logger.debug(f"OpenAI response: {content}")
            
            try:
                # Clean markdown
                if content.startswith("```"):
                    content = content.split("```")[1]
                    if content.startswith("json"):
                        content = content[4:]
                
                result = json.loads(content.strip())
                
                # FALLBACK 1: Auto-detect jenis_ijazah jika kosong
                if not result.get("jenis_ijazah"):
                    if result.get("gelar"):
                        result["jenis_ijazah"] = "Perguruan Tinggi"
                    else:
                        result["jenis_ijazah"] = "SMA/SMK"
                    logger.info(f"✓ Auto-detected jenis_ijazah: {result['jenis_ijazah']}")
                
                # FALLBACK 2: Gabungkan nama + gelar jika nama_gelar kosong
                if not result.get("nama_gelar") and result.get("nama") and result.get("gelar"):
                    result["nama_gelar"] = f"{result['nama']}, {result['gelar']}"
                    logger.info(f"✓ Created nama_gelar: {result['nama_gelar']}")
                elif not result.get("nama_gelar") and result.get("nama"):
                    result["nama_gelar"] = result['nama']
                    logger.info(f"✓ Using nama as nama_gelar: {result['nama_gelar']}")
                
                logger.info(f"✓ Parsed: {result.get('jenis_ijazah', 'N/A')} - {result.get('nama', 'N/A')} - {result.get('gelar', 'N/A')}")
                logger.debug(f"Full result: {result}")
                return result
                
            except json.JSONDecodeError as e:
                logger.error(f"JSON parse error: {e}")
                logger.error(f"Content: {content}")
                return self._empty_result()
                
        except Exception as e:
            logger.error(f"Error parsing: {e}", exc_info=True)
            return self._empty_result()
    
    def _empty_result(self) -> Dict[str, Optional[str]]:
        return {
            "jenis_ijazah": None,
            "nama": None,
            "gelar": None,
            "nama_gelar": None,
            "nim": None,
            "program_studi": None,
            "fakultas": None,
            "universitas": None,
            "tanggal_ijazah": None
        }


# Test dengan contoh ijazah
if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
    
    parser = IjazahParser()
    
    # Test dengan ijazah yang ada
    test_files = [
        "downloads_test/7410011110800001/ijazah.jpg",
        "downloads_test/7410030107670045/ijazah.jpg",
        # Tambahkan path ijazah lain
    ]
    
    for file_path in test_files:
        if os.path.exists(file_path):
            print(f"\n{'='*60}")
            print(f"Testing: {file_path}")
            print('='*60)
            result = parser.parse_ijazah(file_path)
            print(json.dumps(result, indent=2, ensure_ascii=False))
