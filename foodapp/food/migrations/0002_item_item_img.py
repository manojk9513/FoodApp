# Generated by Django 4.1 on 2022-08-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_img',
            field=models.CharField(default='https://theme-assets.getbento.com/sensei/2f8309a.sensei/assets/images/catering-item-placeholder-704x520.png', max_length=500),
        ),
    ]