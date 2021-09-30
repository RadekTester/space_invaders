from typing import List


class TextFileReader():

    def __init__(self):
        pass

    def read_file_content(self, file_path: str) -> List[str]:
        with open(file_path, "r") as input_file:
            lines = input_file.readlines()

        return lines
