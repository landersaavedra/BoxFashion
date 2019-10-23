# Generated by Django 2.2.6 on 2019-10-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_auto_20191021_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Socio')),
                ('email', models.CharField(max_length=150, verbose_name='Email')),
                ('contrasenia', models.CharField(max_length=10, verbose_name='Contraseña')),
                ('is_active', models.BooleanField(verbose_name='Activacion del Cliente')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
