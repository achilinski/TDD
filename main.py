from hour import Hour
from station.station import Station
from station.tests.time_table import TimeTable

directions = {
        'Gdańsk': TimeTable((Hour('11:15'), Hour('17:23'), Hour('23:10'))),
        'Reda': TimeTable((Hour('11:15'), Hour('17:23'), Hour('23:10')))
    }

station = Station('Rumia', directions)
