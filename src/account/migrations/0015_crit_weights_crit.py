# Generated by Django 4.2.4 on 2023-11-27 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_weights'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crit', models.CharField(default='NA', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='weights',
            name='crit',
            field=models.ForeignKey(default='NA', on_delete=django.db.models.deletion.CASCADE, to='account.crit'),
        ),
    ]
