# Generated by Django 4.1.5 on 2023-04-30 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название новости')),
                ('full_text', models.TextField(max_length=2000, verbose_name='Содержание новости')),
                ('author', models.CharField(blank=True, default='unknown', max_length=50, verbose_name='Автор новости')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Иконка новости (4х4)')),
                ('info', models.TextField(blank=True, default=None, max_length=2000, null=True, verbose_name='Дополнительная информация')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление новости')),
            ],
            options={
                'verbose_name': 'Новости сайта',
                'verbose_name_plural': 'Новости сайта',
            },
        ),
    ]
