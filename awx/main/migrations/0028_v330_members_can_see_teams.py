# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 19:18
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

import awx.main.fields

from awx.main.migrations import ActivityStreamDisabledMigration
from awx.main.migrations import _rbac as rbac
from awx.main.migrations import _migration_utils as migration_utils


class Migration(ActivityStreamDisabledMigration):

    dependencies = [
        ('main', '0027_v330_add_tower_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='read_role',
            field=awx.main.fields.ImplicitRoleField(null=b'True', on_delete=django.db.models.deletion.CASCADE, parent_role=[b'organization.auditor_role', b'organization.member_role', b'member_role'], related_name='+', to='main.Role'),
        ),
        migrations.RunPython(migration_utils.set_current_apps_for_migrations),
        migrations.RunPython(rbac.rebuild_role_hierarchy),
    ]
