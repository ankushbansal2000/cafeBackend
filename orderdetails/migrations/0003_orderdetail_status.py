# Generated by Django 3.0.4 on 2020-05-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderdetails', '0002_orderdetail_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
