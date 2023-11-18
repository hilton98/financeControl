# Generated by Django 4.2.7 on 2023-11-18 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('indicators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=15)),
                ('surname', models.CharField(max_length=15)),
                ('born_dt', models.DateTimeField()),
                ('cpf', models.CharField(max_length=11)),
                ('creation_dt', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicators.flag')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100)),
                ('creation_dt', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.person')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_status', to='indicators.flag')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_type', to='indicators.flag')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=30)),
                ('neighborhood', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=8)),
                ('creation_dt', models.DateTimeField(auto_now_add=True)),
                ('activated', models.BooleanField(default=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.person')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicators.flag')),
            ],
        ),
    ]
