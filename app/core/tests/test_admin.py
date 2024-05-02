from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from core.models import User
from django.urls import reverse


class TestAdminSite(TestCase):

    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(email='admin@super.com', password='admin@123')
        self.client = Client()
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email='test@example.com', password='test@123')
        

    def test_cheange_list(self):
       url = reverse('admin:core_user_changelist')
       res = self.client.get(url)
       self.assertEqual(res.status_code,200)
       self.assertContains(res,self.user.email)
       self.assertContains(res,self.user.password)
       



