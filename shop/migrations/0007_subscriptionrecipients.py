# Generated by Django 3.2.2 on 2021-06-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionRecipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
