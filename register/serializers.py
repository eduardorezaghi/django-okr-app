"""
Serializers for Models module.
"""
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
    integrante_nome = serializers.StringRelatedField(source='integrante.nome', read_only=True)
    class Meta:
        """
        Meta-information class for OKR Model Serializer
        """
        model = ObjectiveKeyResult
        fields = ['id', 'integrante', 'integrante_nome', 'objetivo', 'resultado_1',
        'resultado_2', 'resultado_3', 'resultado_4', 'resultado_5']
