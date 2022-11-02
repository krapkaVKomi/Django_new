# Generated by Django 4.1 on 2022-11-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_alter_news_options_alter_news_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Назва кетегорії')),
                ('categores', models.ManyToManyField(blank=True, to='news.category')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
                'ordering': ['title'],
            },
        ),
    ]