# Generated by Django 4.2.1 on 2023-06-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_file',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]