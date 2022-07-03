# Generated by Django 4.0.5 on 2022-07-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ф И О')),
                ('phone', models.CharField(max_length=15, verbose_name='ТЕЛЕФОН')),
                ('description', models.TextField(blank=True, verbose_name='Коментария')),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Форма обратной связи',
            },
        ),
    ]
