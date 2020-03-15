class HourError(RuntimeError):
    pass


class Hour:
    """ Pracuje z godziną w formacie HH:mm """

    def __init__(self, hour: str):
        self.hour = hour

        if not self.is_valid():
            raise HourError('Invalid format')

    def is_valid(self) -> bool:
        if self.hour[2] != ':':
            return False

        hour, minutes = self.hour.split(':')[0], self.hour.split(':')[1]
        if len(minutes) != 2:
            return False
        try:
            if int(hour) not in range(0, 24) or int(minutes) not in range(0, 60):
                return False
        except ValueError:
            return False

        if ' ' in self.hour:
            return False

        return True

    def get_hour(self) -> str:
        return self.hour

    def get_hour_in_seconds(self):
        hour, minutes = int(self.hour.split(':')[0]), int(self.hour.split(':')[1])
        return hour * 3600 + minutes * 60
