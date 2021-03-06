# Generated by Django 3.0.1 on 2020-02-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0035_auto_20200219_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='lvl',
            field=models.CharField(choices=[('w', 'Запись'), ('r', 'Чтение')], help_text='Уровень доступа', max_length=40, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('1', 'Утверждено'), ('0', 'На согласовании'), ('2', 'Ответ отклонен')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('0', 'Закрыто'), ('1', 'В работе'), ('2', 'На модерации')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('0', 'На исполнении'), ('1', 'На согласовании'), ('2', 'Исполнено')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
    ]
