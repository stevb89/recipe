from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(verbose_name="Name des Rezepts", max_length=20, help_text="Name des Rezepts")
    created = models.DateTimeField(verbose_name="Erstellungsdatum", default=timezone.now, help_text="Das Rezeot wurde zu dieser Zeit erstellt.")
    
    EASY = "easy"
    INTERMEDIATE = "medium"
    HARD = "hard"
    
    DIFFICULTY_CHOICES = (
        (EASY, "Einfach"),
        (INTERMEDIATE, "Mittel"),
        (HARD, "Schwierig"),
    )
    difficulty = models.CharField(max_length=10, verbose_name="Schwierigkeitsgrad", choices=DIFFICULTY_CHOICES, help_text="Schwierigkeitsgrad des Rezepts")
    
    instructions = models.TextField(verbose_name="Anleitung", help_text="So wird es gemacht")
    hints = models.TextField(verbose_name="Hinweise", help_text="Das muss man beachten")


class Ingredient(models.Model):
    name = models.CharField(verbose_name="Name des Zutat", max_length=20, help_text="Name der Zutat")
    quantity = models.DecimalField(verbose_name="Menge", max_digits=6, decimal_places=2, blank=True, null=True, help_text='Mengenangabe')
    recipe = models.ForeignKey(Recipe, default=None, blank=True, null=True, on_delete=models.SET_NULL)

image = models.ImageField(upload_to='images',
verbose_name="Bild", blank=True, null=True,
help_text="illustrierendes Bild")