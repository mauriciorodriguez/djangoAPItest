from django.shortcuts import render
from django.views.generic.base import TemplateView
from api.models import Checkpoint, Checkpoint_componente, Clasificacion_componente, Clasificacion_grupo_componente, Componente, Componente_parametro, Genero, Parametro_tipo, Perfil, Recorrido, Sesion, Tipo_componente, Tipo_dato, Tipo_dispositivo, Tipo_vehiculo, Vehiculo
from django.views.generic import ListView
from django.contrib.auth.models import Group, User


class IndexView(TemplateView):
    template_name = "index.html"


class SesionListView(ListView):
    model = Sesion
    template_name = "list_tables.html"


class UsuarioListView(ListView):
    model = User
    template_name = "list_tables.html"


class PerfilListView(ListView):
    model = Perfil
    template_name = "list_tables.html"


class GrupoListView(ListView):
    model = Group
    template_name = "list_tables.html"


class GeneroListView(ListView):
    model = Genero
    template_name = "list_tables.html"


class VehiculoListView(ListView):
    model = Vehiculo
    template_name = "list_tables.html"


class ComponenteListView(ListView):
    model = Componente
    template_name = "list_tables.html"


class RecorridoListView(ListView):
    model = Recorrido
    template_name = "list_tables.html"


class CheckpointListView(ListView):
    model = Checkpoint
    template_name = "list_tables.html"


class TipoDispositivoListView(ListView):
    model = Tipo_dispositivo
    template_name = "list_tables.html"


class ComponenteParametroListView(ListView):
    model = Componente_parametro
    template_name = "list_tables.html"


class TipoDatoListView(ListView):
    model = Tipo_dato
    template_name = "list_tables.html"


class TipoComponenteListView(ListView):
    model = Tipo_componente
    template_name = "list_tables.html"


class ParametroTipoListView(ListView):
    model = Parametro_tipo
    template_name = "list_tables.html"


class ClasificacionComponenteListView(ListView):
    model = Clasificacion_componente
    template_name = "list_tables.html"


class ClasificacionGrupoComponenteListView(ListView):
    model = Clasificacion_grupo_componente
    template_name = "list_tables.html"


class TipoVehiculoListView(ListView):
    model = Tipo_vehiculo
    template_name = "list_tables.html"


class CheckpointComponenteListView(ListView):
    model = Checkpoint_componente
    template_name = "list_tables.html"
