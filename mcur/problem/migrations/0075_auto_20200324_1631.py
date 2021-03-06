# Generated by Django 3.0.1 on 2020-03-24 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0074_auto_20200323_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(blank=True, help_text='ФИО заявителя', max_length=250, null=True, verbose_name='ФИО')),
                ('email', models.EmailField(blank=True, help_text='Почта заявителя', max_length=254, null=True, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'авторы',
                'ordering': ['email'],
            },
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['dateotv'], 'verbose_name': 'обращение', 'verbose_name_plural': 'обращения'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('1', 'Утверждено'), ('0', 'На согласовании'), ('2', 'Ответ отклонен')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='parsing',
            field=models.CharField(choices=[('0', 'На обновлении'), ('1', 'Обновлено')], default='0', help_text='Статус парсинга', max_length=50, verbose_name='Статус парсинга'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='statussys',
            field=models.CharField(choices=[('2', 'На модерации'), ('0', 'Закрыто'), ('1', 'В работе')], default='2', help_text='Статус проблемы', max_length=70, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='visible',
            field=models.CharField(choices=[('1', 'Показывать'), ('0', 'Не показывать'), ('2', 'Временно скрыто')], default='1', help_text='Режим показа на сайте', max_length=50, verbose_name='Режим'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('2', 'Исполнено'), ('1', 'На согласовании'), ('0', 'На исполнении')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='problem',
            name='author',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problem.Author', verbose_name='Автор обращения'),
        ),
    ]
