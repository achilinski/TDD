from hour import Hour
from station.tests.time_table import TimeTable


class TimeTableStub(TimeTable):
    def __init__(self, departure_times):
        self.departure_times = (Hour('10:15'), Hour('12:120'), Hour('23:22'))
