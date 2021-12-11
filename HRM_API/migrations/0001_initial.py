# Generated by Django 3.2.9 on 2021-12-11 06:00

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accou_hol_name', models.CharField(max_length=255, null=True)),
                ('emp_id', models.IntegerField(null=True)),
                ('accou_num', models.CharField(max_length=255, null=True)),
                ('bank_name', models.CharField(max_length=255, null=True)),
                ('ifsc_code', models.CharField(max_length=255, null=True)),
                ('branch', models.CharField(max_length=255, null=True)),
                ('document', models.ImageField(null=True, upload_to='bankdoc/0')),
                ('note', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('history', models.TextField(blank=True, default='No History', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(null=True)),
                ('document_title', models.CharField(max_length=255, null=True)),
                ('Gov_id_1', models.CharField(choices=[('aadhar-card', 'AADHAR-CARD'), ('voter-card', 'VOTER-CARD'), ('pan-card', 'PAN-CARD')], default='aadharCard', max_length=20)),
                ('Gov_id_2', models.CharField(choices=[('aadhar-card', 'AADHAR-CARD'), ('voter-card', 'VOTER-CARD'), ('pan-card', 'PAN-CARD')], default='aadharCard', max_length=20)),
                ('Gov_id_3', models.CharField(choices=[('aadhar-card', 'AADHAR-CARD'), ('voter-card', 'VOTER-CARD'), ('pan-card', 'PAN-CARD')], default='aadharCard', max_length=20)),
                ('note', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('is_employer', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('position', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='HRM_API.user')),
                ('emp_id', models.CharField(default='emp697', max_length=70)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=125)),
                ('current_ddress', models.TextField(default='', max_length=100)),
                ('permanent_address', models.TextField(default='', max_length=100)),
                ('emergency', models.CharField(max_length=11)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=10)),
                ('joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('yoruba', 'YORUBA'), ('hausa', 'HAUSA'), ('french', 'FRENCH')], default='english', max_length=10)),
                ('document_status', models.CharField(choices=[('Provided', 'Provided'), ('Submitted', 'Submitted')], max_length=55, null=True)),
                ('bank', models.CharField(default='First Bank Plc', max_length=25)),
                ('salary', models.CharField(default='00,000.00', max_length=16)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRM_API.department')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=15)),
                ('end', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('approved', 'APPROVED'), ('unapproved', 'UNAPPROVED'), ('decline', 'DECLINED')], default='Not Approved', max_length=15)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM_API.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='HRM_API.user')),
                ('company', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('number_of_employees', models.IntegerField(blank=True, default=0, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRM_API.department')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HRM_API.employer'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('first_in', models.TimeField()),
                ('last_out', models.TimeField(null=True)),
                ('status', models.CharField(choices=[('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'), ('UNAVAILABLE', 'UNAVAILABLE')], max_length=15)),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRM_API.employee')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HRM_API.asset')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HRM_API.employee')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HRM_API.employer'),
        ),
    ]
