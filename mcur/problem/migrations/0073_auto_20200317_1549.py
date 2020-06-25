# Generated by Django 3.0.1 on 2020-03-17 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0072_auto_20200317_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='minis',
            options={'ordering': ['pk'], 'verbose_name': 'территориальное уравление', 'verbose_name_plural': 'территориальные уравления'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ty',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problem.Minis', verbose_name='Тер. управление'),
        ),
        migrations.AlterField(
            model_name='access',
            name='lvl',
            field=models.CharField(choices=[('w', 'Запись'), ('r', 'Чтение')], help_text='Уровень доступа', max_length=40, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='minis',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='ciogv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='problem.Minis', verbose_name='Тер. управление'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='parsing',
            field=models.CharField(choices=[('0', 'На обновлении'), ('1', 'Обновлено')], default='0', help_text='Статус парсинга', max_length=50, verbose_name='Статус парсинга'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('1', 'В работе'), ('0', 'Закрыто'), ('2', 'На модерации')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='visible',
            field=models.CharField(choices=[('1', 'Показывать'), ('2', 'Временно скрыто'), ('0', 'Не показывать')], default='1', help_text='Режим показа на сайте', max_length=50, verbose_name='Режим'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('0', 'На исполнении'), ('1', 'На согласовании'), ('2', 'Исполнено')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
    ]
