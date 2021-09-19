# Generated by Django 3.0.4 on 2020-06-01 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ManyToManyField(related_name='from_user', to='Profile.User_Profile')),
                ('to_user', models.ManyToManyField(related_name='to_user', to='Profile.User_Profile')),
            ],
        ),
    ]
