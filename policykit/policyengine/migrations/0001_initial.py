# Generated by Django 3.0.7 on 2021-04-29 18:03

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import policyengine.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=1000, verbose_name='team_name')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='CommunityUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('readable_name', models.CharField(max_length=300, null=True, verbose_name='readable_name')),
                ('access_token', models.CharField(max_length=300, null=True, verbose_name='access_token')),
                ('is_community_admin', models.BooleanField(default=False)),
                ('avatar', models.CharField(max_length=500, null=True, verbose_name='avatar')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_policyengine.communityuser_set+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', policyengine.models.PolymorphicUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ConstitutionAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_post', models.CharField(max_length=300, null=True, verbose_name='community_post')),
                ('is_bundled', models.BooleanField(default=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community')),
            ],
            options={
                'verbose_name': 'constitutionaction',
                'verbose_name_plural': 'constitutionactions',
            },
        ),
        migrations.CreateModel(
            name='ConstitutionPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.TextField(blank=True, default='')),
                ('initialize', models.TextField(blank=True, default='')),
                ('check', models.TextField(blank=True, default='')),
                ('notify', models.TextField(blank=True, default='')),
                ('success', models.TextField(blank=True, default='')),
                ('fail', models.TextField(blank=True, default='')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_bundled', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community', verbose_name='community')),
            ],
            options={
                'verbose_name': 'constitutionpolicy',
                'verbose_name_plural': 'constitutionpolicies',
            },
        ),
        migrations.CreateModel(
            name='DataStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_store', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PlatformAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_post', models.CharField(max_length=300, null=True, verbose_name='community_post')),
                ('community_revert', models.BooleanField(default=False)),
                ('community_origin', models.BooleanField(default=False)),
                ('is_bundled', models.BooleanField(default=False)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community')),
                ('data', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.DataStore', verbose_name='data')),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.CommunityUser')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_policyengine.platformaction_set+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'platformaction',
                'verbose_name_plural': 'platformactions',
            },
        ),
        migrations.CreateModel(
            name='PlatformPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.TextField(blank=True, default='')),
                ('initialize', models.TextField(blank=True, default='')),
                ('check', models.TextField(blank=True, default='')),
                ('notify', models.TextField(blank=True, default='')),
                ('success', models.TextField(blank=True, default='')),
                ('fail', models.TextField(blank=True, default='')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_bundled', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community', verbose_name='community')),
                ('data', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.DataStore', verbose_name='data')),
            ],
            options={
                'verbose_name': 'platformpolicy',
                'verbose_name_plural': 'platformpolicies',
            },
        ),
        migrations.CreateModel(
            name='EditorModel',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('filter', models.TextField(blank=True, default='return True\n\n', verbose_name='Filter')),
                ('initialize', models.TextField(blank=True, default='pass\n\n', verbose_name='Initialize')),
                ('check', models.TextField(blank=True, default='return PASSED\n\n', verbose_name='Check')),
                ('notify', models.TextField(blank=True, default='pass\n\n', verbose_name='Notify')),
                ('success', models.TextField(blank=True, default='action.execute()\n\n', verbose_name='Pass')),
                ('fail', models.TextField(blank=True, default='pass\n\n', verbose_name='Fail')),
            ],
            options={
                'abstract': False,
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitAddCommunityDoc',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('name', models.TextField()),
                ('text', models.TextField()),
            ],
            options={
                'permissions': (('can_execute_policykitaddcommunitydoc', 'Can execute policykit add community doc'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='StarterKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', null=True)),
                ('platform', models.TextField(blank=True, default='', null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_policyengine.starterkit_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('proposed', 'proposed'), ('failed', 'failed'), ('passed', 'passed')], max_length=10)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.CommunityUser', verbose_name='author')),
            ],
        ),
        migrations.CreateModel(
            name='PlatformPolicyBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.TextField(blank=True, default='')),
                ('initialize', models.TextField(blank=True, default='')),
                ('check', models.TextField(blank=True, default='')),
                ('notify', models.TextField(blank=True, default='')),
                ('success', models.TextField(blank=True, default='')),
                ('fail', models.TextField(blank=True, default='')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_bundled', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('bundled_policies', models.ManyToManyField(to='policyengine.PlatformPolicy')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community', verbose_name='community')),
                ('data', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.DataStore', verbose_name='data')),
            ],
            options={
                'verbose_name': 'platformpolicybundle',
                'verbose_name_plural': 'platformpolicybundles',
            },
        ),
        migrations.CreateModel(
            name='PlatformActionBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_post', models.CharField(max_length=300, null=True, verbose_name='community_post')),
                ('is_bundled', models.BooleanField(default=False)),
                ('bundle_type', models.CharField(choices=[('election', 'election'), ('bundle', 'bundle')], max_length=10)),
                ('bundled_actions', models.ManyToManyField(to='policyengine.PlatformAction')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community', verbose_name='community')),
                ('data', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.DataStore', verbose_name='data')),
                ('proposal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Proposal')),
            ],
            options={
                'verbose_name': 'platformactionbundle',
                'verbose_name_plural': 'platformactionbundles',
            },
        ),
        migrations.AddField(
            model_name='platformaction',
            name='proposal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Proposal'),
        ),
        migrations.CreateModel(
            name='NumberVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_time', models.DateTimeField(auto_now_add=True)),
                ('number_value', models.IntegerField(null=True)),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Proposal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.CommunityUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LogAPICall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_time', models.DateTimeField(auto_now_add=True)),
                ('call_type', models.CharField(max_length=300, verbose_name='call_type')),
                ('extra_info', models.TextField()),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community')),
            ],
        ),
        migrations.CreateModel(
            name='GenericRole',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('role_name', models.TextField(blank=True, default='', null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('is_base_role', models.BooleanField(default=False)),
                ('user_group', models.TextField(blank=True, default='', null=True)),
                ('plat_perm_set', models.TextField(blank=True, default='', null=True)),
                ('starterkit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.StarterKit')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='GenericPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('filter', models.TextField(blank=True, default='', null=True)),
                ('initialize', models.TextField(blank=True, default='', null=True)),
                ('check', models.TextField(blank=True, default='', null=True)),
                ('notify', models.TextField(blank=True, default='', null=True)),
                ('success', models.TextField(blank=True, default='', null=True)),
                ('fail', models.TextField(blank=True, default='', null=True)),
                ('is_bundled', models.BooleanField(default=False)),
                ('is_constitution', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('starterkit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.StarterKit')),
            ],
        ),
        migrations.CreateModel(
            name='ConstitutionPolicyBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.TextField(blank=True, default='')),
                ('initialize', models.TextField(blank=True, default='')),
                ('check', models.TextField(blank=True, default='')),
                ('notify', models.TextField(blank=True, default='')),
                ('success', models.TextField(blank=True, default='')),
                ('fail', models.TextField(blank=True, default='')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_bundled', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('bundled_policies', models.ManyToManyField(to='policyengine.ConstitutionPolicy')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community', verbose_name='community')),
                ('data', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.DataStore', verbose_name='data')),
            ],
            options={
                'verbose_name': 'constitutionpolicybundle',
                'verbose_name_plural': 'constitutionpolicybundles',
            },
        ),
        migrations.AddField(
            model_name='constitutionpolicy',
            name='data',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.DataStore', verbose_name='data'),
        ),
        migrations.CreateModel(
            name='ConstitutionActionBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_post', models.CharField(max_length=300, null=True, verbose_name='community_post')),
                ('is_bundled', models.BooleanField(default=False)),
                ('bundle_type', models.CharField(choices=[('election', 'election'), ('bundle', 'bundle')], max_length=10)),
                ('bundled_actions', models.ManyToManyField(to='policyengine.ConstitutionAction')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community', verbose_name='community')),
                ('data', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.DataStore', verbose_name='data')),
                ('proposal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Proposal')),
            ],
            options={
                'verbose_name': 'constitutionactionbundle',
                'verbose_name_plural': 'constitutionactionbundles',
            },
        ),
        migrations.AddField(
            model_name='constitutionaction',
            name='data',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.DataStore', verbose_name='data'),
        ),
        migrations.AddField(
            model_name='constitutionaction',
            name='initiator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.CommunityUser'),
        ),
        migrations.AddField(
            model_name='constitutionaction',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_policyengine.constitutionaction_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='constitutionaction',
            name='proposal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Proposal'),
        ),
        migrations.CreateModel(
            name='CommunityRole',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('role_name', models.TextField(max_length=300, null=True, verbose_name='readable_name')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community')),
            ],
            options={
                'verbose_name': 'communityrole',
                'verbose_name_plural': 'communityroles',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='CommunityDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', null=True)),
                ('text', models.TextField(blank=True, default='', null=True)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.Community')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='base_role',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='base_community', to='policyengine.CommunityRole'),
        ),
        migrations.AddField(
            model_name='community',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_policyengine.community_set+', to='contenttypes.ContentType'),
        ),
        migrations.CreateModel(
            name='BooleanVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_time', models.DateTimeField(auto_now_add=True)),
                ('boolean_value', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, null=True)),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.Proposal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.CommunityUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PolicykitAddConstitutionPolicy',
            fields=[
                ('editormodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.EditorModel')),
            ],
            options={
                'permissions': (('can_execute_policykitaddconstitutionpolicy', 'Can execute policykit add constitution policy'),),
            },
            bases=('policyengine.editormodel',),
        ),
        migrations.CreateModel(
            name='PolicykitAddPlatformPolicy',
            fields=[
                ('editormodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.EditorModel')),
            ],
            options={
                'permissions': (('can_execute_addpolicykitplatformpolicy', 'Can execute policykit add platform policy'),),
            },
            bases=('policyengine.editormodel',),
        ),
        migrations.CreateModel(
            name='PolicykitRemoveUserRole',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.CommunityRole')),
                ('users', models.ManyToManyField(to='policyengine.CommunityUser')),
            ],
            options={
                'permissions': (('can_execute_policykitremoveuserrole', 'Can execute policykit remove user role'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitRemovePlatformPolicy',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('platform_policy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.PlatformPolicy')),
            ],
            options={
                'permissions': (('can_execute_policykitremoveplatformpolicy', 'Can execute policykit remove platform policy'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitRecoverPlatformPolicy',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('platform_policy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.PlatformPolicy')),
            ],
            options={
                'permissions': (('can_execute_policykitrecoverplatformpolicy', 'Can execute policykit recover platform policy'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitRemoveConstitutionPolicy',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('constitution_policy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.ConstitutionPolicy')),
            ],
            options={
                'permissions': (('can_execute_policykitremoveconstitutionpolicy', 'Can execute policykit remove constitution policy'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitRecoverConstitutionPolicy',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('constitution_policy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.ConstitutionPolicy')),
            ],
            options={
                'permissions': (('can_execute_policykitrecoverconstitutionpolicy', 'Can execute policykit recover constitution policy'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitEditRole',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('name', models.CharField(max_length=300, verbose_name='name')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('permissions', models.ManyToManyField(to='auth.Permission')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.CommunityRole')),
            ],
            options={
                'permissions': (('can_execute_policykiteditrole', 'Can execute policykit edit role'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitDeleteRole',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.CommunityRole')),
            ],
            options={
                'permissions': (('can_execute_policykitdeleterole', 'Can execute policykit delete role'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitDeleteCommunityDoc',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.CommunityDoc')),
            ],
            options={
                'permissions': (('can_execute_policykitdeletecommunitydoc', 'Can execute policykit delete community doc'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitRecoverCommunityDoc',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.CommunityDoc')),
            ],
            options={
                'permissions': (('can_execute_policykitrecovercommunitydoc', 'Can execute policykit recover community doc'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitChangeCommunityDoc',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('name', models.TextField()),
                ('text', models.TextField()),
                ('doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.CommunityDoc')),
            ],
            options={
                'permissions': (('can_execute_policykitchangecommunitydoc', 'Can execute policykit change community doc'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitAddUserRole',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.CommunityRole')),
                ('users', models.ManyToManyField(to='policyengine.CommunityUser')),
            ],
            options={
                'permissions': (('can_execute_policykitadduserrole', 'Can execute policykit add user role'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitAddRole',
            fields=[
                ('constitutionaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.ConstitutionAction')),
                ('name', models.CharField(max_length=300, verbose_name='name')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('permissions', models.ManyToManyField(to='auth.Permission')),
            ],
            options={
                'permissions': (('can_execute_policykitaddrole', 'Can execute policykit add role'),),
            },
            bases=('policyengine.constitutionaction',),
        ),
        migrations.CreateModel(
            name='PolicykitChangePlatformPolicy',
            fields=[
                ('editormodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.EditorModel')),
                ('platform_policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.PlatformPolicy')),
            ],
            options={
                'permissions': (('can_execute_policykitchangeplatformpolicy', 'Can execute policykit change platform policy'),),
            },
            bases=('policyengine.editormodel',),
        ),
        migrations.CreateModel(
            name='PolicykitChangeConstitutionPolicy',
            fields=[
                ('editormodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.EditorModel')),
                ('constitution_policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.ConstitutionPolicy')),
            ],
            options={
                'permissions': (('can_execute_policykitchangeconstitutionpolicy', 'Can execute policykit change constitution policy'),),
            },
            bases=('policyengine.editormodel',),
        ),
    ]
