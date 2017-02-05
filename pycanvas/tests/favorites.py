"""Favorites API Tests for Version 1.0.

This is a testing template for the generated FavoritesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.favorites import FavoritesAPI
from pycanvas.apis.favorites import Favorite


class TestFavoritesAPI(unittest.TestCase):
    """Tests for the FavoritesAPI."""

    def setUp(self):
        self.client = FavoritesAPI(secrets.instance_address, secrets.access_token)

    def test_list_favorite_courses(self):
        """Integration test for the FavoritesAPI.list_favorite_courses method."""

        r = self.client.list_favorite_courses()

    def test_add_course_to_favorites(self):
        """Integration test for the FavoritesAPI.add_course_to_favorites method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_remove_course_from_favorites(self):
        """Integration test for the FavoritesAPI.remove_course_from_favorites method."""
        id = None  # Change me!!

        r = self.client.remove_course_from_favorites(id)

    def test_reset_course_favorites(self):
        """Integration test for the FavoritesAPI.reset_course_favorites method."""

        r = self.client.reset_course_favorites()

