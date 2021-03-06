# Generated by Django 3.0.1 on 2020-02-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0034_auto_20200219_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='lvl',
            field=models.CharField(choices=[('r', 'Чтение'), ('w', 'Запись')], help_text='Уровень доступа', max_length=40, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('0', 'На согласовании'), ('1', 'Утверждено'), ('2', 'Ответ отклонен')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Категория проблемы', max_length=255, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='curator',
            name='name',
            field=models.CharField(help_text='Куратор проблемы', max_length=100, verbose_name='Куратор'),
        ),
        migrations.AlterField(
            model_name='podcategory',
            name='name',
            field=models.CharField(help_text='Подкатегория проблемы', max_length=255, verbose_name='Подкатегория'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='parsing',
            field=models.CharField(choices=[('0', 'На обновлении'), ('1', 'Обновлено')], default='0', help_text='Статус парсинга', max_length=50, verbose_name='Статус парсинга'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('2', 'На модерации'), ('1', 'В работе'), ('0', 'Закрыто')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='visible',
            field=models.CharField(choices=[('0', 'Не показывать'), ('1', 'Показывать')], default='1', help_text='Режим показа на сайте', max_length=50, verbose_name='Режим'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('2', 'Исполнено'), ('0', 'На исполнении'), ('1', 'На согласовании')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
    ]
