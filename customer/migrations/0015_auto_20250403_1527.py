# Generated by Django 3.0.5 on 2025-04-03 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0014_auto_20250403_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claims',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to=settings.AUTH_USER_MODEL),
        ),
    ]
