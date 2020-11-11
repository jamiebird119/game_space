from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save

from django.dispatch import receiver


# Taken from CI Ecommerce project - edited
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(upload_to="profile_images", blank=True)
    default_full_name = models.CharField(
        max_length=50, blank=True, default="", null=True)
    default_email = models.EmailField(
        max_length=254, blank=True, null=True, default="")
    default_phone_number = models.CharField(
        max_length=20, blank=True, null=True, default="")
    default_country = CountryField(
        blank_label="Country", null=True, blank=True, default="")
    default_postcode = models.CharField(
        max_length=20, blank=True, null=True, default="")
    default_town_or_city = models.CharField(
        max_length=40, blank=True, null=True, default="")
    default_street_address1 = models.CharField(
        max_length=80, blank=True, null=True, default="")
    default_street_address2 = models.CharField(
        max_length=80, blank=True, null=True, default="")
    default_county = models.CharField(
        max_length=80, null=True, blank=True, default="")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
