# Generated by Django 3.1 on 2020-08-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_author',
            field=models.CharField(default='', max_length=20, verbose_name='작성자'),
        ),
    ]
