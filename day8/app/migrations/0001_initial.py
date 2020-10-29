# Generated by Django 2.0.6 on 2020-10-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.SmallIntegerField(choices=[(0, '男'), (1, '女'), (2, '未知')], default=0)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('pic', models.ImageField(default='pic/1.jpg', upload_to='pic/')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'db_table': 't_student',
            },
        ),
    ]