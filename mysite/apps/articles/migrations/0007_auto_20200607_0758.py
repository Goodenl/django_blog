# Generated by Django 3.0.5 on 2020-06-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20200607_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_tags',
            field=models.CharField(max_length=100, null=True, verbose_name='тэги статьи'),
        ),
    ]
