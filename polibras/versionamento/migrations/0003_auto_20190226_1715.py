# Generated by Django 2.1.4 on 2019-02-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versionamento', '0002_auto_20190226_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='data_pub',
            field=models.DateTimeField(),
        ),
    ]