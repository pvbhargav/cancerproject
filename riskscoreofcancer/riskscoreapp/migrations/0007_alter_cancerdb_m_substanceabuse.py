# Generated by Django 5.0 on 2024-05-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskscoreapp', '0006_alter_cancerdb_m_cancertype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Substanceabuse',
            field=models.CharField(choices=[('TeeTotaler', 'TeeTotaler'), ('Not a TeeTotaler', 'Not a TeeTotaler')], max_length=40),
        ),
    ]
