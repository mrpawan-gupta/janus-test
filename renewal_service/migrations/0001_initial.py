# Generated by Django 4.1.5 on 2023-01-12 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=15, null=True, unique=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=200)),
                ('ktp_number', models.CharField(blank=True, default=None, max_length=15, null=True, unique=True)),
                ('is_applicable', models.BooleanField(default=True, help_text='The customer data is correct/same')),
                ('is_verified', models.BooleanField(default=False, help_text='Customer data is Verified by agent')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('address', models.TextField(blank=True)),
                ('locality', models.TextField(blank=True)),
                ('zipcode', models.CharField(blank=True, max_length=50, null=True)),
                ('province', models.TextField(default='')),
                ('city', models.TextField(default='')),
                ('flat_no', models.TextField(default='')),
                ('lane', models.TextField(default='')),
                ('block', models.TextField(default='')),
                ('is_serviceable', models.BooleanField(default=False)),
                ('serviceable_epoch', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'customer_address',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('description', models.TextField(blank=True, default='')),
                ('is_active', models.BooleanField(default=True, help_text='Show all active service provide by us')),
            ],
            options={
                'db_table': 'service',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=25, null=True, unique=True)),
                ('phone', models.CharField(blank=True, default=None, max_length=15, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=200, unique=True)),
                ('password', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('otp', models.IntegerField(blank=True)),
                ('otp_sent_time', models.DateTimeField(auto_now_add=True)),
                ('is_blocked', models.BooleanField(default=False)),
                ('otp_hashed', models.CharField(blank=True, max_length=64)),
            ],
            options={
                'db_table': 'user',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='VehicleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('number', models.CharField(db_index=True, max_length=15, unique=True)),
                ('stnk_number', models.CharField(max_length=15, unique=True)),
                ('vehicle_tax', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('expiry_slot_id', models.IntegerField(db_index=True, default=0, help_text='date in format of YYMMDD')),
                ('is_active', models.BooleanField(default=True, help_text='check if the vehicle is registered with ins')),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'vehicle_info',
                'ordering': ['-id'],
                'unique_together': {('number', 'stnk_number')},
            },
        ),
        migrations.CreateModel(
            name='RenewalOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('P', 'Processed'), ('I', 'In Transit'), ('D', 'Delivered'), ('C', 'Completed'), ('X', 'Canceled'), ('V', 'Verified'), ('A', 'Active')], default='P', max_length=10)),
                ('slot_id', models.IntegerField(db_index=True, default=0, help_text='date in format of YYMMDD')),
                ('type', models.IntegerField(choices=[(0, 'Self Pickup and Drop'), (1, 'Home Pickup and Drop')], default=0)),
                ('is_active', models.BooleanField(default=True, help_text='check if the vehicle is registered with insureka')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('net_amount', models.DecimalField(decimal_places=2, default=0, help_text='amount after all deducting', max_digits=8)),
                ('discount_amount', models.DecimalField(decimal_places=2, default=0, help_text='deduction amount', max_digits=8)),
                ('coupon_code', models.CharField(blank=True, max_length=10, null=True)),
                ('pkb_amount', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('payment', models.IntegerField(choices=[(0, 'default'), (1, 'COD'), (2, 'ONLINE')], default=0)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='renewal_service.customer')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='renewal_service.service')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='renewal_service.vehicleinfo')),
            ],
            options={
                'db_table': 'renewal_order',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renewal_service.customeraddress'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='renewal_service.user'),
        ),
    ]