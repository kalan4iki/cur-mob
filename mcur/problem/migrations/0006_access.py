# Generated by Django 3.0.1 on 2020-01-16 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problem', '0005_auto_20200116_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dost', models.ManyToManyField(help_text='Организация', to='problem.Curator', verbose_name='Организация')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name': 'доступ',
                'verbose_name_plural': 'доступы',
                'ordering': ['user'],
            },
        ),
    ]
