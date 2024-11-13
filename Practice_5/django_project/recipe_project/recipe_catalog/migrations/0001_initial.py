# Generated by Django 5.1.2 on 2024-11-12 13:40

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Название должно быть строковым значением', regex='^[A-Za-zА-Яа-яёЁ\\s]+$')])),
                ('raw_weight', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0.1, message='Сырой вес должен быть положительным числом')])),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0.1, message='Вес должен быть положительным числом')])),
                ('cost', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0.1, message='Цена должна быть положительным числом')])),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, validators=[django.core.validators.RegexValidator(message='Название должно быть строковым значением', regex='^[A-Za-zА-Яа-яёЁ\\s]+$')])),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_catalog.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_catalog.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipe_catalog.RecipeIngredient', to='recipe_catalog.ingredient'),
        ),
        migrations.AddConstraint(
            model_name='recipeingredient',
            constraint=models.UniqueConstraint(fields=('recipe', 'ingredient'), name='unique recipes ingredients'),
        ),
    ]
