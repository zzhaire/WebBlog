# Generated by Django 3.2.9 on 2023-06-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_bloginfo_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloginfo',
            name='cover',
            field=models.ImageField(blank=True, default='cover/default3.jpg', max_length=200, null=True, upload_to='%y/%m/%d', verbose_name='封面'),
        ),
    ]
