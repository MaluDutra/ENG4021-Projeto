# Generated by Django 3.2.13 on 2023-12-04 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdearte', '0010_alter_events_recomendation'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]
