from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='game',password="usaib",email='usaib@usaib.com')        
      
    def test_profiles(self):
        user = User.objects.get(username='game')
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.image.url, "/media/default.jpg")

class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="habib",password="usaib",email='usaib@usaib.com')        
      
    def test_users(self):
        user = User.objects.get(username="habib")
    
        self.assertEqual(user.username, "habib")
     
       