# Generated by Django 2.2.3 on 2019-07-12 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=15)),
                ('student_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Grades')),
            ],
        ),
    ]