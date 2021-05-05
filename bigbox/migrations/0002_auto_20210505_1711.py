# Generated by Django 2.2 on 2021-05-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='slug',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='box',
            name='activities',
            field=models.ManyToManyField(to='bigbox.Activity', verbose_name='actividades'),
        ),
    ]
