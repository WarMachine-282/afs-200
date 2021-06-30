# Generated by Django 3.2.4 on 2021-06-30 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_alter_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ideas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imgURL', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]