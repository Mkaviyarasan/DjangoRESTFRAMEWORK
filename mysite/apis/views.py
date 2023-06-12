from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import GeeksSerializer
from .models import DataModel

# create a viewset
class ViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = DataModel.objects.all()
	
	# specify serializer to be used
	serializer_class = GeeksSerializer
