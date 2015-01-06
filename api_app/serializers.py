from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.fields import BooleanField

from OWSyncAPIApp.models import Artist, Country

'''
    Custom field based on rest_framework.fields.BooleanField to get NullBooleanField behaviour
    https://github.com/tomchristie/django-rest-framework/pull/1422#issuecomment-43181297
'''
# class NullBooleanField(BooleanField):
#     empty = True
# 
#     def __init__(self, *args, **kwargs):
#         kwargs['required'] = False
#         super(NullBooleanField, self).__init__(*args, **kwargs)
# 
#     def from_native(self, value):
#         if value in ('none', 'None', 'null', None):
#             return None
#         return super(NullBooleanField, self).from_native(value)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id',
            'is_valid',
            'created_at',
            'updated_at',
            'name',
            'country_code',
        )

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'id',
            'is_valid',
            'created_at',
            'updated_at',
            'name',
            'origin',
        )

# class UserSerializer(serializers.ModelSerializer):
#     ambitionprofile_set = AmbitionProfileSerializer(many=True)
# 
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#             'email',
#             'groups',
#             'ambitionprofile_set'
#        )
