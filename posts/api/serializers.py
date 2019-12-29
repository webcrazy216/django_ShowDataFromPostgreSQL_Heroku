from ..models import Personaldatas
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaldatas
        fields = ('imgurl', 'name', 'age', 'score', 'level', 'goals', 'achived', 'gender')
        
