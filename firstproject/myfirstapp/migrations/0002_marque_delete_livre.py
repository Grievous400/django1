# Generated by Django 4.0.4 on 2022-05-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_marque', models.CharField(max_length=100)),
                ('createur', models.CharField(max_length=100)),
                ('date_creation', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Livre',
        ),
    ]
