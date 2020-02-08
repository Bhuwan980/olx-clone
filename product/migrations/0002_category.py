# Generated by Django 3.0.1 on 2020-02-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(upload_to='category_image/')),
            ],
        ),
    ]