# Generated by Django 3.0.1 on 2020-02-17 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0021_auto_20200206_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Категория проблемы', max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'категория проблемы',
                'verbose_name_plural': 'категории проблем',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='access',
            name='lvl',
            field=models.CharField(choices=[('w', 'Запись'), ('r', 'Чтение')], help_text='Уровень доступа', max_length=40, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='term',
            name='status',
            field=models.CharField(choices=[('0', 'На исполнении'), ('2', 'Исполнено'), ('1', 'На согласовании')], default='0', help_text='Статус ответа', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='post',
            field=models.CharField(blank=True, default=None, help_text='Должность', max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.CreateModel(
            name='Podcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Подкатегория проблемы', max_length=100, verbose_name='Подкатегория')),
                ('categ', models.ForeignKey(help_text='Категория проблемы', on_delete=django.db.models.deletion.PROTECT, to='problem.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'подкатегория проблемы',
                'verbose_name_plural': 'подкатегории проблем',
                'ordering': ['name'],
            },
        ),
    ]