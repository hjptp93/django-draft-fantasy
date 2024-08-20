# Generated by Django 3.2.13 on 2022-06-17 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_app', '0002_auto_20220604_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialConditions',
            fields=[
                ('id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('player', models.CharField(blank=True, max_length=250, null=True)),
                ('initial_condition', models.FloatField(blank=True, null=True)),
                ('club_position_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FirstWeekPred',
        ),
        migrations.DeleteModel(
            name='PlayerScores',
        ),
        migrations.DeleteModel(
            name='PredictedTable',
        ),
        migrations.RenameField(
            model_name='playerscoresminutes',
            old_name='name',
            new_name='player',
        ),
        migrations.RemoveField(
            model_name='playerscoresminutes',
            name='gameweek',
        ),
        migrations.AlterField(
            model_name='normscores',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='playerprofilescores',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='playerscoresminutes',
            name='id',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
    ]
