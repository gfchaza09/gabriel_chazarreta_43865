# Generated by Django 4.2.3 on 2023-08-09 02:48

from django.db import migrations, models
import tercera_preentrega_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('tercera_preentrega_app', '0002_perfil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='usuario',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='imagen_perfil',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='pagina_web',
        ),
        migrations.AddField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=tercera_preentrega_app.models.user_directory_path),
        ),
    ]
