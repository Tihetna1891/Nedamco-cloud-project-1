# Generated by Django 3.2.21 on 2023-10-04 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
            preserve_default=False,
        ),
    ]
