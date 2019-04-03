from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    Custom User model.
    '''

    def __str__(self):
        return self.username
