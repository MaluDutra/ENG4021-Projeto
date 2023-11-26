# Generated by Django 3.2.13 on 2023-11-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdearte', '0002_rename_title_events_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='description',
        ),
        migrations.RemoveField(
            model_name='events',
            name='time',
        ),
        migrations.AddField(
            model_name='events',
            name='category',
            field=models.CharField(choices=[('C', 'Cinema'), ('T', 'Teatro'), ('S', 'Sebo'), ('F', 'Shows/Festas'), ('T', 'Eventos Temáticos'), ('E', 'Exposições')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='price',
            field=models.CharField(choices=[('G', 'Gratuito'), ('1', 'R$10-R$20'), ('2', 'R$20-R$40'), ('3', 'R$100-')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1, null=True),
        ),
    ]