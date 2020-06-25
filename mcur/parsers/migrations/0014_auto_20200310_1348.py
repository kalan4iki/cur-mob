# Generated by Django 3.0.1 on 2020-03-10 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsers', '0013_auto_20200310_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionhistory',
            name='pars',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parsers', to='parsers.Parser', verbose_name='Парсер'),
        ),
        migrations.AlterField(
            model_name='actionhistory',
            name='status',
            field=models.CharField(choices=[('1', 'Выполнено'), ('0', 'На выполнении')], default='0', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='loggings',
            name='name',
            field=models.CharField(choices=[('1', 'Обновлено'), ('0', 'Добавлено'), ('2', 'Прочее')], default='0', max_length=50, verbose_name='Статус'),
        ),
    ]
