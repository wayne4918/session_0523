# Generated by Django 5.0.6 on 2024-05-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0002_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
