from rest_framework import serializers
from .models import Composition, CompositionDetail

class CompositionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompositionDetail
        fields = '__all__'

class CompositionSerializer(serializers.ModelSerializer):
    details = CompositionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Composition
        fields = '__all__'
