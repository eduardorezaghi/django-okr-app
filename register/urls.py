"""
App urls.py URLconf settings.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from register import views


APP_NAME = 'register'
# Criando um roteador para realizar a configuração das URLS.
router = DefaultRouter()


router.register(r'okr-list', views.OkrViewSet)
router.register(r'okr-integrantes', views.IntegranteViewSet)

urlpatterns = [
    path('okrs/', views.index),
    path('', include(router.urls)),
]
