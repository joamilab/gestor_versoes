# Generated by Django 2.1.4 on 2019-02-26 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versionamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='data_pub',
            field=models.DateField(),
        ),
    ]
