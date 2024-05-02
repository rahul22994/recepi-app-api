from django.contrib.auth import get_user_model
from django.test import TestCase

class TestModels(TestCase):
    
    def test_user_model_success(self):
        email = 'abc@example.com'
        password = 'pass1234'
        user = get_user_model().objects.create_user(email,password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        emails_list = [['hello@Example.com','hello@example.com'],['Test@EXAMPLE.COM','Test@example.com']]
        for email, expected_email in emails_list:
            user = get_user_model().objects.create_user(email,'pass123')
            self.assertEqual(user.email,expected_email)

    def test_validate_email_for_valueError(self):
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user('','pass_word_is_123')

    
    def test_superuser_creation_functionality(self):
        """Testing super user functionality"""        
        user = get_user_model().objects.create_superuser('superuser@example.com','super123')
        self.assertTrue(user.is_superuser)        

    
        