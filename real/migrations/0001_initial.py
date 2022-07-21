# Generated by Django 3.2 on 2022-07-12 06:33

import ckeditor.fields
import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('fullname', models.CharField(default='', max_length=50)),
                ('usertitle', models.CharField(default='', max_length=50)),
                ('about', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('phonenumber', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('facebook_link', models.CharField(max_length=50)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('twitter_link', models.CharField(max_length=200)),
                ('google_link', models.CharField(max_length=200)),
                ('linkdin', models.CharField(max_length=200)),
                ('photo', models.FileField(default='avatar.png', upload_to='images/profile_img')),
                ('address', models.TextField()),
                ('package', models.CharField(choices=[('BASIC PACKAGE', 'BASIC PACKAGE'), ('PLATINUM PACKAGE', 'PLATINUM PACKAGE'), ('STANDARD PACKAGE', 'STANDARD PACKAGE')], default='BASIC PACKAGE', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
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
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('property_type', models.CharField(max_length=225)),
                ('price', models.FloatField()),
                ('area', models.CharField(max_length=225)),
                ('bedrooms', models.CharField(max_length=225)),
                ('bathrooms', models.CharField(max_length=225)),
                ('location', models.CharField(max_length=225)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('building_Age', models.CharField(blank=True, max_length=225, null=True)),
                ('garage', models.CharField(blank=True, default=0, max_length=225, null=True)),
                ('Rooms', models.CharField(blank=True, max_length=225, null=True)),
                ('sqft', models.CharField(max_length=225)),
                ('image', models.FileField(upload_to='images/photos')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='images/photos')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='images/photos')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='images/photos')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.CharField(max_length=225)),
                ('contact_phone', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('property_type', models.CharField(max_length=225)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('area', models.CharField(max_length=225)),
                ('bedrooms', models.CharField(max_length=225)),
                ('bathrooms', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('building_Age', models.CharField(blank=True, max_length=225, null=True)),
                ('garage', models.CharField(blank=True, default=0, max_length=225, null=True)),
                ('Rooms', models.CharField(blank=True, max_length=225, null=True)),
                ('sqft', models.CharField(max_length=225)),
                ('image', models.FileField(upload_to='images/photos')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='images/photos')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='images/photos')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='images/photos')),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
                ('listing_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=20)),
                ('body', ckeditor.fields.RichTextField()),
                ('image', models.FileField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('property_title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='real.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=50)),
                ('landline', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('is_approve', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
                ('user_agent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmarklisting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='real.listing', verbose_name='Property bookmark')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'property')},
            },
        ),
    ]
