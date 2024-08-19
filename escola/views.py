from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, MatriculaEstudanteSerializer, MatriculaCursoSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class EstudanteViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
class MatriculaEstudante(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = MatriculaEstudanteSerializer
    
class MatriculaCurso(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = MatriculaCursoSerializer
    
    