import datetime
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from OWSyncAPIApp.models import Artist, Country

from api_app.serializers import ArtistSerializer, CountrySerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows Users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# 
#     def get_queryset(self):
#         if not self.request.user.is_superuser:
#             return self.queryset.filter(pk=self.request.user.pk)
#         else:
#            return self.queryset

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Artists to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_queryset(self):
        # Get all articles
        queryset = Artist.objects.all()

        # Filter on date if present
        date = self.request.QUERY_PARAMS.get('date', None)
        if date is not None:
            try:
                queryset = queryset.filter(updated_at__gt=date)
            except:
                # Exception, return empty
                queryset = Artist.objects.none()

        return queryset
