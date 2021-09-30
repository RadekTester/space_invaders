import pytest
import config
import os
from src.models.scan import Scan
from tests.mockers.mock_scan_data_reader import MockScanDataReader
from src.exceptions.coordinates_out_of_bound import CoordinatesOutOfBandException


mock_scan_data_reader = MockScanDataReader()
scan = Scan(mock_scan_data_reader)
radar_mock_file_path = os.path.join(config.SCAN_FILE_PATH_RADARS, '1.txt')
intruder_mock_file_path = os.path.join(config.SCAN_FILE_PATH_INTRUDERS, '1.txt')


@pytest.mark.parametrize("coordinates", [
    [-1, -1, False],
    [0, -1, False],
    [-1, 0, False],
    [0, 0, True],
    [13, 0, True],
    [14, 0, False],
    [0, 5, True],
    [0, 6, False],
    [14, 7, False],
])
def test_check_if_coordinates_are_valid(coordinates):
    scan.read_scan_data(radar_mock_file_path)

    assert scan.check_if_coordinates_are_valid(coordinates[0], coordinates[1]) == coordinates[2]


@pytest.mark.parametrize("coordinates", [
    [0, 0, "-"],
    [5, 0, "o"],
    [12, 5, "o"],
    [13, 5, "-"],
])
def test_get_pixel_at_coordinates(coordinates):
    scan.read_scan_data(radar_mock_file_path)

    assert scan.get_pixel_at_coordinates(coordinates[0], coordinates[1]) == coordinates[2]


def test_get_pixel_at_coordinates_check_exception():
    scan.read_scan_data(radar_mock_file_path)
    with pytest.raises(CoordinatesOutOfBandException):
        scan.get_pixel_at_coordinates(100, 100)


def test_get_size():
    scan.read_scan_data(radar_mock_file_path)
    assert scan.get_size() == (14, 6)

    scan.read_scan_data(intruder_mock_file_path)
    assert scan.get_size() == (5, 4)
