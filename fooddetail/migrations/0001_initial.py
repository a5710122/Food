# Generated by Django 2.0.6 on 2018-07-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_text', models.CharField(max_length=200)),
                ('number_sugar', models.IntegerField(default=0)),
            ],
        ),
    ]
