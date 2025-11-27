from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework import viewsets
from . import serializers

# Create your views here.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = serializers.Autor.objects.all()
    serializer_class = serializers.AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = serializers.Libro.objects.all()
    serializer_class = serializers.LibroSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = serializers.Resena.objects.all()
    serializer_class = serializers.ResenaSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        calificacion_min = self.request.query_params.get('calificacion_minima')

        if calificacion_min:
            queryset = queryset.filter(calificacion__gte=calificacion_min)
        return queryset
    
    @action(detail=False, methods=['get'])
    def promedio(self, request):
        libro_id = request.query_params.get('libro_id')

        if libro_id:
            promedio = serializers.Resena.objects.filter(libro__id=libro_id).aggregate(Avg('calificacion'))
            return Response({
                "libro_id": libro_id,
                "rating_promedio": promedio
            })
        
    def perform_create(self, serializer):
        serializer.save()