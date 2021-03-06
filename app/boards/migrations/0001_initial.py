# Generated by Django 3.1.7 on 2021-03-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='게시판 이름')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000, verbose_name='내용')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='등록일')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='수정일')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.CharField(max_length=1000, verbose_name='내용')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='등록일')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='수정일')),
            ],
        ),
    ]
