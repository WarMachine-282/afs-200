# Generated by Django 3.2.4 on 2021-06-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=100),
        ),
    ]
