from django.db import models
from django.contrib.auth.models import User


class Tipo_vehiculo(models.Model):
    nombre_tipo = models.CharField(max_length=50)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre_tipo


class Vehiculo(models.Model):
    tipo_vehiculo = models.ForeignKey(Tipo_vehiculo, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    identificacion = models.IntegerField()
    kms_recorridos_acumulados = models.FloatField()
    timepo_recorridos_acumulados = models.IntegerField()
    fecha_alta = models.DateField(auto_now=False, auto_now_add=False)
    fecha_baja = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "Vehiculo: " + str(self.identificacion)

    def toString(self):
        return "Vehiculo: " + str(self.identificacion)


class Recorrido(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
    ubicacion_inicio = models.CharField(max_length=50)
    ubicacion_fin = models.CharField(max_length=50)
    fuente_velocidad = models.CharField(max_length=50)
    velocidad_max = models.IntegerField()
    velocidad_media = models.IntegerField()
    velocidad_minima = models.IntegerField()
    kms_recorrido = models.FloatField()
    temperatura_media = models.IntegerField()
    presion_atm_media = models.FloatField()
    viento_predominante = models.CharField(max_length=50)
    nivel_lluvias_media = models.FloatField()
    estado_cota_media = models.FloatField()
    estado_trafico_media = models.CharField(max_length=50)
    calorias_quemadas = models.IntegerField()
    pulsaciones_media = models.IntegerField()
    co2_evitado = models.FloatField()

    def __str__(self):
        return "Recorrido: " + str(self.pk)


class Checkpoint(models.Model):
    recorrido = models.ForeignKey(Recorrido, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    ubicacion = models.CharField(max_length=50)
    km_parcial = models.FloatField()
    temperatura = models.IntegerField()
    visibilidad = models.CharField(max_length=50)
    presion_atm = models.FloatField()
    viento = models.FloatField()
    precipitaciones = models.IntegerField()
    radiacion_uv = models.IntegerField()
    nivel_cota = models.FloatField()
    estado_trafico = models.CharField(max_length=50)
    calorias_quemadas = models.IntegerField()
    pulsaciones = models.IntegerField()
    estado_componentes = models.CharField(max_length=50)
    estado_vehiculo = models.CharField(max_length=50)

    def __str__(self):
        return "Checkpoint: " + str(self.pk)


class Genero(models.Model):
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.valor


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    token_oauth = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    fecha_alta = models.DateTimeField()
    fecha_baja = models.DateTimeField()
    foto_jpg = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    altura = models.FloatField()
    frecuencia_cardiaca = models.IntegerField()
    rango_cadencia = models.IntegerField()


class Tipo_dispositivo(models.Model):
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.valor


class Sesion(models.Model):
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    ingreso = models.BooleanField()
    tipo_dispositivo = models.ForeignKey(
        Tipo_dispositivo, on_delete=models.CASCADE)
    dispositivo = models.CharField(max_length=50)

    def __str__(self):
        return "Sesion:" + str(self.pk)


class Tipo_componente(models.Model):
    nombre_tipo = models.CharField(max_length=50)
    activo = models.BooleanField()
    clasificacion_componentes = models.ManyToManyField(
        "Clasificacion_componente", through="Clasificacion_grupo_componente")

    def __str__(self):
        return self.nombre_tipo


class Tipo_dato(models.Model):
    valor = models.CharField(max_length=50)

    def __str__(self):
        return self.valor


class Parametro_tipo(models.Model):
    tipo_componente = models.ForeignKey(
        Tipo_componente, on_delete=models.CASCADE)
    tipo_dato = models.ForeignKey(Tipo_dato, on_delete=models.CASCADE)
    nombre_parametro = models.CharField(max_length=50)
    activo = models.BooleanField()
    obligatorio = models.BooleanField()

    def __str__(self):
        return self.nombre_parametro


class Componente(models.Model):
    tipo_componente = models.ForeignKey(
        Tipo_componente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    s_n = models.CharField(max_length=50)
    fecha_alta = models.DateField(auto_now=False, auto_now_add=False)
    fecha_baja = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.tipo_componente) + " " + self.marca + " " + self.modelo + " " + self.s_n


class Componente_parametro(models.Model):
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    parametro_tipo = models.ForeignKey(
        Parametro_tipo, on_delete=models.CASCADE)
    tipo_componente = models.ForeignKey(
        Tipo_componente, on_delete=models.CASCADE, null=True)
    valor_inferior = models.CharField(max_length=50)
    valor_superior = models.CharField(max_length=50)
    mediana = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=50)

    def __str__(self):
        return str(self.componente) + " " + str(self.parametro_tipo)


class Clasificacion_componente(models.Model):
    nombre_clasificacion = models.CharField(max_length=50)
    activo = models.BooleanField()
    tipo_componentes = models.ManyToManyField(
        Tipo_componente, through="Clasificacion_grupo_componente")

    def __str__(self):
        return self.nombre_clasificacion


class Clasificacion_grupo_componente(models.Model):
    clasificacion_componente = models.ForeignKey(
        Clasificacion_componente, on_delete=models.CASCADE)
    tipo_componente = models.ForeignKey(
        Tipo_componente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.clasificacion_componente) + " " + str(self.tipo_componente)


class Vehiculo_componente(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    clasificacion_componente = models.ForeignKey(
        Clasificacion_componente, on_delete=models.CASCADE)
    parametro_tipo = models.ForeignKey(
        Parametro_tipo, on_delete=models.CASCADE)
    valor_inicial = models.CharField(max_length=50)
    valor_actual = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    activo = models.BooleanField()

    def __str__(self):
        return str(self.vehiculo) + " " + str(self.componente)


class Checkpoint_componente(models.Model):
    checkpoint = models.ForeignKey(Checkpoint, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente,  on_delete=models.CASCADE)
    parametro_tipo = models.ForeignKey(
        Parametro_tipo, on_delete=models.CASCADE)
    valor_chequeado = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return str(self.checkpoint) + " " + str(self.componente)
