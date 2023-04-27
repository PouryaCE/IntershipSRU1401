# Generated by Django 4.2 on 2023-04-27 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_officemanager_professor_school_student_teacher_and_more'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summery_to_student', to='accounts.student')),
            ],
        ),
    ]
