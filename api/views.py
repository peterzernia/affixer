from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.serializers import TransformationSerializer
from transformations.models import Transformation


class TransformationsListView(ListAPIView):
    '''
    '''
    queryset = Transformation.objects.all()
    serializer_class = TransformationSerializer
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('word',)
