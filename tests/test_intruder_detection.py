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


@pytest.mark.parametrize("data", [
    [0, 0, 10, 10, 10, 
        "location: 0, 0 | intruders visibility: 100 %| matching pixels: 10| matching pixels %: 100%"],
    [10, 20, 100, 50, 50, 
        "location: 10, 20 | intruders visibility: 50 %| matching pixels: 50| matching pixels %: 100%"],
    [30, 20, 1000, 800, 600, 
        "location: 30, 20 | intruders visibility: 80 %| matching pixels: 600| matching pixels %: 75%"]
])
def test_str(data):
    intruder_detection = IntruderDetection()
    intruder_detection.loc_x = data[0]
    intruder_detection.loc_y = data[1]
    intruder_detection.total_intruder_pixels = data[2]
    intruder_detection.intruder_pixels_visible_on_scan = data[3]
    intruder_detection.matching_pixels_count = data[4]

    output_str = intruder_detection.__str__()
    assert output_str == data[5]
