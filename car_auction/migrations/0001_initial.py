# Generated by Django 4.2.13 on 2024-05-19 05:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1970), django.core.validators.MaxValueValidator(2070)])),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('add_date', models.DateField(auto_now_add=True, verbose_name='Время')),
                ('city', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32, verbose_name='Страна')),
                ('mileage', models.PositiveSmallIntegerField(default=0, verbose_name='Пробег')),
                ('with_photo', models.BooleanField(default=True)),
                ('drive', models.CharField(choices=[('Задний', 'Задний'), ('Передний', 'Передний'), ('Полный привод', 'Полный привод')], max_length=16, verbose_name='Привод')),
                ('volume', models.FloatField(default=0.8)),
            ],
        ),
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_make_name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=32, unique=True)),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_auction.carmake')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_auction.car')),
                ('parent_review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car_auction.comment')),
            ],
        ),
        migrations.AddField(
            model_name='carmake',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_auction.category'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_auction.carmake'),
        ),
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_auction.category'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_auction.model'),
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('total_price', models.IntegerField(default=0)),
                ('buy_now', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car_auction.car')),
            ],
        ),
    ]