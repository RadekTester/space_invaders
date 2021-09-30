from typing import List
import os
from src.services.text_file_reader import TextFileReader


class ScanDataReader(): 

    INTRUDERS_FILE_PATH = os.path.join('scan_data', 'intruder')
    RADAR_FILE_PATH = os.path.join('scan_data', 'radar')
    
    def __init__(self, text_file_reader: TextFileReader) -> None: 
        self.text_file_reader = text_file_reader

    def read_scan_data(self, file_path_name: str) -> List[str]:
        rows = self.text_file_reader.read_file_content(
            os.path.join(file_path_name)
        ) 
        rows = self._clean_cappital_letters(rows)
        rows = self._clean_white_spaces(rows)
        return rows

    def _clean_white_spaces(self, rows: List[str]) -> List[str]:
        return [row.strip() for row in rows]

    def _clean_cappital_letters(self, rows: List[str]) -> List[str]:
        return [row.lower() for row in rows]
