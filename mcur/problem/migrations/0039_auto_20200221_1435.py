# Generated by Django 3.0.1 on 2020-02-21 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('problem', '0038_auto_20200221_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('1', 'Утверждено'), ('2', 'Ответ отклонен'), ('0', 'На согласовании')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='parsing',
            field=models.CharField(choices=[('1', 'Обновлено'), ('0', 'На обновлении')], default='0', help_text='Статус парсинга', max_length=50, verbose_name='Статус парсинга'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('0', 'Закрыто'), ('1', 'В работе'), ('2', 'На модерации')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('2', 'Исполнено'), ('1', 'На согласовании'), ('0', 'На исполнении')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'резолюция',
                'verbose_name_plural': 'резолюции',
                'ordering': ['object_id'],
            },
        ),
    ]
