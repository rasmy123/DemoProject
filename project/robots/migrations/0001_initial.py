# Generated by Django 3.0 on 2020-09-22 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Group', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Model', models.CharField(max_length=50)),
                ('SN', models.CharField(max_length=50)),
                ('Software', models.CharField(blank=True, max_length=50, null=True)),
                ('MAC', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='robots.Category')),
                ('Location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='robots.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('Process_ID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Schedule', models.DateTimeField()),
                ('Flag', models.BooleanField(default=False)),
                ('Robot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='robots.Robot')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start', models.DateTimeField(blank=True, null=True)),
                ('Stop', models.DateTimeField(blank=True, null=True)),
                ('Forward', models.DateTimeField(blank=True, null=True)),
                ('Backward', models.DateTimeField(blank=True, null=True)),
                ('Backward_Error', models.DateTimeField(blank=True, null=True)),
                ('Status', models.CharField(choices=[('IOT', 'INTERNET OF THINGS'), ('MANUAL', 'MANUAL'), ('SWITCH', 'SWICTH CLICK'), ('LS', 'LOCAL SCHEDULE')], max_length=50)),
                ('Process_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='robots.Schedule')),
                ('Robot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='robots.Robot')),
            ],
        ),
    ]
