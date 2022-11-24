# Generated by Django 3.1.5 on 2022-07-22 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_contact_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('mb_id', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reply', models.TextField(blank=True, null=True)),
            ],
        ),
    ]