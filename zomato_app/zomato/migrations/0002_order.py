# Generated by Django 4.2.4 on 2023-08-13 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('received', 'Received'), ('preparing', 'Preparing'), ('delivered', 'Delivered')], default='preparing', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('dishes', models.ManyToManyField(to='zomato.dish')),
            ],
        ),
    ]
