# Generated by Django 4.2.9 on 2024-02-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_reviewpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewpost',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Posted')], default=1),
        ),
    ]
