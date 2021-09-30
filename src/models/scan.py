from typing import Tuple
from src.exceptions.coordinates_out_of_bound import CoordinatesOutOfBandException
from src.services.scan_data_reader import ScanDataReader


class Scan():

    scan_rows = []

    def __init__(self, scan_data_reader: ScanDataReader) -> None:
        self.scan_data_reader = scan_data_reader

    def read_scan_data(self, file_path: str) -> None: 
        self.scan_rows = self.scan_data_reader.read_scan_data(file_path)

    def get_pixel_at_coordinates(self, x: int, y: int) -> str:
        if self.check_if_coordinates_are_valid(x, y):
            return self.scan_rows[y][x]
        else: 
            raise CoordinatesOutOfBandException

    def check_if_coordinates_are_valid(self, x: int, y: int) -> bool:
        if x < 0 or y < 0: 
            return False

        if y > len(self.scan_rows) - 1:
            return False

        if x > len(self.scan_rows[0]) - 1:
            return False

        return True

    def get_size(self) -> Tuple[int, int]:
        return (len(self.scan_rows[0]), len(self.scan_rows))
