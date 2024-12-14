from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, MeasurementUnit


class IngredientInline(admin.StackedInline):
	model = RecipeIngredient
	extra = 5


class RecipeAdmin(admin.ModelAdmin):
	inlines = [IngredientInline]
	list_display = ["title"]


class IngredientAdmin(admin.ModelAdmin):
	list_display = [
		"title",
		"measurement_unit",
		"total_weight",
		"cost"
	]
	list_filter = ["measurement_unit"]


class MeasurementUnitAdmin(admin.ModelAdmin):
	list_display = ["title", "symbol", "grams_per_unit"]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(MeasurementUnit, MeasurementUnitAdmin)