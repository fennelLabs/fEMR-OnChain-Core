# Generated by Django 3.2.4 on 2021-06-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_chiefcomplaint_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientencounter',
            name='pharmacy_notes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='patientencounter',
            name='procedure',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
