# Generated by Django 2.2.11 on 2020-03-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_phno', models.BigIntegerField()),
                ('user_pass', models.CharField(max_length=50)),
            ],
        ),
    ]
