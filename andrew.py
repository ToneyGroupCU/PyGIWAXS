"""Goals to write classes covering some 2D image processing and fitting for
GIWAXS data"""


class data(GIWAXS):
    def __init__(self, example):
        """
        Class that adds more processing functions for GIWAXS objects.
        """
        self.example = example
