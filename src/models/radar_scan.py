import math
from typing import List, Tuple
from src.services.scan_data_reader import ScanDataReader
from src.models.intruder import Intruder
from src.models.intruder_detection import IntruderDetection
from src.models.scan import Scan


class RadarScan(Scan):

    scan_rows = []

    def __init__(self, scan_data_reader: ScanDataReader) -> None:
        super().__init__(scan_data_reader)

    def scan_for_intruders(self, intruders: List[Intruder]) -> List[IntruderDetection]:
        scan_start_x, scan_start_y, scan_end_x, scan_end_y = self._get_scanning_boundaries(intruders)
        intruder_detections = []
        for x in range(scan_start_x, scan_end_x + 1):
            for y in range(scan_start_y, scan_end_y + 1):
                intruder_detections.extend(self._get_intruders_at_location(
                    x, y, intruders))
        return intruder_detections

    def _get_intruders_at_location(self, loc_x: int, loc_y: int, intruders: List[Intruder]) -> List[IntruderDetection]:
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
        detection.intruder = intruder
        intruder_width, intruder_height = intruder.get_size()
        total_intruder_pixels = intruder_width * intruder_height
        intruder_pixels_visible_on_scan = self._get_potential_intruders_pixels_visible_on_radar_at_location(
            intruder_loc_x, intruder_loc_y, intruder
        )

        detection.total_intruder_pixels = total_intruder_pixels
        detection.intruder_pixels_visible_on_scan = intruder_pixels_visible_on_scan

        # check what are matching pixels
        matching_pixels_count = 0
        for x in range(intruder_width):
            for y in range(intruder_height):
                if intruder.check_if_coordinates_are_valid(x, y):
                    intruder_pixel = intruder.get_pixel_at_coordinates(x, y)
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
        detection.loc_x = intruder_loc_x
        detection.loc_y = intruder_loc_y

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

        if visible_end_x > radar_width: 
            visible_end_x = radar_width
        if visible_end_x < 0: 
            visible_end_x = 0
        
        if visible_end_y > radar_height: 
            visible_end_y = radar_height
        if visible_end_y < 0: 
            visible_end_y = 0

        # ensure that if intruder is far away from the scan, it will not count negative width and height
        if visible_end_x < visible_start_x: 
            visible_start_x, visible_end_x = 0, 0
        
        if visible_end_y < visible_start_y: 
            visible_start_y, visible_end_y = 0, 0

        visible_pixles = (visible_end_x - visible_start_x) * (visible_end_y - visible_start_y)

        return visible_pixles

    def _get_scanning_boundaries(self, intruders: List[Intruder]) -> Tuple[int, int, int, int]:
        widest_intruder = self._get_widest_intruder(intruders)
        tallest_intruder = self._get_tallest_intruder(intruders)
        max_intruder_width = widest_intruder.get_width()
        max_intruder_height = tallest_intruder.get_height()
        
        scan_width, scan_height = self.get_size()

        mid_intruder_width = math.ceil(max_intruder_width / 2)
        mid_intruder_height = math.ceil(max_intruder_height / 2)
        return -1 * mid_intruder_width, -1 * mid_intruder_height, scan_width + mid_intruder_width, scan_height + mid_intruder_height

    def _get_widest_intruder(self, intruders: List[Intruder]):
        widest = None
        current_max_width = 0
        for intruder in intruders: 
            if widest is None: 
                widest = intruder
                current_max_width = widest.get_width()
                continue

            curr_width = intruder.get_width()
            if current_max_width < curr_width: 
                widest = intruder
                current_max_width = widest.get_width()
    
        return widest

    def _get_tallest_intruder(self, intruders: List[Intruder]):
        tallest = None
        current_max_height = 0
        for intruder in intruders: 
            if tallest is None: 
                tallest = intruder
                current_max_height = tallest.get_height()
                continue

            curr_height = intruder.get_height()
            if current_max_height < curr_height: 
                tallest = intruder
                current_max_height = tallest.get_height()
    
        return tallest
