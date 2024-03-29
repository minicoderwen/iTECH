import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iTECH.settings')

import django
django.setup()
from authentication.models import UserProfile
from django.contrib.auth.models import User




def populate():
    # delete all users
    User.objects.all().delete()
    # delete all user profiles
    UserProfile.objects.all().delete()

    # create superuser
    User.objects.create_superuser(username='group15', password='group15')

    # create users
    user1 = User(username="user1", email="user1@student.gla.ac.uk")
    user1.set_password("user1")
    user1.save()
    user_profile1 = UserProfile(user=user1)
    user_profile1.save()
    user2 = User(username="user2", email="user2@student.gla.ac.uk")
    user2.set_password("user2")
    user2.save()
    user_profile2 = UserProfile(user=user2)
    user_profile2.save()
    user3 = User(username="user3", email="user3@student.gla.ac.uk")
    user3.set_password("user3")
    user3.save()
    user_profile3 = UserProfile(user=user3)
    user_profile3.save()

    user4 = User(username="user4", email="user4@student.gla.ac.uk")
    user4.set_password("user4")
    user4.save()
    user_profile4 = UserProfile(user=user4)
    user_profile4.save()


    # set user1, user2, user3 as staff
    user1.is_staff = True
    user1.save()
    user2.is_staff = True
    user2.save()
    user3.is_staff = True
    user3.save()

if __name__ == '__main__':
    print("populating authentication...")
    populate()
    print("populating complete")

