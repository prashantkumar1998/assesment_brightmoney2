# Generated by Django 4.2.6 on 2023-10-08 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_transaction_user_delete_appuser'),
        ('userloan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='users.user'),
        ),
    ]