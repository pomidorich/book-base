# Generated by Django 4.1.1 on 2022-09-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksappBook',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=255)),
                ('author_name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'bookdb',
                'managed': True,
            },
        ),
    ]
