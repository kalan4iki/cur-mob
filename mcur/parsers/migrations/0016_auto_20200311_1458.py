# Generated by Django 3.0.1 on 2020-03-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsers', '0015_auto_20200310_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actionhistory',
            options={'ordering': ['-lastaction'], 'verbose_name': 'история действия', 'verbose_name_plural': 'истории действий'},
        ),
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ['pk'], 'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
        migrations.AlterField(
            model_name='actionhistory',
            name='arg',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Аргументы'),
        ),
        migrations.AlterField(
            model_name='actionhistory',
            name='status',
            field=models.CharField(choices=[('2', 'Ошибка'), ('1', 'Выполнено'), ('0', 'На выполнении')], default='0', max_length=50, verbose_name='Статус'),
        ),
    ]