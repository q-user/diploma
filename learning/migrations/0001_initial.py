# Generated by Django 3.0.6 on 2020-06-09 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Область')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Область обучения',
                'verbose_name_plural': 'Области обучения',
            },
        ),
        migrations.CreateModel(
            name='FormatCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип курса')),
            ],
            options={
                'verbose_name': 'Тип курса',
                'verbose_name_plural': 'Тип курса',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Язык курса')),
            ],
            options={
                'verbose_name': 'Язык курса',
                'verbose_name_plural': 'Язык курса',
            },
        ),
        migrations.CreateModel(
            name='TypeRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тип оценивания')),
            ],
            options={
                'verbose_name': 'Тип оценивания',
                'verbose_name_plural': 'Тип оценивания',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название курса')),
                ('img', models.ImageField(upload_to='img/', verbose_name='Изображение курса')),
                ('duration', models.TimeField(verbose_name='Длительность курса')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('areas', models.ManyToManyField(related_name='areas_course', to='learning.CourseAreas', verbose_name='Область курса')),
                ('format_course', models.ManyToManyField(related_name='format_type', to='learning.FormatCourse', verbose_name='Тип курса')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='language_course', to='learning.Language', verbose_name='Язык курса')),
                ('type_rating', models.ManyToManyField(related_name='rating_type', to='learning.TypeRating', verbose_name='Формат проверки')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]