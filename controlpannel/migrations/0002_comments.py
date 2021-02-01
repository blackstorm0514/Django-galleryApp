# Generated by Django 3.1.5 on 2021-01-31 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
        ('controlpannel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('P_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlpannel.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authorization.user')),
            ],
        ),
    ]
