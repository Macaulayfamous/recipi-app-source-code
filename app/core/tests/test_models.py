
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_succecfull(self):
        """creating user with email instead of username"""

        email = "owhedofamous@gmail.com"
        password = 'beejaymac'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        email = "test@BEEJAYMAC.COM"
        user = get_user_model().objects.create_user(email, 'beejaymac')

        self.assertEqual(user.email, email.lower())
    def test_new_user_invalid_email(self):
         """test creating user with no email will raise and error"""
         with self.assertRaises(ValueError):
             get_user_model().objects.create_user(None,'beejaymac')
    def test_create_new_superuser(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'beejaymac@gmail', 'beejaymac'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
         