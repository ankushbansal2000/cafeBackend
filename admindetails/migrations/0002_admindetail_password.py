# Generated by Django 2.2.4 on 2020-03-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admindetail',
            name='password',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
