# Generated by Django 3.1.2 on 2022-06-17 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_app', '0005_auto_20220617_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normscores',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='playerprofilescores',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
