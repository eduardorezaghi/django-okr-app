"""
Serializers for Models module.
"""
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Integrante, ObjectiveKeyResult


class IntegranteSerializer(serializers.ModelSerializer):
    """
    Serializer Class for Integrante Model, mapping each OKR.
    """
    okrs = serializers.StringRelatedField(many=True)

    class Meta:
        """
        Meta-information class for Integrante Model Serializer
        """
        model = Integrante
        fields = ['id', 'nome', 'okrs']


class ObjectiveKeyResultSerializer(serializers.ModelSerializer):
    """
    Serializer Class for ObjectiveKeyResult Model.
    """
    integrante = serializers.CharField(source='integrante.nome')
    class Meta:
        """
        Meta-information class for OKR Model Serializer
        """
        model = ObjectiveKeyResult
        fields = ['id', 'integrante', 'objetivo', 'resultado_1',
                  'resultado_2', 'resultado_3', 'resultado_4', 'resultado_5']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializing an User Model from Django default auth system.
    """
    class Meta:
        """
        Meta-information class for User Model Serializer
        """
        model = User
        fields = ['id', 'username', 'okrs']
