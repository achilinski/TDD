class TimeTable:
    def __init__(self, departure_time: tuple):
        departure_time = tuple(sorted(list(departure_time)))
        seconds_in_day = 24 * 60 * 60
        for i in departure_time:
            if i > seconds_in_day:
                raise ValueError('too big value')
        self.departure_times = departure_time
