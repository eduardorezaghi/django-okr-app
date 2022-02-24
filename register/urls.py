from atexit import register
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import OkrViewSet

app_name = 'register'
# Criando um roteador para realizar a configuração das URLS.
router = DefaultRouter()

router.register(r'okr-api', OkrViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    # path('okr-api/', views.OkrViewSet.as_view())
]