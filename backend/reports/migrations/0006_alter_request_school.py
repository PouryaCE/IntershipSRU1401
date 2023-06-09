# Generated by Django 4.1.7 on 2023-05-13 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_student_school2_alter_student_teacher2'),
        ('reports', '0005_remove_request_manager_request_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='school',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='office_request_school', to='accounts.school'),
            preserve_default=False,
        ),
    ]
