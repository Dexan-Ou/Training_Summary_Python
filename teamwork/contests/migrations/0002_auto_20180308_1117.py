# Generated by Django 2.0.3 on 2018-03-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='cid',
        ),
        migrations.AddField(
            model_name='contest',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contest',
            name='num_of_problem',
            field=models.IntegerField(choices=[(5, '5 - E'), (6, '6 - F'), (7, '7 - G'), (8, '8 - H'), (9, '9 - I'), (10, '10 - J'), (11, '11 - K'), (12, '12 - L'), (13, '13 - M')], default=5),
        ),
    ]