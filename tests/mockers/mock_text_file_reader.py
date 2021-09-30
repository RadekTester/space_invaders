from typing import List
import os
import config
from src.services.text_file_reader import TextFileReader


class MockTextFileReader(TextFileReader): 

    def __init__(self):
        pass

    def read_file_content(self, path: str) -> List[str]:
        if path == os.path.join(config.SCAN_FILE_PATH_INTRUDERS, '1.txt'):
            return self._mock_of_intruder_1()

        if path == os.path.join(config.SCAN_FILE_PATH_RADARS, '1.txt'):
            return self._mock_of_radar_1()
        
        raise NotImplementedError
        
    def _mock_of_intruder_1(self) -> List[str]:
        output = []
        output.append("-ooo-")
        output.append("--o--")
        output.append("-O-O-")
        output.append("-oo--")
        return output

    def _mock_of_radar_1(self) -> List[str]:
        output = []
        output.append("-----o---O----")
        output.append("-------o------")
        output.append("----o----o----")
        output.append("----ooooo-----")
        output.append("----O---O-----")
        output.append("-oO------oo-o-")
        return output
