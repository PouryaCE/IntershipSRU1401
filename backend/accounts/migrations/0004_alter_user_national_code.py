# Generated by Django 4.2 on 2023-04-24 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='national_code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
