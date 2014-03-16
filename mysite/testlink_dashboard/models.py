# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AssignmentStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'assignment_status'

class AssignmentTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_table = models.CharField(max_length=30, blank=True) # TODO: Don't know
    description = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'assignment_types'

class Attachments(models.Model):
    id = models.IntegerField(primary_key=True)
    fk_id = models.IntegerField() # TODO: Don't know
    fk_table = models.CharField(max_length=250, blank=True) # TODO: Don't know
    title = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=250, blank=True)
    file_name = models.CharField(max_length=250)
    file_path = models.CharField(max_length=250, blank=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=250)
    date_added = models.DateTimeField()
    content = models.TextField(blank=True)
    compression_type = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'attachments'

class Builds(models.Model):
    id = models.IntegerField(primary_key=True)#models.ForeignKey('NodesHierarchy', primary_key=True, limit_choices_to={'node_type_id', 12})
    testplan = models.ForeignKey('Testplans')
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    author = models.ForeignKey('Users', blank=True, null=True)
    creation_ts = models.DateTimeField()
    release_date = models.DateField(blank=True, null=True)
    closed_on_date = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'builds'

class CfieldBuildDesignValues(models.Model):
    field = models.ForeignKey('CustomFields')
    node = models.ForeignKey('NodesHierarchy', primary_key=True)
    value = models.CharField(max_length=4000)
    class Meta:
        managed = False
        db_table = 'cfield_build_design_values'

class CfieldDesignValues(models.Model):
    field = models.ForeignKey('CustomFields')
    node = models.ForeignKey('NodesHierarchy', primary_key=True, limit_choices_to={'node_type_id', 4})
    value = models.CharField(max_length=4000)
    class Meta:
        managed = False
        db_table = 'cfield_design_values'

class CfieldExecutionValues(models.Model):
    field = models.ForeignKey('CustomFields')
    execution = models.ForeignKey('Executions', primary_key=True)
    testplan = models.ForeignKey('Testplans')
    tcversion = models.ForeignKey('Tcversions', db_column='tcversion')
    value = models.CharField(max_length=4000)
    class Meta:
        managed = False
        db_table = 'cfield_execution_values'

class CfieldNodeTypes(models.Model):
    field = models.ForeignKey('CustomFields', primary_key=True)
    node_type = models.ForeignKey('NodeTypes', db_column='node_type')
    class Meta:
        managed = False
        db_table = 'cfield_node_types'

class CfieldTestplanDesignValues(models.Model):
    field = models.ForeignKey('CustomFields')
    link_id = models.IntegerField() # TODO: Don't know
    value = models.CharField(max_length=4000)
    class Meta:
        managed = False
        db_table = 'cfield_testplan_design_values'

class CfieldTestprojects(models.Model):
    # No primary key
    field = models.ForeignKey('CustomFields')
    testproject = models.ForeignKey('Testprojects')
    display_order = models.IntegerField()
    location = models.IntegerField()
    active = models.IntegerField()
    required = models.IntegerField()
    required_on_design = models.IntegerField()
    required_on_execution = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'cfield_testprojects'

class CustomFields(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    label = models.CharField(max_length=64)
    type = models.IntegerField()
    possible_values = models.CharField(max_length=4000)
    default_value = models.CharField(max_length=4000)
    valid_regexp = models.CharField(max_length=255)
    length_min = models.IntegerField()
    length_max = models.IntegerField()
    show_on_design = models.IntegerField()
    enable_on_design = models.IntegerField()
    show_on_execution = models.IntegerField()
    enable_on_execution = models.IntegerField()
    show_on_testplan_design = models.IntegerField()
    enable_on_testplan_design = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'custom_fields'

class DbVersion(models.Model):
    version = models.CharField(primary_key=True, max_length=50)
    upgrade_ts = models.DateTimeField()
    notes = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'db_version'

class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    transaction = models.ForeignKey('Transactions')
    log_level = models.IntegerField()
    source = models.CharField(max_length=45, blank=True)
    description = models.TextField()
    fired_at = models.IntegerField()
    activity = models.CharField(max_length=45, blank=True)
    object_id = models.IntegerField(blank=True, null=True) # TODO: Don't know
    object_type = models.CharField(max_length=45, blank=True) # TODO: Don't know
    class Meta:
        managed = False
        db_table = 'events'

class ExecutionBugs(models.Model):
    execution = models.ForeignKey('Executions')
    bug_id = models.CharField(max_length=64)
    class Meta:
        managed = False
        db_table = 'execution_bugs'

class Executions(models.Model):
    id = models.IntegerField(primary_key=True)
    build = models.ForeignKey('builds')
    tester = models.ForeignKey('Users', blank=True, null=True)
    execution_ts = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True)
    testplan = models.ForeignKey('Testplans')
    tcversion = models.ForeignKey('Tcversions', related_name='+')
    tcversion_number = models.IntegerField()
    platform = models.ForeignKey('Platforms')
    execution_type = models.IntegerField()
    execution_duration = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'executions'

