# Generated by Django 3.2.3 on 2021-11-12 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('ubicacion', models.CharField(max_length=50)),
                ('km_parcial', models.FloatField()),
                ('temperatura', models.IntegerField()),
                ('visibilidad', models.CharField(max_length=50)),
                ('presion_atm', models.FloatField()),
                ('viento', models.FloatField()),
                ('precipitaciones', models.IntegerField()),
                ('radiacion_uv', models.IntegerField()),
                ('nivel_cota', models.FloatField()),
                ('estado_trafico', models.CharField(max_length=50)),
                ('calorias_quemadas', models.IntegerField()),
                ('pulsaciones', models.IntegerField()),
                ('estado_componentes', models.CharField(max_length=50)),
                ('estado_vehiculo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion_componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_clasificacion', models.CharField(max_length=50)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion_grupo_componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion_componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clasificacion_componente')),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('s_n', models.CharField(max_length=50)),
                ('fecha_alta', models.DateField()),
                ('fecha_baja', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parametro_tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_parametro', models.CharField(max_length=50)),
                ('activo', models.BooleanField()),
                ('obligatorio', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_oauth', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_alta', models.DateTimeField()),
                ('fecha_baja', models.DateTimeField()),
                ('foto_jpg', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('altura', models.FloatField()),
                ('frecuencia_cardiaca', models.IntegerField()),
                ('rango_cadencia', models.IntegerField()),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.genero')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_dato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=50)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('identificacion', models.IntegerField()),
                ('kms_recorridos_acumulados', models.FloatField()),
                ('timepo_recorridos_acumulados', models.IntegerField()),
                ('fecha_alta', models.DateField()),
                ('fecha_baja', models.DateField()),
                ('tipo_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipo_vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo_componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_inicial', models.CharField(max_length=50)),
                ('valor_actual', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('activo', models.BooleanField()),
                ('clasificacion_componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clasificacion_componente')),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.componente')),
                ('parametro_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.parametro_tipo')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=50)),
                ('activo', models.BooleanField()),
                ('clasificacion_componentes', models.ManyToManyField(through='api.Clasificacion_grupo_componente', to='api.Clasificacion_componente')),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('ingreso', models.BooleanField()),
                ('dispositivo', models.CharField(max_length=50)),
                ('tipo_dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipo_dispositivo')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.perfil')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Recorrido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('ubicacion_inicio', models.CharField(max_length=50)),
                ('ubicacion_fin', models.CharField(max_length=50)),
                ('fuente_velocidad', models.CharField(max_length=50)),
                ('velocidad_max', models.IntegerField()),
                ('velocidad_media', models.IntegerField()),
                ('velocidad_minima', models.IntegerField()),
                ('kms_recorrido', models.FloatField()),
                ('temperatura_media', models.IntegerField()),
                ('presion_atm_media', models.FloatField()),
                ('viento_predominante', models.CharField(max_length=50)),
                ('nivel_lluvias_media', models.FloatField()),
                ('estado_cota_media', models.FloatField()),
                ('estado_trafico_media', models.CharField(max_length=50)),
                ('calorias_quemadas', models.IntegerField()),
                ('pulsaciones_media', models.IntegerField()),
                ('co2_evitado', models.FloatField()),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehiculo')),
            ],
        ),
        migrations.AddField(
            model_name='parametro_tipo',
            name='tipo_componente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipo_componente'),
        ),
        migrations.AddField(
            model_name='parametro_tipo',
            name='tipo_dato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipo_dato'),
        ),
        migrations.CreateModel(
            name='Componente_parametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_inferior', models.CharField(max_length=50)),
                ('valor_superior', models.CharField(max_length=50)),
                ('mediana', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=50)),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.componente')),
                ('parametro_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.parametro_tipo')),
            ],
        ),
        migrations.AddField(
            model_name='componente',
            name='tipo_componente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipo_componente'),
        ),
        migrations.AddField(
            model_name='clasificacion_grupo_componente',
            name='tipo_componente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipo_componente'),
        ),
        migrations.AddField(
            model_name='clasificacion_componente',
            name='tipo_componentes',
            field=models.ManyToManyField(through='api.Clasificacion_grupo_componente', to='api.Tipo_componente'),
        ),
        migrations.CreateModel(
            name='Checkpoint_componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_chequeado', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('checkpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.checkpoint')),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.componente')),
                ('parametro_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.parametro_tipo')),
            ],
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='recorrido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.recorrido'),
        ),
    ]
