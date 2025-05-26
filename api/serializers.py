from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CotizacionClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotizacionCliente
        fields = '__all__'

class CotizacionSerializer(serializers.ModelSerializer):
    cliente = CotizacionClienteSerializer()

    class Meta:
        model = Cotizacion
        fields = '__all__'