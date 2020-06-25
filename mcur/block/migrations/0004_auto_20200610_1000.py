# Generated by Django 3.0.1 on 2020-06-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_auto_20200603_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='nomkom',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='Номер комиссии'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='status',
            field=models.CharField(choices=[('1', 'На блокировке'), ('3', 'Отказано'), ('2', 'Заблокировано'), ('0', 'В работе')], default='0', help_text='Статус блокировки', max_length=50, verbose_name='Статус'),
        ),
    ]