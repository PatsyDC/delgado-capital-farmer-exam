from django.shortcuts import render
from .models import *
from .serializers import *
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



SERVICE_PRICES = {
    'Constitución de empresa': 1500,
    'Defensa laboral': 2000,
    'Consultoría tributaria': 800,
}

def generar_numero_cotizacion():
    count = Cotizacion.objects.count() + 1
    return f"COT-2025-{str(count).zfill(4)}"

class CotizacionAPIView(APIView):
    def post(self, request):
        cliente_serializer = CotizacionClienteSerializer(data=request.data)
        if cliente_serializer.is_valid():
            cliente = cliente_serializer.save()
            tipo = cliente.tipoServicio
            precio = SERVICE_PRICES.get(tipo, 0)
            cot_id = generar_numero_cotizacion()
            cotizacion = Cotizacion.objects.create(
                cotizacion_id=cot_id,
                cliente=cliente,
                precio=precio,
                fecha_creacion=timezone.now()
            )
            response_serializer = CotizacionSerializer(cotizacion)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        cotizaciones = Cotizacion.objects.all()
        serializer = CotizacionSerializer(cotizaciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def Index(request):
    return render(request, 'index.html')