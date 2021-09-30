import pytest
from src.models.intruder_detection import IntruderDetection


intruder_detection = IntruderDetection()


@pytest.mark.parametrize("data", [
    [100, 49, False],
    [100, 50, True],
    [0, 0, False],
    [100, 100, True],
    [100, 30, False],
])
def test__intruder_has_enought_data_visible_in_scan(data):
    intruder_detection.total_intruder_pixels = data[0]
    intruder_detection.intruder_pixels_visible_on_scan = data[1]
    assert intruder_detection._intruder_has_enought_data_visible_in_scan() == data[2]


@pytest.mark.parametrize("data", [
    [0, 0, 0, False],
    [0, 100, 85, True],
    [0, 100, 84, False],
    [0, 100, 86, True],
])
def test__enough_match_pixels_found(data):
    intruder_detection.total_intruder_pixels = data[0]
    intruder_detection.intruder_pixels_visible_on_scan = data[1]
    intruder_detection.matching_pixels_count = data[2]

    assert intruder_detection._enough_match_pixels_found() == data[3]


@pytest.mark.parametrize("data", [
    [100, 100, 0],
    [100, 0, 0],
    [100, 20, 0],
    [100, 49, 0],
    [100, 50, 0.15],
    [100, 80, 0.06],
    [100, 90, 0.03],
])
def test__get_invisible_part_adjustment_factor(data):
    intruder_detection.total_intruder_pixels = data[0]
    intruder_detection.intruder_pixels_visible_on_scan = data[1]
    assert (intruder_detection._get_invisible_part_adjustment_factor() - data[2]) < 0.000001


@pytest.mark.parametrize("data", [
    [0, 0, 0, False],
    [100, 100, 85, True],
    [100, 100, 100, True],
    [100, 100, 84, False],
    [100, 100, 0, False],
])
def test_is_intruder_found(data):
    intruder_detection.total_intruder_pixels = data[0]
    intruder_detection.intruder_pixels_visible_on_scan = data[1]
    intruder_detection.matching_pixels_count = data[2]

    assert intruder_detection.is_intruder_found() == data[3]
