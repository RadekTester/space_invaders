# import pytest
import config
import os
from src.services.scan_data_reader import ScanDataReader
from tests.mockers.mock_text_file_reader import MockTextFileReader


mock_text_file_reader = MockTextFileReader()
scan_data_reader = ScanDataReader(mock_text_file_reader)

SCAN_DATA_PATH = 'scan_data'


def test_read_intruder_file_read():
    intruder_str_rows = scan_data_reader.read_scan_data(
        os.path.join(config.SCAN_FILE_PATH_INTRUDERS, '1.txt')
    )
    assert intruder_str_rows == [
        "-ooo-", 
        "--o--",
        "-o-o-",
        "-oo--"
    ]


def test_read_radar_file_read():
    radar_rows = scan_data_reader.read_scan_data(
        os.path.join(config.SCAN_FILE_PATH_RADARS, '1.txt')
    )
    assert radar_rows == [
        "-----o---o----",
        "-------o------",
        "----o----o----",
        "----ooooo-----",
        "----o---o-----",
        "-oo------oo-o-"
    ]


def test__clean_white_spaces():
    rows = []
    rows.append("  ---  ")
    rows.append("  ---\n")
    rows.append("  ---  \n")

    rows = scan_data_reader._clean_white_spaces(rows)
    assert rows == [
        "---",
        "---",
        "---"
    ]


def test__clean_cappital_letters():
    rows = []
    rows.append("-o-")
    rows.append("-O-")
    rows.append("-OO")

    rows = scan_data_reader._clean_cappital_letters(rows)
    assert rows == [
        "-o-",
        "-o-",
        "-oo"
    ]
