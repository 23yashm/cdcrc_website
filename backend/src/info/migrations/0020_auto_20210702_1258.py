# Generated by Django 3.1.9 on 2021-07-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0019_auto_20210602_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='brief',
            field=models.CharField(help_text='Try to keep it less than 300 chars', max_length=2000),
        ),
    ]
