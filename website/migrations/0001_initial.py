# Generated by Django 2.2.12 on 2020-05-29 14:08

from django.db import migrations, models
import taggit.managers
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('icon_color_tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('details', models.CharField(blank=True, max_length=500)),
                ('fromdate', models.DateField()),
                ('todate', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('image', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('about', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WebAppDeveloper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('desc', models.CharField(blank=True, max_length=500)),
                ('fromdate', models.DateField()),
                ('todate', models.CharField(blank=True, max_length=500)),
                ('project_link', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to=website.models.get_upload_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=website.models.get_upload_path, verbose_name='')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='icon_color_tags.TaggedThing', to='icon_color_tags.IconColorTag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareDevelopment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('desc', models.CharField(blank=True, max_length=500)),
                ('fromdate', models.DateField()),
                ('todate', models.CharField(blank=True, max_length=500)),
                ('project_link', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to=website.models.get_upload_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=website.models.get_upload_path, verbose_name='')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='icon_color_tags.TaggedThing', to='icon_color_tags.IconColorTag', verbose_name='Tags')),
            ],
        ),
    ]
