# Generated by Django 3.0.1 on 2020-03-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsers', '0020_auto_20200317_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionhistory',
            name='status',
            field=models.CharField(choices=[('2', 'Ошибка'), ('1', 'Выполнено'), ('0', 'На выполнении')], default='0', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='loggings',
            name='name',
            field=models.CharField(choices=[('2', 'Прочее'), ('1', 'Обновлено'), ('0', 'Добавлено')], default='0', max_length=50, verbose_name='Статус'),
        ),
    ]