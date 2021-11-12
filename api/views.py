from django.contrib.auth.models import Group, User
from rest_framework import viewsets

from .models import Checkpoint, Checkpoint_componente, Clasificacion_componente, Clasificacion_grupo_componente, Componente, Componente_parametro, Genero, Parametro_tipo, Perfil, Recorrido, Sesion, Tipo_componente, Tipo_dato, Tipo_dispositivo, Tipo_vehiculo, Vehiculo, Vehiculo_componente
from .serializers import (CheckpointComponenteSerializer, CheckpointSerializer, ClasificacionComponenteSerializer, ClasificacionGrupoComponenteSerializer, ComponenteParametroSerializer, ComponenteSerializer, GeneroSerializer, GroupSerializer, ParametroTipoSerializer,
                          PerfilSerializer, RecorridoSerializer,
                          SesionSerializer, TipoComponenteSerializer, TipoDatoSerializer, TipoDispositivoSerializer, TipoVehiculoSerializer, UserSerializer, VehiculoComponenteSerializer, VehiculoSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("date_joined")
    serializer_class = UserSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all().order_by("-usuario__date_joined")
    serializer_class = PerfilSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all().order_by("fecha_alta")
    serializer_class = VehiculoSerializer


class RecorridoViewSet(viewsets.ModelViewSet):
    queryset = Recorrido.objects.all().order_by("fecha_inicio")
    serializer_class = RecorridoSerializer


class CheckpointViewSet(viewsets.ModelViewSet):
    queryset = Checkpoint.objects.all().order_by("fecha")
    serializer_class = CheckpointSerializer


class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all().order_by("fecha")
    serializer_class = SesionSerializer


class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer


class TipoDispositivoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_dispositivo.objects.all()
    serializer_class = TipoDispositivoSerializer


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class ComponenteParametroViewSet(viewsets.ModelViewSet):
    queryset = Componente_parametro.objects.all()
    serializer_class = ComponenteParametroSerializer


class VehiculoComponenteViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo_componente.objects.all()
    serializer_class = VehiculoComponenteSerializer


class TipoDatoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_dato.objects.all()
    serializer_class = TipoDatoSerializer


class TipoComponenteViewSet(viewsets.ModelViewSet):
    queryset = Tipo_componente.objects.all()
    serializer_class = TipoComponenteSerializer


class ParametroTipoViewSet(viewsets.ModelViewSet):
    queryset = Parametro_tipo.objects.all()
    serializer_class = ParametroTipoSerializer


class ClasificacionComponenteViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion_componente.objects.all()
    serializer_class = ClasificacionComponenteSerializer


class ClasificacionGrupoComponenteViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion_grupo_componente.objects.all()
    serializer_class = ClasificacionGrupoComponenteSerializer


class TipoVehiculoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_vehiculo.objects.all()
    serializer_class = TipoVehiculoSerializer


class CheckpointComponenteViewSet(viewsets.ModelViewSet):
    queryset = Checkpoint_componente.objects.all()
    serializer_class = CheckpointComponenteSerializer
