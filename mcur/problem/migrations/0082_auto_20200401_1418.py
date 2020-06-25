# Generated by Django 3.0.1 on 2020-04-01 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0081_auto_20200401_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='lvl',
            field=models.CharField(choices=[('w', 'Запись'), ('r', 'Чтение')], help_text='Уровень доступа', max_length=40, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('0', 'Закрыто'), ('1', 'В работе'), ('2', 'На модерации')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('2', 'Исполнено'), ('0', 'На исполнении'), ('1', 'На согласовании')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
    ]
