from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_witj_email_successful(self):
        """Creating a new user with email is successfull"""
        email = 'test@mail.com'
        password = 'qwerty123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """New user email is normalized"""
        email = 'test@MAIL.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='qwerty123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """User with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='qwerty123'
            )

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@mail.com',
            password='qwerty123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
