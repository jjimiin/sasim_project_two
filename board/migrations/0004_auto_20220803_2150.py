# Generated by Django 3.1.5 on 2022-08-03 12:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_contact_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_contact',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
