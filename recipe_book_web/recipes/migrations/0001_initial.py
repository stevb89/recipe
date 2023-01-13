# Generated by Django 4.1.5 on 2023-01-13 13:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name des Rezepts', max_length=20, verbose_name='Name des Rezepts')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text='Das Rezeot wurde zu dieser Zeit erstellt.', verbose_name='Erstellungsdatum')),
                ('difficulty', models.CharField(choices=[('easy', 'Einfach'), ('medium', 'Mittel'), ('hard', 'Schwierig')], help_text='Schwierigkeitsgrad des Rezepts', max_length=10, verbose_name='Schwierigkeitsgrad')),
                ('instructions', models.TextField(help_text='So wird es gemacht', verbose_name='Anleitung')),
                ('hints', models.TextField(help_text='Das muss man beachten', verbose_name='Hinweise')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name der Zutat', max_length=20, verbose_name='Name des Zutat')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, help_text='Mengenangabe', max_digits=6, null=True, verbose_name='Menge')),
                ('recipe', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.recipe')),
            ],
        ),
    ]
