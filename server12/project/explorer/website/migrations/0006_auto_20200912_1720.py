# Generated by Django 3.0.5 on 2020-09-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200910_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_desc',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_desc',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
