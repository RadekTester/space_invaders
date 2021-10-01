import config


class IntruderDetection():
    
    total_intruder_pixels = 0
    intruder_pixels_visible_on_scan = 0
    matching_pixels_count = 0
    adjusted_min_matching_pixcels_factor = 0
    loc_x = None
    loc_y = None
    intruder = None

    NOT_ENOUGH_PIXELS_VISIBLE_FACTOR = 0.5
    MIN_MATCHING_PIXELS_FACTOR = config.MIN_MATCHING_PIXELS_PERCENTAGE

    def is_intruder_found(self) -> bool:

        if not self._intruder_has_enought_data_visible_in_scan():
            return False

        if self._enough_match_pixels_found():
            return True
        
        return False

    def _intruder_has_enought_data_visible_in_scan(self) -> bool:
        if self.total_intruder_pixels == 0: 
            return False
        else: 
            if float(self.intruder_pixels_visible_on_scan) / float(self.total_intruder_pixels) \
                    >= self.NOT_ENOUGH_PIXELS_VISIBLE_FACTOR: 
                return True

        return False

    def _enough_match_pixels_found(self) -> bool:
        if self.intruder_pixels_visible_on_scan == 0: 
            return False

        invisible_part_adjustment_factor = self._get_invisible_part_adjustment_factor()
        self.adjusted_min_matching_pixcels_factor = self.MIN_MATCHING_PIXELS_FACTOR + invisible_part_adjustment_factor

        if float(self.matching_pixels_count) / float(self.intruder_pixels_visible_on_scan) \
                < self.adjusted_min_matching_pixcels_factor:
            return False
        else: 
            return True

    def _get_invisible_part_adjustment_factor(self) -> float: 

        if self.total_intruder_pixels == 0: 
            return 0.0
        if self.intruder_pixels_visible_on_scan == 0: 
            return 0.0

        visible_intruder_factor = 1 - float(self.intruder_pixels_visible_on_scan) / float(self.total_intruder_pixels)
        if visible_intruder_factor > 0.5: 
            return 0.0

        max_gap = 1 - self.MIN_MATCHING_PIXELS_FACTOR

        return 2 * max_gap * visible_intruder_factor

    def __str__(self) -> str: 
        visibility_percentage = self.intruder_pixels_visible_on_scan / self.total_intruder_pixels
        matching_pixels_percentage = self.matching_pixels_count / self.intruder_pixels_visible_on_scan 
        
        output_str = f"location: {self.loc_x}, {self.loc_y} "
        output_str += f"| intruders visibility: {round(visibility_percentage * 100)} %"
        output_str += f"| matching pixels: {self.matching_pixels_count}"
        output_str += f"| matching pixels %: {round(matching_pixels_percentage * 100)}%"

        return output_str
