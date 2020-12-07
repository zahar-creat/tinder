# Generated by Django 2.2.17 on 2020-12-07 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tinder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='investor',
        ),
        migrations.RemoveField(
            model_name='users',
            name='no_list',
        ),
        migrations.RemoveField(
            model_name='users',
            name='yes_list',
        ),
        migrations.AddField(
            model_name='users',
            name='user_type',
            field=models.CharField(choices=[('Инвестор', 'Инвестор'), ('Пользователь', 'Пользователь')], default='Инвестор', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='pitch_desk',
            field=models.FileField(upload_to='pitchdeck/'),
        ),
        migrations.AlterField(
            model_name='users',
            name='company_type',
            field=models.CharField(choices=[('Компания', 'Компания'), ('Частное лицо', 'Частное лицо'), ('Фонд', 'Фонд')], default='Компания', max_length=100),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='image/')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tinder.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choicetype', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tinder.Project')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='choicelist',
            field=models.ManyToManyField(through='tinder.Choice', to='tinder.Project'),
        ),
    ]
