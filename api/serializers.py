from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import (Checkpoint, Checkpoint_componente,
                     Clasificacion_componente, Clasificacion_grupo_componente,
                     Componente, Componente_parametro, Genero, Parametro_tipo,
                     Perfil, Recorrido, Sesion, Tipo_componente, Tipo_dato,
                     Tipo_dispositivo, Tipo_vehiculo, Vehiculo,
                     Vehiculo_componente)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class VehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo
        fields = "__all__"


class RecorridoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recorrido
        fields = "__all__"


class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer

    class Meta:
        model = Perfil
        fields = "__all__"


class SesionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sesion
        fields = "__all__"


class CheckpointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Checkpoint
        fields = "__all__"


class ComponenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Componente
        fields = "__all__"


class TipoDispositivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_dispositivo
        fields = "__all__"


class GeneroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"


class ComponenteParametroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Componente_parametro
        fields = "__all__"


class VehiculoComponenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo_componente
        fields = "__all__"


class TipoDatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_dato
        fields = "__all__"


class TipoComponenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_componente
        fields = "__all__"


class ParametroTipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parametro_tipo
        fields = "__all__"


class ClasificacionComponenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clasificacion_componente
        fields = "__all__"


class ClasificacionGrupoComponenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clasificacion_grupo_componente
        fields = "__all__"


class TipoVehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_vehiculo
        fields = "__all__"


class CheckpointComponenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Checkpoint_componente
        fields = "__all__"
