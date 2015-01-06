from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class UserProfile(models.Model):
    GenderChoices = (('F', 'Kvinna'), ('M', 'Man'), ('U', 'Ospecificerat'))

    user = models.OneToOneField(User, primary_key=True)
    gender = models.CharField(max_length=1, choices=GenderChoices)
    date_of_birth = models.DateField(blank=True, null=True)

class Country(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    country_code = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'Updated at')
    is_valid = models.BooleanField(default=True, verbose_name=u'Is valid', help_text=u'If unchecked the object will be considered deleted')

    class Meta:
        verbose_name_plural = _('Countries')

    def __unicode__(self):
        return self.name


class Artist(models.Model):
    GenderChoices = (('F', 'Kvinna'), ('M', 'Man'), ('U', 'Ospecificerat'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'Updated at')
    is_valid = models.BooleanField(default=True, verbose_name=u'Is valid', help_text=u'If unchecked the object will be considered deleted')

    name = models.CharField(max_length=256, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GenderChoices)
    date_of_birth = models.DateField(blank=True, null=True)

    # relations
    user = models.OneToOneField(User, null=True, blank=True)
    origin = models.ForeignKey(Country, null=True, blank=True)
