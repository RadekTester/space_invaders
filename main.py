import os
from src.models.intruder import Intruder
from src.models.radar_scan import RadarScan
from src.services.scan_data_reader import ScanDataReader
from src.services.text_file_reader import TextFileReader


def main():
    text_file_reader = TextFileReader()
    scan_data_reader = ScanDataReader(text_file_reader)
    
    intruder_files_paths = []
    intruder_files_paths.append(os.path.join('scan_data', 'intruder', '1.txt'))
    intruder_files_paths.append(os.path.join('scan_data', 'intruder', '2.txt'))

    scan_file_path = os.path.join('scan_data', 'radar', '1.txt')

    radar_scan = RadarScan(scan_data_reader)
    radar_scan.read_scan_data(scan_file_path)

    intruders = []
    for file_path in intruder_files_paths: 
        new_intruder = Intruder(scan_data_reader)
        new_intruder.read_scan_data(file_path)
        intruders.append(new_intruder)

    intruders_detections = radar_scan.scan_for_intruders(intruders)
    for detection in intruders_detections: 
        print(detection)


if __name__ == "__main__":
    main()
