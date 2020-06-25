# Generated by Django 3.0.1 on 2020-02-17 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0026_auto_20200217_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('1', 'Обновлено'), ('0', 'На обновлении')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='access',
            name='lvl',
            field=models.CharField(choices=[('w', 'Запись'), ('r', 'Чтение')], help_text='Уровень доступа', max_length=40, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='term',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='problem.Term', verbose_name='Назначение'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.ForeignKey(blank=True, help_text='Статус в доброделе', null=True, on_delete=django.db.models.deletion.PROTECT, to='problem.Status', verbose_name='Статус в доброделе'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='visible',
            field=models.CharField(choices=[('0', 'Не показывать'), ('1', 'Показывать')], default='1', help_text='Режим показа на сайте', max_length=50, verbose_name='Режим'),
        ),
        migrations.AlterField(
            model_name='term',
            name='problem',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='problem.Problem', verbose_name='Проблема'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('2', 'Исполнено'), ('0', 'На исполнении'), ('1', 'На согласовании')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
    ]