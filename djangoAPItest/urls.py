"""djangoAPItest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"sesion", views.SesionViewSet)
router.register(r"usuarios", views.UserViewSet)
router.register(r"grupos", views.GroupViewSet)
router.register(r"perfiles", views.PerfilViewSet)
router.register(r"genero", views.GeneroViewSet)
router.register(r"vehiculos", views.VehiculoViewSet)
router.register(r"componentes", views.ComponenteViewSet)
router.register(r"recorridos", views.RecorridoViewSet)
router.register(r"checkpoints", views.CheckpointViewSet)
router.register(r"tipo_dispositivo", views.TipoDispositivoViewSet)
router.register(r"componente_parametro", views.ComponenteParametroViewSet)
router.register(r"tipo_dato", views.TipoDatoViewSet)
router.register(r"tipo_componente", views.TipoComponenteViewSet)
router.register(r"parametro_tipo", views.ParametroTipoViewSet)
router.register(r"clasificacion_componente",
                views.ClasificacionComponenteViewSet)
router.register(r"clasificacion_grupo_componente",
                views.ClasificacionGrupoComponenteViewSet)
router.register(r"tipo_vehiculo", views.TipoVehiculoViewSet)
router.register(r"checkpoint_componente", views.CheckpointComponenteViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]
