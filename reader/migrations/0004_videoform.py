# Generated by Django 4.0.2 on 2022-02-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0003_alter_pdfform_language_alter_textform_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoType', models.FileField(upload_to='videos')),
                ('audioType', models.FileField(upload_to='audios')),
            ],
        ),
    ]