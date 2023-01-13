from django.contrib import admin
from .models import Recipe, Ingredient


# Register your models here.
admin.site.register(Ingredient)

class IngredientInlineAdmin(admin.StackedInline):
    model = Ingredient
    show_change_link = True
    extra=0
    fields = (('name', 'quantity'),)
    
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'difficulty', 'instructions', 'hints')
    inlines = (IngredientInlineAdmin,)