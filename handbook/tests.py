"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import os
from django.test import TestCase
from handbook.models import CatPhoto, get_crop_image_size, cat_photo_saved, cat_photo_path
from django.conf import settings

THUMBNAILS = getattr ( settings, "THUMBNAILS", ( 320 ) )

class ImageSizeTest ( TestCase ):
	def test_10_16_equal ( self ):
		self.assertEqual ( ( 20, 32 ), get_crop_image_size ( ( 20, 32 ) ) )

	def test_10_16_x_less ( self ):
		self.assertEqual ( ( 20, 32 ), get_crop_image_size ( ( 38, 32 ) ) )

	def test_10_16_x_greater ( self ):
		self.assertEqual ( ( 10, 18 ), get_crop_image_size ( ( 20, 18 ) ) )

class AdminTest ( TestCase ):
	def test_cat_photo_path ( self ):
		cat = CatPhoto ( id = 1, origin = "img/photo/1/1/1.jpg" )
		self.assertEqual ( os.path.join ( "img", "photo", "1", "1", "1.jpg" ), cat_photo_path ( cat, "1.jpg" ) )

	def test_cat_photo_saved ( self ):
		cat = CatPhoto ( id = 1, origin = "img/photo/1/1/1.jpg" )
		cat_photo_saved ( None, instance = cat )
		self.assertEqual ( 1, 2 )


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
