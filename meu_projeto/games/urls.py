from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, UsuarioViewSet, JogoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'jogos', JogoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]