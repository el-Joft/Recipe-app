# Generated by Django 2.2.5 on 2019-09-22 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='step',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe_app.Recipe'),
        ),
        migrations.AddField(
            model_name='step',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe_app.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipe_app.User'),
        ),
    ]
