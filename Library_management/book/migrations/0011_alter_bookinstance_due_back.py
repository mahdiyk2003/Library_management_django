# Generated by Django 4.2.1 on 2023-06-06 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_book_thumbnail_alter_bookinstance_due_back'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 21, 7, 3, 11, 47997)),
        ),
    ]