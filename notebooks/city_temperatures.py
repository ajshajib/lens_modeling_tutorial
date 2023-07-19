# -*- coding: utf-8 -*-
"""
This module defines a class that fectches daily temperature data for a given
city.
"""

__author__ = 'ajshajib'

from meteostat import Point
from meteostat import Daily
from geopy.geocoders import Nominatim


class CityTemperatures(object):
    """
    This class provides methods to fetch daily temperature data for a given
    city.
    """
    def __init__(self, city_name):
        """

        :param city_name: City name
        :type city_name: str
        """
        self.city_name = city_name

        self.city_latitude, self.city_longitude = self.get_coordinates(
                                                                    city_name)

        self.city_coordinate_point = Point(self.city_latitude,
                                           self.city_longitude,
                                           alt=70)

    @staticmethod
    def get_coordinates(city_name):
        """
        Get latitude and longitude of a city.
        :param city_name: City name
        :type city_name: str
        :return: latitude, longitude
        :rtype: tuple
        """
        geolocator = Nominatim(user_agent="myapplication")

        city_location = geolocator.geocode(city_name)

        if city_location is not None:
            return city_location.latitude, city_location.longitude
        else:
            raise ValueError("City not found! Choose a different city.")

    def get_temperatures(self, start_date, end_date):
        """
        Get daily temperature data for a given city.
        :param start_date: Start date
        :type start_date: datetime
        :param end_date: End date
        :type end_date: datetime
        :return: time, average temperature, difference between highest and
        lowest temperatures
        :rtype: tuple
        """
        data = Daily(self.city_coordinate_point, start_date, end_date)
        data = data.fetch()

        return data.index.values, data['tavg'], data['tmax'] - data['tmin']

