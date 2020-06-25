# Generated by Django 3.0.1 on 2020-02-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0040_auto_20200221_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='resolution',
            name='datecre',
            field=models.DateField(auto_now_add=True, help_text='Дата создания', null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='access',
            name='lvl',
            field=models.CharField(choices=[('w', 'Запись'), ('r', 'Чтение')], help_text='Уровень доступа', max_length=40, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='parsing',
            field=models.CharField(choices=[('0', 'На обновлении'), ('1', 'Обновлено')], default='0', help_text='Статус парсинга', max_length=50, verbose_name='Статус парсинга'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('0', 'Закрыто'), ('1', 'В работе'), ('2', 'На модерации')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('1', 'На согласовании'), ('0', 'На исполнении'), ('2', 'Исполнено')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
    ]