#!/usr/bin/env python
#! -*- encoding:utf-8 -*-

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_save
import os
import re
from pdb import set_trace as bp
import Image

def get_crop_image_size ( size ):
	w, h = size
	refer_to_w = w / 10
	ratio_h = h / refer_to_w

	refer_to_h = h / 16

	if ( ratio_h > 16 ):
		h = w / 10 * 16
	else:
		w = refer_to_h * 10

	return ( w, h )

def cat_photo_path ( media_root, cat_id, cat_photo_id, filename, size = '' ):
	p = os.path.join ( media_root, "img", "photo", str ( cat_id % 1000 ), str ( cat_id ), str ( cat_photo_id ), size + "_" + filename )
	if not os.path.exists ( os.path.dirname ( p ) ):
		try:
			os.makedirs ( os.path.dirname ( p ) )
		except e:
			pass
	
	return p

def cat_photo_path_with_uplaod_to ( cat_photo, filename ):
	return cat_photo_path_no_photo_id ( cat_photo.cat.id, filename )

def cat_photo_path_no_photo_id ( cat_id, filename ):
	return os.path.join ( "img", "photo", str ( cat_id % 1000 ), str ( cat_id ), filename )

def cat_avatar_path_with_upload_to ( cat, filename ):
	return os.path.join ( "img", "avatar", filename )

class Cat ( models.Model ):
	name = models.CharField ( u"喵星人姓名", max_length = 255 )
	avatar = models.ImageField ( upload_to = cat_avatar_path_with_upload_to )
	summary = models.CharField ( u"简介", max_length = 255 )
	content = models.TextField ( u"介绍" );

	def __unicode__ ( self ):
		return self.name

class CatPhoto ( models.Model ):
	cat = models.ForeignKey ( Cat, )
	origin = models.ImageField ( upload_to = cat_photo_path_with_uplaod_to )

	def t480 ( self ):
		url = self.origin.url
		return os.path.join ( os.path.dirname ( url ), "%d_%s" % ( 480, os.path.basename ( url ) ) )

	def t220 ( self ):
		url = self.origin.url
		return os.path.join ( os.path.dirname ( url ), "%d_%s" % ( 220, os.path.basename ( url ) ) )

def cat_post_saved ( sender, **kwargs ):
	cat = kwargs.get ( "instance" )
	MEDIA_ROOT = settings.MEDIA_ROOT

	filename = os.path.basename ( str ( cat.avatar ) )
	ext = os.path.splitext ( filename )[1]
	avatar_dir = os.path.join ( "%d" % ( cat.id % 1000 ), "%d" % cat.id )
	new_filename = os.path.join ( avatar_dir, "%d%s" % ( cat.id, ext ) )

	filename_without_ext = os.path.splitext ( filename )[0]
	if re.compile ( "^\d+$" ).match ( filename_without_ext ):
		if int(filename_without_ext) == cat.id:
			return

	try:
		os.makedirs ( os.path.join ( MEDIA_ROOT, "img", "avatar", avatar_dir ) )
	except:
		pass


	abs_origin_path = os.path.join ( MEDIA_ROOT, "img", "avatar", filename )
	abs_new_path = os.path.join ( MEDIA_ROOT, "img", "avatar", new_filename  )

	if os.path.exists ( abs_origin_path ):
		if os.path.exists ( abs_new_path ):
			os.unlink ( abs_new_path )
		try:
			os.rename ( abs_origin_path, abs_new_path )
		except:
			bp ()
			pass
		cat.avatar = os.path.join ( "img", "avatar", new_filename ).replace ( os.sep, "/" )
		cat.save ( )

def cat_photo_saved ( sender, **kwargs ):
	cat_photo = kwargs.get ( "instance" )
	MEDIA_ROOT = settings.MEDIA_ROOT

	origin_filename = cat_photo.origin.__str__ ( )
	filename = os.path.basename ( origin_filename )
	ext = os.path.splitext ( filename )[1]
	photo_dir = os.path.join ( "%d" % ( cat_photo.cat.id % 1000 ), "%d" % cat_photo.cat.id )
	new_filename = os.path.join ( "%d%s" % ( cat_photo.id, ext ) )
	abs_photo_dir = os.path.join ( MEDIA_ROOT, "img", "photo", photo_dir )

	filename_without_ext = os.path.splitext ( filename )[0]
	if re.compile ( "^\d+$" ).match ( filename_without_ext ):
		if int(filename_without_ext) == cat_photo.id:
			return

	try:
		os.makedirs ( abs_photo_dir )
	except:
		pass

	abs_origin_path = os.path.join ( MEDIA_ROOT, origin_filename )
	abs_new_path = os.path.join ( abs_photo_dir, new_filename  )

	if os.path.exists ( abs_origin_path ):
		if os.path.exists ( abs_new_path ):
			os.unlink ( abs_new_path )

		try:
			os.rename ( abs_origin_path, abs_new_path )
		except:
			bp ()
			pass
	cat_photo.origin = os.path.join ( "img", "photo", photo_dir, new_filename ).replace ( os.sep, "/" )
	cat_photo.save ( )

	origin_bitmap = Image.open ( os.path.join ( abs_photo_dir, new_filename  ) )
	w, h = origin_bitmap.size

	# list_thumbnail = origin_bitmap.copy ( )
	if w > h:
		list_thumbnail = origin_bitmap.crop ( ( (w-h)/2, 0, h + (w-h)/2, h ) )
	else:
		list_thumbnail = origin_bitmap.crop ( ( 0, (h-w)/2, w, w ) )

	print list_thumbnail.size

	list_thumbnail.thumbnail ( ( 220, 220 ) )

	
	list_thumbnail.save ( os.path.join ( abs_photo_dir, "%d_%s" % ( 220, new_filename  ) ) )
	# w, h = get_crop_image_size ( ( w, h ) )
	# origin_bitmap = origin_bitmap.crop ( ( 0, 0, w, h ) )
	for THUMBNAIL in getattr ( settings, "THUMBNAILS", ( 480 ) ):
		thumbnail_bitmap = origin_bitmap.copy ( )
		thumbnail_bitmap.thumbnail ( ( THUMBNAIL, float ( THUMBNAIL ) / w * h )  )
		thumbnail_bitmap.save ( os.path.join ( abs_photo_dir, "%d_%s" % ( THUMBNAIL, new_filename  ) ) )


post_save.connect ( cat_photo_saved, sender = CatPhoto )
post_save.connect ( cat_post_saved,  sender = Cat )