from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from handbook.models import Cat, CatPhoto
from pdb import set_trace as br

class CatResource ( ModelResource ):

	class Meta:
		queryset = Cat.objects.all ( )
		fields = [ 'id', 'avatar' ]
		resource_name = 'cat'

class CatFullResource ( ModelResource ):
	class Meta:
		list_allowed_methods = []
		detail_allowed_methods = [ 'get' ]
		queryset = Cat.objects.all ( )
		resource_name = 'cat_full'

class CatPhotoResource ( ModelResource ):
	cat = fields.ForeignKey ( CatResource, 'cat' )

	class Meta:
		queryset = CatPhoto.objects.all ( )
		resource_name = 'cat_photo'
		filtering = {
			"cat": ALL_WITH_RELATIONS
		}

	def dehydrate ( self, bundle ):
		obj = self.obj_get ( id = bundle.data['id'] )
		# br ( )
		bundle.data['480'] = obj.t480 ( )
		bundle.data['220'] = obj.t220 ( )
		return bundle