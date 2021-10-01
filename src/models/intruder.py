from src.services.scan_data_reader import ScanDataReader
from src.models.scan import Scan


class Intruder(Scan):

    def __init__(self, scan_data_reader: ScanDataReader):
        super().__init__(scan_data_reader)
