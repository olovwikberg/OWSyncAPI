from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from OWSyncAPIApp.models import UserProfile, Artist, Country

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	verbose_name_plural = 'UserProfiles'
	can_delete = False

class InlineUserAdmin(UserAdmin):
	inlines = (UserProfileInline, )

class ArtistAdmin(admin.ModelAdmin):
    model = Artist
#	list_display = ('__unicode__', 'name')

class CountryAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'country_code')

admin.site.unregister(User)
admin.site.register(User, InlineUserAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Artist, ArtistAdmin)
