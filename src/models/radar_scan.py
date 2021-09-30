from typing import List
from src.services.scan_data_reader import ScanDataReader
from src.models.intruder import Intruder
from src.models.intruder_detection import IntruderDetection
from src.models.scan import Scan


class RadarScan(Scan):

    _data_loaded = False
    _data_is_correct = None
    _valid_characters = ['-', 'o']
    scan_rows = []

    def __init__(self, scan_data_reader: ScanDataReader) -> None:
        super().__init__(scan_data_reader)

    def check_for_intruders_at_location(self, loc_x: int, loc_y: int, intruders: List[Intruder]) -> List[IntruderDetection]:
        intruder_detections = []
        for intruder in intruders: 
            detection = self._get_intruder_detection_at_location(loc_x, loc_y, intruder)
            if detection.is_intruder_found(): 
                intruder_detections.append(detection)

        return intruder_detections

    def _get_intruder_detection_at_location(
        self, intruder_loc_x: int, intruder_loc_y: int, intruder: Intruder
    ) -> IntruderDetection:
        detection = IntruderDetection()
        intruder_width, intruder_height = intruder.get_size()
        total_intruder_pixels = intruder_width * intruder_height
        intruder_pixels_visible_on_scan = self._get_intruder_detection_at_location(
            intruder_loc_x, intruder_loc_y, intruder
        )

        detection.total_intruder_pixels = total_intruder_pixels
        detection.intruder_pixels_visible_on_scan = intruder_pixels_visible_on_scan

        # check what are matching pixels
        matching_pixels_count = 0
        for x in range(intruder_width):
            for y in range(intruder_height):
                if intruder.check_if_coordinates_are_valid(intruder_loc_x + x, intruder_loc_y + y):
                    intruder_pixel = intruder.get_pixel_at_coordinates( 
                        intruder_loc_x + x, intruder_loc_y + y)
                else: 
                    intruder_pixel = ""
                
                if self.check_if_coordinates_are_valid(intruder_loc_x + x, intruder_loc_y + y):
                    radar_pixel = self.get_pixel_at_coordinates( 
                        intruder_loc_x + x, intruder_loc_y + y)
                else: 
                    radar_pixel = ""

                if radar_pixel != "" and radar_pixel == intruder_pixel: 
                    matching_pixels_count += 1

        detection.matching_pixels_count = matching_pixels_count

        return detection

    def _get_potential_intruders_pixels_visible_on_radar_at_location(
        self, intruder_loc_x: int, intruder_loc_y: int, intruder: Intruder
    ) -> int:

        radar_width, radar_height = self.get_size()
        intruder_width, intruder_height = intruder.get_size()

        visible_start_x = intruder_loc_x
        visible_start_y = intruder_loc_y
        visible_end_x = visible_start_x + intruder_width
        visible_end_y = visible_start_y + intruder_height

        if visible_start_x < 0: 
            visible_start_x = 0
        if visible_start_x > radar_width: 
            visible_start_x = radar_width
        
        if visible_start_y < 0: 
            visible_start_y = 0
        if visible_start_y > radar_height: 
            visible_start_y = radar_height

        # ensure that if intruder is far away from the scan, it will not count negative width and height
        if visible_end_x < visible_start_x: 
            visible_start_x, visible_end_x = 0, 0
        
        if visible_end_y < visible_start_y: 
            visible_start_y, visible_end_y = 0, 0

        visible_pixles = (visible_end_x - visible_start_x) * (visible_end_y - visible_start_y)

        return visible_pixles
