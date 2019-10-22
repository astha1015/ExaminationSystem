# Generated by Django 2.2.5 on 2019-10-22 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_id', models.IntegerField(primary_key=True, serialize=False)),
                ('exam_name', models.TextField(blank=True, null=True)),
                ('exam_type_id', models.IntegerField(blank=True, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('teacher_id', models.IntegerField(blank=True, null=True)),
                ('exam_question_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'exam',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExaminationQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'examination_question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExamQuestion',
            fields=[
                ('exam_question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('exam_type_id', models.IntegerField(blank=True, null=True)),
                ('mc_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'exam_question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExamResults',
            fields=[
                ('exam_results_id', models.IntegerField(primary_key=True, serialize=False)),
                ('exam_results', models.TextField(blank=True, null=True)),
                ('student_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'exam_results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('exam_type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('exam_type_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'exam_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('mc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mc_name', models.TextField(blank=True, null=True)),
                ('answer1', models.TextField(blank=True, null=True)),
                ('answer2', models.TextField(blank=True, null=True)),
                ('answer3', models.TextField(blank=True, null=True)),
                ('answer4', models.TextField(blank=True, null=True)),
                ('correct_answer', models.TextField(blank=True, null=True)),
                ('question_type_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'multiple_choice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('question_type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('question_type_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'question_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
