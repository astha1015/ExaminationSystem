from django.test import TestCase
from django.contrib.auth.models import User
from django.db import models


from django.apps import apps
from django.contrib.auth import authenticate, signals
from django.contrib.auth.models import User
from django.core.exceptions import FieldDoesNotExist
from django.test import TestCase, override_settings
from django.test.client import RequestFactory



@override_settings(ROOT_URLCONF='login.urls')
class SignalTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.u1 = User.objects.create_user(username='testclient', password='password')
        cls.u3 = User.objects.create_user(username='staff', password='password')

    def listener_login(self, user, **kwargs):
        self.logged_in.append(user)

    def listener_logout(self, user, **kwargs):
        self.logged_out.append(user)

    def listener_login_failed(self, sender, **kwargs):
        self.login_failed.append(kwargs)

    def setUp(self):
        """Set up the listeners and reset the logged in/logged out counters"""
        self.logged_in = []
        self.logged_out = []
        self.login_failed = []
        signals.user_logged_in.connect(self.listener_login)
        signals.user_logged_out.connect(self.listener_logout)
        signals.user_login_failed.connect(self.listener_login_failed)

    def tearDown(self):
        """Disconnect the listeners"""
        signals.user_logged_in.disconnect(self.listener_login)
        signals.user_logged_out.disconnect(self.listener_logout)
        signals.user_login_failed.disconnect(self.listener_login_failed)

    def test_login(self):
        # Only a successful login will trigger the success signal.
        self.client.login(username='testclient', password='bad')
        self.assertEqual(len(self.logged_in), 0)
        self.assertEqual(len(self.login_failed), 1)
        self.assertEqual(self.login_failed[0]['credentials']['username'], 'testclient')
        # verify the password is cleansed
        self.assertIn('***', self.login_failed[0]['credentials']['password'])
        self.assertIn('request', self.login_failed[0])

        # Like this:
        self.client.login(username='testclient', password='password')
        self.assertEqual(len(self.logged_in), 1)
        self.assertEqual(self.logged_in[0].username, 'testclient')

        # Ensure there were no more failures.
        self.assertEqual(len(self.login_failed), 1)

    def test_update_last_login(self):
        """Only `last_login` is updated in `update_last_login`"""
        user = self.u3
        old_last_login = user.last_login

        user.username = "This username shouldn't get saved"
        request = RequestFactory().get('/login')
        signals.user_logged_in.send(sender=user.__class__, request=request, user=user)
        user = User.objects.get(pk=user.pk)
        self.assertEqual(user.username, 'staff')
        self.assertNotEqual(user.last_login, old_last_login)

    def test_failed_login_without_request(self):
        authenticate(username='testclient', password='bad')
        self.assertIsNone(self.login_failed[0]['request'])

    def test_login_with_custom_user_without_last_login_field(self):
        """
        The user_logged_in signal is only registered if the user model has a
        last_login field.
        """
        last_login_receivers = signals.user_logged_in.receivers
        try:
            signals.user_logged_in.receivers = []
           # with self.assertRaises(FieldDoesNotExist):
           #    Profile.get_field('last_login')

            with self.settings(AUTH_USER_MODEL='user.Profile'):
                apps.get_app_config('auth').ready()
            self.assertEqual(signals.user_logged_in.receivers, [])

            # last_login is a property whose value is None.
            #self.assertIsNone(Profile).user_logged_in
            with self.settings(AUTH_USER_MODEL='Profile.user_logged_in'):
                apps.get_app_config('user').ready()
            self.assertEqual(signals.user_logged_in.receivers, [])

            with self.settings(AUTH_USER_MODEL='Profile.user_logged_in'):
                apps.get_app_config('user').ready()
            #self.assertEqual(len(signals.user_logged_in.receivers), 1)
        finally:
            signals.user_logged_in.receivers = last_login_receivers
   