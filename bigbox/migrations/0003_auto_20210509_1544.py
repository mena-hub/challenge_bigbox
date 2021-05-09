# Generated by Django 2.2 on 2021-05-09 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bigbox', '0002_auto_20210505_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'experiencia', 'verbose_name_plural': 'experiencias'},
        ),
        migrations.AlterModelOptions(
            name='box',
            options={'verbose_name': 'box', 'verbose_name_plural': 'boxes'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'categoría', 'verbose_name_plural': 'categorías'},
        ),
        migrations.AlterModelOptions(
            name='reason',
            options={'verbose_name': 'ocasión', 'verbose_name_plural': 'ocasiones'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bigbox.Category', verbose_name='categorías'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='internal_name',
            field=models.CharField(max_length=200, verbose_name='nombre interno'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='reasons',
            field=models.ManyToManyField(blank=True, to='bigbox.Reason', verbose_name='ocasiones'),
        ),
        migrations.AlterField(
            model_name='box',
            name='activities',
            field=models.ManyToManyField(to='bigbox.Activity', verbose_name='experiencias'),
        ),
        migrations.AlterField(
            model_name='box',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bigbox.Category', verbose_name='categorías'),
        ),
        migrations.AlterField(
            model_name='box',
            name='internal_name',
            field=models.CharField(max_length=200, verbose_name='nombre interno'),
        ),
        migrations.AlterField(
            model_name='box',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='box',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='reason',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
    ]