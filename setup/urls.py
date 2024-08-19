from django.contrib import admin
from django.urls import path, include, re_path
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, MatriculaEstudante, MatriculaCurso
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename = 'Cursos')
router.register('matriculas', MatriculaViewSet, basename = 'Matriculas')

schema_view = get_schema_view(
   openapi.Info(
      title="API Escola - Alura",
      default_version='v1',
      description="Projeto do curso 'Django REST Framework: construindo APIs RESTful do Zero' da Alura",
      terms_of_service="#",
      contact=openapi.Contact(email="vianayyasmin@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/',MatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/',MatriculaCurso.as_view()),
    
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
