# Generated by Django 4.2.10 on 2024-02-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0007_rename_portfolio_userprofileinfo_portfolio_site_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='media/profile_pics'),
        ),
    ]