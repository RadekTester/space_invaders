import pytest
import config
import os
from src.models.radar_scan import RadarScan
from src.models.intruder import Intruder
from tests.mockers.mock_scan_data_reader import MockScanDataReader


mock_scan_data_reader = MockScanDataReader()

intruder_mock_file_path = os.path.join(config.SCAN_FILE_PATH_INTRUDERS, '2.txt')
radar_mock_file_path = os.path.join(config.SCAN_FILE_PATH_RADARS, '2.txt')


radar_scan = RadarScan(mock_scan_data_reader)
radar_scan.read_scan_data(radar_mock_file_path)


@pytest.fixture
def intruder():
    intruder = Intruder(mock_scan_data_reader)
    intruder.read_scan_data(intruder_mock_file_path)
    return intruder


@pytest.mark.parametrize("coordinates", [
    [0, 0, 20],
    [-1, -1, 12], 
    [-2, -2, 6], 
    [0, -2, 10], 
    [-6, -6, 0], 
    [-10, -10, 0], 

])
def test__get_potential_intruders_pixels_visible_on_radar_at_location(intruder, coordinates):
    visible_pixles = radar_scan._get_potential_intruders_pixels_visible_on_radar_at_location(
        coordinates[0], coordinates[1], intruder
    )
    assert visible_pixles == coordinates[2]


# def test_get_intruder_detection_found(radar_scan, intruder):
#     detection = radar_scan._get_intruder_detection_at_location(
#         0, 0, intruder
#     )
#     assert detection.is_intruder_found() is True

#     detection = radar_scan._get_intruder_detection_at_location(
#         6, 2, intruder
#     )
#     assert detection.is_intruder_found() is True


# def test_get_intruder_detection_not_found(radar_scan: RadarScan, intruder: Intruder):
#     detection = radar_scan._get_intruder_detection_at_location(
#         2, 2, intruder
#     )
#     assert detection.is_intruder_found() is False



# @pytest.mark.parametrize("coordinates", [
#     [-1, -1, False],
#     [0, -1, False],
#     [-1, 0, False],
#     [0, 0, True],
#     [13, 0, True],
#     [14, 0, False],
#     [0, 5, True],
#     [0, 6, False],
#     [14, 7, False],
# ])
# def test_check_if_coordinates_are_valid(coordinates):
#     scan.read_radar_data(radar_mock_file_path)
#     assert scan.check_if_coordinates_are_valid(coordinates[0], coordinates[1]) == coordinates[2]


# @pytest.mark.parametrize("coordinates", [
#     [0, 0, "-"],
#     [5, 0, "o"],
#     [12, 5, "o"],
#     [13, 5, "-"],
# ])
# def test_get_pixel_at_coordinates(coordinates):
#     scan.read_radar_data(radar_mock_file_path)

#     assert scan.get_pixel_at_coordinates(coordinates[0], coordinates[1]) == coordinates[2]


# def test_get_pixel_at_coordinates_check_exception():
#     scan.read_radar_data(radar_mock_file_path)
#     with pytest.raises(CoordinatesOutOfBandException):
#         scan.get_pixel_at_coordinates(100, 100)


# def test_get_size():
#     scan.read_radar_data(radar_mock_file_path)
#     assert scan.get_size() == (14, 6)

#     scan.read_radar_data(intruder_mock_file_path)
#     assert scan.get_size() == (5, 4)
