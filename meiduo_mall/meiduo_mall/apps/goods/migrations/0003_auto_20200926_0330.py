# Generated by Django 3.1 on 2020-09-26 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20190327_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodschannel',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goods.goodschannelgroup', verbose_name='频道组名'),
        ),
    ]