# Generated by Django 3.2.5 on 2021-07-14 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0070_patientencounter_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyofpresentillness',
            name='narrative',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historyofpresentillness',
            name='onset',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historyofpresentillness',
            name='palliates',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historyofpresentillness',
            name='physical_examination',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='historyofpresentillness',
            name='provokes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historyofpresentillness',
            name='quality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historyofpresentillness',
            name='radiation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historyofpresentillness',
            name='severity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historyofpresentillness',
            name='time_of_day',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
