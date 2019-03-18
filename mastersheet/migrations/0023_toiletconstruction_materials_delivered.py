# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mastersheet', '0022_auto_20181213_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='toiletconstruction',
            name='materials_delivered',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
    ]
