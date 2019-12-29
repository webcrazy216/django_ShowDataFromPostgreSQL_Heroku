from ..models import Personaldatas
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response

class PostListView(generics.ListAPIView):
    queryset = Personaldatas.objects.all()
    serializer_class = serializers.PostSerializer