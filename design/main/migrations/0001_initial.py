# Generated by Django 5.0.6 on 2024-06-24 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('office_hours', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Связаться',
                'verbose_name_plural': 'Связаться',
            },
        ),
        migrations.CreateModel(
            name='OurProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('footage', models.FloatField()),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Наш проект',
                'verbose_name_plural': 'Наши проекты',
            },
        ),
        migrations.CreateModel(
            name='OurWorksVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Видео наших работ',
                'verbose_name_plural': 'Видео наших работ',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='WhyWeAre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Почему мы?',
                'verbose_name_plural': 'Почему мы?',
            },
        ),
        migrations.CreateModel(
            name='OurWorksVideoDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('our_works_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_urls', to='main.ourworksvideo')),
            ],
            options={
                'verbose_name': 'Отдельное видео наших работ',
                'verbose_name_plural': 'Отдельные видео наших работ',
            },
        ),
        migrations.CreateModel(
            name='ProjectPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_url', models.URLField()),
                ('description', models.TextField()),
                ('our_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_pictures', to='main.ourproject')),
            ],
            options={
                'verbose_name': 'Картинки наших проектов',
                'verbose_name_plural': 'Картинки наших проектов',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='main.rate')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='OneReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('surname', models.CharField(max_length=80)),
                ('photo_url', models.URLField()),
                ('title', models.CharField(max_length=80)),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='one_reviews', to='main.review')),
            ],
            options={
                'verbose_name': 'Конкретный отзыв',
                'verbose_name_plural': 'Конкретные отзывы',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='main.rate')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='ReasonsWhyWeAre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('picture_url', models.URLField()),
                ('why_we_are', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reasons', to='main.whyweare')),
            ],
            options={
                'verbose_name': 'Причины почему мы',
                'verbose_name_plural': 'Причины почему мы',
            },
        ),
    ]
