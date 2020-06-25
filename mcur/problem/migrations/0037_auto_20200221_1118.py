# Generated by Django 3.0.1 on 2020-02-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0036_auto_20200221_1115'),
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
            field=models.CharField(choices=[('1', 'Утверждено'), ('2', 'Ответ отклонен'), ('0', 'На согласовании')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('1', 'В работе'), ('2', 'На модерации'), ('0', 'Закрыто')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='visible',
            field=models.CharField(choices=[('1', 'Показывать'), ('0', 'Не показывать')], default='1', help_text='Режим показа на сайте', max_length=50, verbose_name='Режим'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('1', 'На согласовании'), ('2', 'Исполнено'), ('0', 'На исполнении')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
    ]