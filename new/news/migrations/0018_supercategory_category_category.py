# Generated by Django 4.1 on 2022-11-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_alter_news_cost_alter_news_rating_alter_news_we_have'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Назва супер кетегорії')),
            ],
            options={
                'verbose_name': 'Супер категорія',
                'verbose_name_plural': 'Супер категорія',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.ManyToManyField(blank=True, to='news.supercategory'),
        ),
    ]
