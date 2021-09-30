from typing import List
import os
import config
from src.services.scan_data_reader import ScanDataReader


class MockScanDataReader(ScanDataReader): 

    def __init__(self):
        pass

    def read_scan_data(self, path: str) -> List[str]:
        
        # intruders
        if path == os.path.join(config.SCAN_FILE_PATH_INTRUDERS, '1.txt'):
            return self._mock_of_intruder_1()
        if path == os.path.join(config.SCAN_FILE_PATH_INTRUDERS, '2.txt'):
            return self._mock_of_intruder_2()
        
        # radars
        if path == os.path.join(config.SCAN_FILE_PATH_RADARS, '1.txt'):
            return self._mock_of_radar_1()
        if path == os.path.join(config.SCAN_FILE_PATH_RADARS, '2.txt'):
            return self._mock_of_radar_2()
        
        raise NotImplementedError
        
    def _mock_of_intruder_1(self) -> List[str]:
        output = []
        output.append("-ooo-")
        output.append("--o--")
        output.append("-o-o-")
        output.append("-oo--")
        return output

    def _mock_of_radar_1(self) -> List[str]:
        output = []
        output.append("-----o---o----")
        output.append("-------o------")
        output.append("----o----o----")
        output.append("----ooooo-----")
        output.append("----o---o-----")
        output.append("-oo------oo-o-")
        return output

    def _mock_of_intruder_2(self) -> List[str]:
        output = []
        output.append("--o--")
        output.append("-o-o-")
        output.append("-o-o-")
        output.append("--o--")
        return output

    def _mock_of_radar_2(self) -> List[str]:
        output = []
        output.append("--o-----------")
        output.append("-o-o----------")
        output.append("-o-o-----o----")
        output.append("--o-----o-o---")
        output.append("----o---o-o---")
        output.append("---o-o---o----")
        output.append("---o-o--------")
        return output