class Inventory(models.Model):
    id = models.IntegerField(primary_key=True)
    testproject = models.ForeignKey('Testprojects')
    owner = models.ForeignKey('Users')
    name = models.CharField(max_length=255)
    ipaddress = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    creation_ts = models.DateTimeField()
    modification_ts = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'inventory'

class Issuetrackers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    type = models.IntegerField(blank=True, null=True)
    cfg = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'issuetrackers'

class Keywords(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.CharField(max_length=100)
    testproject = models.ForeignKey('Testprojects')
    notes = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'keywords'

class Milestones(models.Model):
    id = models.IntegerField(primary_key=True)
    testplan = models.ForeignKey('Testplans')
    target_date = models.DateField(blank=True, null=True)
    start_date = models.DateField()
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    name = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'milestones'

class NodeTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'node_types'

class NodesHierarchy(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    node_type = models.ForeignKey('NodeTypes')
    node_order = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'nodes_hierarchy'

class ObjectKeywords(models.Model): # TODO: Don't know
    id = models.IntegerField(primary_key=True)
    fk_id = models.IntegerField() # TODO: Don't know
    fk_table = models.CharField(max_length=30, blank=True) # TODO: Don't know
    keyword = models.ForeignKey('Keywords')
    class Meta:
        managed = False
        db_table = 'object_keywords'

class Platforms(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    testproject = models.ForeignKey('Testprojects')
    notes = models.TextField()
    class Meta:
        managed = False
        db_table = 'platforms'

class ReqCoverage(models.Model):
    req = models.ForeignKey('Requirements', primary_key=True)
    testcase = models.ForeignKey('Tcversions')
    author = models.ForeignKey('Users', blank=True, null=True, related_name='authored_req_coverage_set')
    creation_ts = models.DateTimeField()
    review_requester = models.ForeignKey('Users', blank=True, null=True, related_name='review_requested_req_coverage_set')
    review_request_ts = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'req_coverage'

class ReqRelations(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.ForeignKey('Requirements', related_name='src_relations_set')
    destination = models.ForeignKey('Requirements',  related_name='dst_relations_set')
    relation_type = models.IntegerField()
    author = models.ForeignKey('Users', blank=True, null=True)
    creation_ts = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'req_relations'

class ReqRevisions(models.Model):
    parent =models.ForeignKey('ReqVersions')
    id = models.ForeignKey('NodesHierarchy', primary_key=True, db_column='id', limit_choices_to={'node_type_id', 10})
    revision = models.IntegerField()
    req_doc_id = models.CharField(max_length=64, blank=True)
    name = models.CharField(max_length=100, blank=True)
    scope = models.TextField(blank=True)
    status = models.CharField(max_length=1)
    type = models.CharField(max_length=1, blank=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    expected_coverage = models.IntegerField()
    log_message = models.TextField(blank=True)
    author = models.ForeignKey('Users',blank=True, null=True, related_name='+')
    creation_ts = models.DateTimeField()
    modifier = models.ForeignKey('Users', blank=True, null=True, related_name='+')
    modification_ts = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'req_revisions'

class ReqSpecs(models.Model):
    id = models.ForeignKey('NodesHierarchy', primary_key=True, db_column='id', limit_choices_to={'node_type_id', 6})
    testproject = models.ForeignKey('Testprojects')
    doc_id = models.CharField(max_length=64)
    class Meta:
        managed = False
        db_table = 'req_specs'

class ReqSpecsRevisions(models.Model):
    parent = models.ForeignKey('ReqSpecs')
    id = models.ForeignKey('NodesHierarchy', primary_key=True, db_column='id', limit_choices_to={'node_type_id', 11})
    revision = models.IntegerField()
    doc_id = models.CharField(max_length=64, blank=True)
    name = models.CharField(max_length=100, blank=True)
    scope = models.TextField(blank=True)
    total_req = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=1, blank=True)
    log_message = models.TextField(blank=True)
    author = models.ForeignKey('Users',blank=True, null=True, related_name='+')
    creation_ts = models.DateTimeField()
    modifier = models.ForeignKey('Users',blank=True, null=True, related_name='+')
    modification_ts = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'req_specs_revisions'

class ReqVersions(models.Model):
    id = models.ForeignKey('NodesHierarchy', primary_key=True, db_column='id', limit_choices_to={'node_type_id', 8})
    version = models.IntegerField()
    revision = models.IntegerField()
    scope = models.TextField(blank=True)
    status = models.CharField(max_length=1)
    type = models.CharField(max_length=1, blank=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    expected_coverage = models.IntegerField()
    author = models.ForeignKey('Users',blank=True, null=True, related_name='+')
    creation_ts = models.DateTimeField()
    modifier = models.ForeignKey('Users',blank=True, null=True, related_name='+')
    modification_ts = models.DateTimeField()
    log_message = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'req_versions'

class Reqmgrsystems(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    type = models.IntegerField(blank=True, null=True)
    cfg = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'reqmgrsystems'

class Requirements(models.Model):
    id = models.ForeignKey('NodesHierarchy', primary_key=True, db_column='id', related_name='+', limit_choices_to={'node_type_id', 7})
    srs = models.ForeignKey('NodesHierarchy', related_name='+', limit_choices_to={'node_type_id', 6})
    req_doc_id = models.CharField(max_length=64)
    class Meta:
        managed = False
        db_table = 'requirements'

class Rights(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(unique=True, max_length=100)
    class Meta:
        managed = False
        db_table = 'rights'

class RiskAssignments(models.Model):
    id = models.IntegerField(primary_key=True)
    testplan = models.ForeignKey('Testplans')
    node = models.ForeignKey('NodesHierarchy')# TODO: Don't know, maybe wrong
    risk = models.CharField(max_length=1)
    importance = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'risk_assignments'

class RoleRights(models.Model):
    role = models.ForeignKey('Roles')
    right = models.ForeignKey('Rights')
    class Meta:
        managed = False
        db_table = 'role_rights'

class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(unique=True, max_length=100)
    notes = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'roles'

class Tcsteps(models.Model):
    id = models.OneToOneField('NodesHierarchy',parent_link=True, primary_key=True, db_column='id', limit_choices_to={'node_type_id', 9})
    step_number = models.IntegerField()
    actions = models.TextField(blank=True)
    expected_results = models.TextField(blank=True)
    active = models.IntegerField()
    execution_type = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'tcsteps'

class Tcversions(models.Model):
    id = models.OneToOneField('NodesHierarchy',parent_link=True, primary_key=True, db_column='id', limit_choices_to={'node_type_id', 4})
    tc_external_id = models.IntegerField(blank=True, null=True)
    version = models.IntegerField()
    layout = models.IntegerField()
    status = models.IntegerField()
    summary = models.TextField(blank=True)
    preconditions = models.TextField(blank=True)
    importance = models.IntegerField()
    author = models.ForeignKey('Users', related_name='authored_testcase_set')
    creation_ts = models.DateTimeField()
    updater = models.ForeignKey('Users', related_name='updated_testcase_set')
    modification_ts = models.DateTimeField()
    active = models.IntegerField()
    is_open = models.IntegerField()
    execution_type = models.IntegerField()
    estimated_exec_duration = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tcversions'

class TestcaseKeywords(models.Model):
    testcase = models.ForeignKey('NodesHierarchy', primary_key=True, limit_choices_to={'node_type_id', 3})
    keyword = models.ForeignKey('Keywords')
    class Meta:
        managed = False
        db_table = 'testcase_keywords'

class TestplanPlatforms(models.Model):
    id = models.IntegerField(primary_key=True)
    testplan = models.ForeignKey('Testplans')
    platform = models.ForeignKey('Platforms')
    class Meta:
        managed = False
        db_table = 'testplan_platforms'

class TestplanTcversions(models.Model):
    id = models.IntegerField(primary_key=True)
    testplan =models.ForeignKey('Testplans')
    tcversion = models.ForeignKey('Tcversions')
    node_order = models.IntegerField()
    urgency = models.IntegerField()
    platform = models.ForeignKey('Platforms')
    author = models.ForeignKey('Users', blank=True, null=True)
    creation_ts = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'testplan_tcversions'

class Testplans(models.Model):
    id = models.ForeignKey('NodesHierarchy', primary_key=True, db_column='id', limit_choices_to={'node_type_id', 5})
    testproject = models.ForeignKey('Testprojects')
    notes = models.TextField(blank=True)
    active = models.IntegerField()
    is_open = models.IntegerField()
    is_public = models.IntegerField()
    api_key = models.CharField(unique=True, max_length=64)
    class Meta:
        managed = False
        db_table = 'testplans'

class TestprojectIssuetracker(models.Model):
    testproject = models.ForeignKey('Testprojects')
    issuetracker = models.ForeignKey('Issuetrackers')
    class Meta:
        managed = False
        db_table = 'testproject_issuetracker'

class TestprojectReqmgrsystem(models.Model):
    testproject = models.ForeignKey('Testprojects')
    reqmgrsystem = models.ForeignKey('Reqmgrsystems')
    class Meta:
        managed = False
        db_table = 'testproject_reqmgrsystem'

class Testprojects(models.Model):
    id = models.ForeignKey('NodesHierarchy', primary_key=True, db_column='id', limit_choices_to={'node_type_id', 1})
    notes = models.TextField(blank=True)
    color = models.CharField(max_length=12)
    active = models.IntegerField()
    option_reqs = models.IntegerField()
    option_priority = models.IntegerField()
    option_automation = models.IntegerField()
    options = models.TextField(blank=True)
    prefix = models.CharField(unique=True, max_length=16)
    tc_counter = models.IntegerField()
    is_public = models.IntegerField()
    issue_tracker_enabled = models.IntegerField()
    reqmgr_integration_enabled = models.IntegerField()
    api_key = models.CharField(unique=True, max_length=64)
    class Meta:
        managed = False
        db_table = 'testprojects'

class Testsuites(models.Model):
    id = models.ForeignKey('NodesHierarchy', primary_key=True, db_column='id', limit_choices_to={'node_type_id', 2})
    details = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'testsuites'

class Transactions(models.Model):
    id = models.IntegerField(primary_key=True)
    entry_point = models.CharField(max_length=45)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    user = models.ForeignKey('Users')
    session_id = models.CharField(max_length=45, blank=True)
    class Meta:
        managed = False
        db_table = 'transactions'

class UserAssignments(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    feature_id = models.IntegerField()  #TODO: Don't know
    user = models.ForeignKey('Users', blank=True, null=True, related_name='+')
    build = models.ForeignKey('Builds', blank=True, null=True)
    deadline_ts = models.DateTimeField(blank=True, null=True)
    assigner = models.ForeignKey('Users', blank=True, null=True, related_name='+')
    creation_ts = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'user_assignments'

class UserGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'user_group'

class UserGroupAssign(models.Model):
    usergroup = models.ForeignKey('UserGroup')
    user = models.ForeignKey('Users')
    class Meta:
        managed = False
        db_table = 'user_group_assign'

class UserTestplanRoles(models.Model):
    user = models.ForeignKey('Users')
    testplan = models.ForeignKey('Testplans')
    role = models.ForeignKey('Roles')
    class Meta:
        managed = False
        db_table = 'user_testplan_roles'

class UserTestprojectRoles(models.Model):
    user = models.ForeignKey('Users')
    testproject = models.ForeignKey('Testprojects')
    role = models.ForeignKey('Roles')
    class Meta:
        managed = False
        db_table = 'user_testproject_roles'

class Users(models.Model):
    id = models.ForeignKey('NodesHierarchy', primary_key=True, db_column='id', limit_choices_to={'node_type_id', 14})
    login = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=32)
    role = models.ForeignKey('Roles')
    email = models.CharField(max_length=100)
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    locale = models.CharField(max_length=10)
    default_testproject = models.ForeignKey('Testprojects')
    active = models.IntegerField()
    script_key = models.CharField(max_length=32, blank=True)
    cookie_string = models.CharField(unique=True, max_length=64)
    auth_method = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'users'

