# Generated by Django 3.0.5 on 2025-03-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0008_remove_claim_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='reason',
            field=models.CharField(default='No reason provided', max_length=255),
        ),
    ]
