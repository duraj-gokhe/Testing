# Generated by Django 2.1.7 on 2020-02-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0002_auto_20200217_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='UserName',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
