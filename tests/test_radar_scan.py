import pytest
import config
import os
from src.models.radar_scan import RadarScan
from src.models.intruder import Intruder
from tests.mockers.mock_scan_data_reader import MockScanDataReader


mock_scan_data_reader = MockScanDataReader()

intruder_mock_file_path_1 = os.path.join(config.SCAN_FILE_PATH_INTRUDERS, '1.txt')
intruder_mock_file_path_2 = os.path.join(config.SCAN_FILE_PATH_INTRUDERS, '2.txt')
intruder_mock_file_path_3 = os.path.join(config.SCAN_FILE_PATH_INTRUDERS, '3.txt')
intruder_mock_file_path_4 = os.path.join(config.SCAN_FILE_PATH_INTRUDERS, '4.txt')
radar_mock_file_path = os.path.join(config.SCAN_FILE_PATH_RADARS, '2.txt')


radar_scan = RadarScan(mock_scan_data_reader)
radar_scan.read_scan_data(radar_mock_file_path)


@pytest.fixture
def intruder():
    intruder = Intruder(mock_scan_data_reader)
    intruder.read_scan_data(intruder_mock_file_path_2)
    return intruder


@pytest.fixture
def intruder1():
    intruder = Intruder(mock_scan_data_reader)
    intruder.read_scan_data(intruder_mock_file_path_1)
    return intruder


@pytest.fixture
def intruder2():
    intruder = Intruder(mock_scan_data_reader)
    intruder.read_scan_data(intruder_mock_file_path_2)
    return intruder


@pytest.fixture
def intruder3():
    intruder = Intruder(mock_scan_data_reader)
    intruder.read_scan_data(intruder_mock_file_path_3)
    return intruder


@pytest.fixture
def intruder4():
    intruder = Intruder(mock_scan_data_reader)
    intruder.read_scan_data(intruder_mock_file_path_4)
    return intruder


@pytest.mark.parametrize("coordinates", [
    [0, 0, 20],
    [-1, -1, 12], 
    [-2, -2, 6], 
    [0, -2, 10], 
    [-6, -6, 0], 
    [-10, -10, 0], 
    [2, 4, 15],
    [2, 5, 10],
    [9, 3, 20],
    [10, 3, 16],
    [10, 4, 12],
    [100, 100, 0],
])
def test__get_potential_intruders_pixels_count_visible_on_radar_at_location(intruder, coordinates):
    visible_pixles = radar_scan._get_potential_intruders_pixels_visible_on_radar_at_location(
        coordinates[0], coordinates[1], intruder
    )
    assert visible_pixles == coordinates[2]


@pytest.mark.parametrize("data", [
    [0, 0, True],
    [7, 2, True],
    [1, 0, False],
    [2, 4, True],
])
def test_get_intruder_detection_found(intruder, data):
    detection = radar_scan._get_intruder_detection_at_location(
        data[0], data[1], intruder
    )
    assert detection.is_intruder_found() is data[2]


@pytest.mark.parametrize("data", [
    [0, 0, 2],
    [7, 2, 2],
    [1, 0, 0],
    [2, 4, 2],
])
def test__get_intruders_at_location(data):
    intruderA = Intruder(mock_scan_data_reader)
    intruderA.read_scan_data(intruder_mock_file_path_2)
    intruderB = Intruder(mock_scan_data_reader)
    intruderB.read_scan_data(intruder_mock_file_path_2)
    intruders = [intruderA, intruderB]

    intruder_detections = radar_scan._get_intruders_at_location(data[0], data[1], intruders)
    assert len(intruder_detections) == data[2]


def test__get_scanning_boundaries(intruder2, intruder3):
    intruders = [intruder2, intruder3]  # 5x4 and 8x6      14x7

    start_x, end_x, start_y, end_y = radar_scan._get_scanning_boundaries(intruders)
    assert (start_x, end_x, start_y, end_y) == (-4, -3, 14 + 4, 7 + 3)

    intruders = [intruder2, intruder2]  # 5x4 and 5x4    14x7
    start_x, end_x, start_y, end_y = radar_scan._get_scanning_boundaries(intruders)
    assert (start_x, end_x, start_y, end_y) == (-3, -2, 14 + 3, 7 + 2)


def test_get_intruders(intruder1, intruder2, intruder3, intruder4):
    intruders = [intruder2, intruder3]

    intruders_detections = radar_scan.scan_for_intruders(intruders)
    assert len(intruders_detections) == 3

    intruders = [intruder2, intruder4]
    intruders_detections = radar_scan.scan_for_intruders(intruders)
    assert len(intruders_detections) == 4
