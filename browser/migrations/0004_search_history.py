# Generated by Django 2.1.3 on 2018-11-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0003_blacklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='search_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_item', models.CharField(max_length=999)),
                ('time_elapsed', models.CharField(max_length=999)),
                ('search_datetime', models.CharField(max_length=999)),
                ('items_total', models.CharField(max_length=999)),
                ('items_okidoki', models.CharField(max_length=999)),
                ('items_osta', models.CharField(max_length=999)),
                ('items_soov', models.CharField(max_length=999)),
                ('items_kuldnebors', models.CharField(max_length=999)),
            ],
        ),
    ]
