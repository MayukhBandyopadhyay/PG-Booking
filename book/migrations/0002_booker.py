# Generated by Django 5.0.6 on 2024-06-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=50)),
                ('adh', models.IntegerField()),
                ('addr', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
