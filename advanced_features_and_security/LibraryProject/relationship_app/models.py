from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Author(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name
  

class Book(models.Model):
  title = models.CharField(max_length=30)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

  class Meta:
    permissions = [
      ("can_add_book", "Can add book"),
      ("can_change_book", "Can change book"),
      ("can_delete_book", "Can delete book"),
    ]

  def __str__(self):
    return (f"{self.title} by {self.author.name}")
  

class Library(models.Model):
  name = models.CharField(max_length=30)
  books= models.ManyToManyField(Book)

  def __str__(self):
    return (self.name)
  

class Librarian(models.Model):
  name = models.CharField(max_length=20)
  library = models.OneToOneField(Library, on_delete=models.CASCADE)

  def __str__(self):
    return (f"{self.name} at {self.library.name}")
  
  
class UserProfile(models.Model):

  ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
  ]

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

  def __str__(self):
    return(f'{self.user.username}' - {self.role})
  
  
@receiver (post_save, sender=User)
def create_user_profile (sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)

@receiver (post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.userprofile.save()


class CustomUserManager(BaseUserManager):
  def create_user(self, date_of_birth, profile_photo, password=None):
    user = self.model(date_of_birth=date_of_birth, profile_photo=profile_photo)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, date_of_birth, profile_photo, password=None):
    user = self.model(date_of_birth=date_of_birth, profile_photo=profile_photo)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  
class CustomUser (AbstractUser):
  date_of_birth = models.DateField()
  profile_photo = models.ImageField()

  objects = CustomUserManager()