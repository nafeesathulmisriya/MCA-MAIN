# Generated by Django 3.0.5 on 2025-03-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0012_alter_category_id_alter_claim_id_alter_policy_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='supporting_document',
            field=models.FileField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='policyrecord',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
