# Generated by Django 3.0.1 on 2020-02-25 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0044_auto_20200225_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='resolution',
            name='prob',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='problem.Problem'),
        ),
        migrations.AlterField(
            model_name='access',
            name='lvl',
            field=models.CharField(choices=[('w', 'Запись'), ('r', 'Чтение')], help_text='Уровень доступа', max_length=40, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('2', 'Ответ отклонен'), ('0', 'На согласовании'), ('1', 'Утверждено')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='parsing',
            field=models.CharField(choices=[('0', 'На обновлении'), ('1', 'Обновлено')], default='0', help_text='Статус парсинга', max_length=50, verbose_name='Статус парсинга'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('1', 'В работе'), ('2', 'На модерации'), ('0', 'Закрыто')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='resolution',
            name='date',
            field=models.DateField(blank=True, help_text='Срок резолюции', null=True, verbose_name='Срок'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('0', 'На исполнении'), ('1', 'На согласовании'), ('2', 'Исполнено')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
    ]
