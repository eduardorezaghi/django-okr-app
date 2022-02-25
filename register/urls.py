from django.urls import path, include
from register import views
from rest_framework.routers import DefaultRouter


app_name = 'register'
# Criando um roteador para realizar a configuração das URLS.
router = DefaultRouter()

# router.register(r'', views.index)
router.register(r'okr-api', views.OkrViewSet)
router.register(r'okr-integrantes', views.IntegranteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]