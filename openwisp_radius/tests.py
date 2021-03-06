import os
from unittest import skipUnless

import swapper
from django.contrib.auth import get_user_model
from django.test import TestCase
from django_freeradius.tests import FileMixin
from django_freeradius.tests.base.test_admin import BaseTestAdmin
from django_freeradius.tests.base.test_api import BaseTestApi, BaseTestApiReject
from django_freeradius.tests.base.test_batch_add_users import BaseTestCSVUpload
from django_freeradius.tests.base.test_commands import BaseTestCommands
from django_freeradius.tests.base.test_models import (BaseTestNas, BaseTestRadiusAccounting,
                                                      BaseTestRadiusBatch, BaseTestRadiusCheck,
                                                      BaseTestRadiusGroupCheck, BaseTestRadiusGroupReply,
                                                      BaseTestRadiusPostAuth, BaseTestRadiusProfile,
                                                      BaseTestRadiusReply, BaseTestRadiusUserGroup,
                                                      BaseTestRadiusUserProfile)
from django_freeradius.tests.base.test_utils import BaseTestUtils

from openwisp_users.models import Organization
from openwisp_users.tests.test_admin import TestUsersAdmin

from .mixins import ApiParamsMixin, CallCommandMixin, CreateRadiusObjectsMixin
from .models import *

_SUPERUSER = {'username': 'gino', 'password': 'cic', 'email': 'giggi_vv@gmail.it'}
_RADCHECK_ENTRY = {'username': 'Monica', 'value': 'Cam0_liX',
                   'attribute': 'NT-Password'}
_RADCHECK_ENTRY_PW_UPDATE = {'username': 'Monica', 'new_value': 'Cam0_liX',
                             'attribute': 'NT-Password'}


class TestNas(BaseTestNas, TestCase, CreateRadiusObjectsMixin):
    nas_model = Nas


class TestRadiusAccounting(BaseTestRadiusAccounting, TestCase, CreateRadiusObjectsMixin):
    radius_accounting_model = RadiusAccounting


class TestRadiusCheck(BaseTestRadiusCheck, TestCase, CreateRadiusObjectsMixin):
    radius_check_model = RadiusCheck


class TestRadiusReply(BaseTestRadiusReply, TestCase, CreateRadiusObjectsMixin):
    radius_reply_model = RadiusReply


class TestRadiusGroupReply(BaseTestRadiusGroupReply, TestCase, CreateRadiusObjectsMixin):
    radius_groupreply_model = RadiusGroupReply


class TestRadiusGroupCheck(BaseTestRadiusGroupCheck, TestCase, CreateRadiusObjectsMixin):
    radius_groupcheck_model = RadiusGroupCheck


class TestRadiusUserGroup(BaseTestRadiusUserGroup, TestCase, CreateRadiusObjectsMixin):
    radius_usergroup_model = RadiusUserGroup


class TestRadiusPostAuth(BaseTestRadiusPostAuth, TestCase, CreateRadiusObjectsMixin):
    radius_postauth_model = RadiusPostAuth


class TestRadiusBatch(BaseTestRadiusBatch, TestCase, CreateRadiusObjectsMixin):
    radius_batch_model = RadiusBatch


class TestRadiusProfile(BaseTestRadiusProfile, TestCase, CreateRadiusObjectsMixin):
    radius_profile_model = RadiusProfile


class TestRadiusUserProfile(BaseTestRadiusUserProfile, TestCase, CreateRadiusObjectsMixin):
    radius_profile_model = RadiusProfile
    radius_userprofile_model = RadiusUserProfile
    radius_check_model = RadiusCheck


class TestAdmin(BaseTestAdmin, TestCase, CreateRadiusObjectsMixin,
                FileMixin, CallCommandMixin):
    app_name = "openwisp_radius"
    nas_model = Nas
    radius_accounting_model = RadiusAccounting
    radius_batch_model = RadiusBatch
    radius_check_model = RadiusCheck
    radius_groupcheck_model = RadiusGroupCheck
    radius_groupreply_model = RadiusGroupReply
    radius_postauth_model = RadiusPostAuth
    radius_reply_model = RadiusReply
    radius_usergroup_model = RadiusUserGroup
    radius_profile_model = RadiusProfile

    def setUp(self):
        self._create_org()
        super(TestAdmin, self).setUp()

    def _get_csv_post_data(self):
        data = super(TestAdmin, self)._get_csv_post_data()
        org = Organization.objects.first()
        data['organization'] = org.pk
        return data

    def _get_prefix_post_data(self):
        data = super(TestAdmin, self)._get_prefix_post_data()
        org = Organization.objects.first()
        data['organization'] = org.pk
        return data


class TestApi(BaseTestApi, TestCase, CreateRadiusObjectsMixin, ApiParamsMixin):
    radius_postauth_model = RadiusPostAuth
    radius_accounting_model = RadiusAccounting
    radius_batch_model = RadiusBatch
    user_model = get_user_model()

    def setUp(self):
        self._create_org()


class TestApiReject(BaseTestApiReject, TestCase, CreateRadiusObjectsMixin):
    pass


class TestCommands(BaseTestCommands, TestCase, CreateRadiusObjectsMixin,
                   FileMixin, CallCommandMixin):
    radius_accounting_model = RadiusAccounting
    radius_batch_model = RadiusBatch
    radius_postauth_model = RadiusPostAuth


class TestCSVUpload(BaseTestCSVUpload, TestCase,
                    CreateRadiusObjectsMixin, FileMixin):
    radius_batch_model = RadiusBatch


class TestUtils(BaseTestUtils, TestCase, CreateRadiusObjectsMixin, FileMixin):
    pass


class TestUsersIntegration(TestUsersAdmin):
    pass
