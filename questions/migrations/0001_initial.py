# Generated by Django 2.1.4 on 2019-01-10 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0002_auto_20190105_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['likes'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('body', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('solved', models.BooleanField(default=False)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='groups.Group')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.Question'),
        ),
    ]
