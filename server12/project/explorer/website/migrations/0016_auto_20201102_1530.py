# Generated by Django 3.1.2 on 2020-11-02 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_customer_bill_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='bil_pin',
            new_name='bill_pin',
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('t_amt', models.IntegerField()),
                ('flag', models.IntegerField()),
                ('ship_add', models.CharField(max_length=255, null=True)),
                ('ship_city', models.CharField(max_length=30, null=True)),
                ('ship_pin', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('order_status', models.BooleanField(default='0')),
                ('payment_status', models.BooleanField(default='0')),
                ('cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.customer')),
                ('p', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.product')),
            ],
        ),
    ]
