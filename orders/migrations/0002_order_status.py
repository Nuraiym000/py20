# Generated by Django 4.0.5 on 2022-07-08 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('open', 'Открыт'), ('in_process', 'В обработке'), ('canceled', 'Отмененный'), ('finished', 'Завершенный')], default='open', max_length=20),
        ),
    ]
