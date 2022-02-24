from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Integrante, ObjectiveKeyResult


class IntegranteSerializer(serializers.ModelSerializer):
    """
    Serializer Class for Integrante Model, mapping each OKR.
    """
    okrs = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ObjectiveKeyResult.objects.all())

    class Meta:
        model = Integrante
        fields = ['id', 'nome']


class ObjectiveKeyResultSerializer(serializers.ModelSerializer):
    """
    Serializer Class for ObjectiveKeyResult Model.
    """
    class Meta:
        model = ObjectiveKeyResult
        fields = ['id', 'integrante', 'objetivo', 'resultado_1',
                  'resultado_2', 'resultado_3', 'resultado_4', 'resultado_5']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializing an User Model from Django default auth system.
    """
    okrs = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ObjectiveKeyResult.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'okrs']
