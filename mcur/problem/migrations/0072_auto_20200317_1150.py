# Generated by Django 3.0.1 on 2020-03-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0071_auto_20200316_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='lvl',
            field=models.CharField(choices=[('r', 'Чтение'), ('w', 'Запись')], help_text='Уровень доступа', max_length=40, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='parsing',
            field=models.CharField(choices=[('1', 'Обновлено'), ('0', 'На обновлении')], default='0', help_text='Статус парсинга', max_length=50, verbose_name='Статус парсинга'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('0', 'Закрыто'), ('2', 'На модерации'), ('1', 'В работе')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='visible',
            field=models.CharField(choices=[('2', 'Временно скрыто'), ('0', 'Не показывать'), ('1', 'Показывать')], default='1', help_text='Режим показа на сайте', max_length=50, verbose_name='Режим'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('1', 'На согласовании'), ('0', 'На исполнении'), ('2', 'Исполнено')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
    ]
