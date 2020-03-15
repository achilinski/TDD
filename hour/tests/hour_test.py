import unittest

from hour import Hour
from hour.hour import HourError
from unittest_dataprovider import data_provider


class HourTest(unittest.TestCase):
    incorrect_hours = lambda: (
        ('11.05',), ('ef:gh',), ('24:11',), ('23:60',), ('1:30',),
        ('-1:11',), ('23:-8',), ('001:30',), ('11: 5',), ('  :11',),

    )

    @staticmethod
    def incorrect_values():
        return (
            ('11.05',),
            ('ef:gh',),
            ('24:11',),
            ('23:60',),
            ('1:30',),
            ('-1:11',),
            ('23:-8',),
            ('001:30',),
            ('11: 5',),

        )

    @data_provider(incorrect_values)
    def test_raiase_error(self, hour_value):
        """error with incorrect hour values"""
        with self.assertRaises(HourError):
            Hour(hour_value)

    def test_should_work_with_correct_data(self):
        """Podajemy prawdziwą godzinę i sprawdzamy, czy działa"""
        correct_hour = '23:15'
        hour = Hour(correct_hour)
        actual_hour = hour.get_hour()

        self.assertEqual(correct_hour, actual_hour)
