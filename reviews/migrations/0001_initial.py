# Generated by Django 4.1.7 on 2023-03-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
