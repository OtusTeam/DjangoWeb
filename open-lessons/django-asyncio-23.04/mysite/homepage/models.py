from django.dispatch import receiver
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        default="",
        db_default="",
    )
    bio = models.TextField(
        null=False,
        blank=True,
        default="",
        db_default="",
    )

    class FamilyStatus(models.TextChoices):
        SINGLE = "S", "Single"
        IN_A_RELATIONSHIP = "R", "In A Relationship"
        MARRIED = "M", "Married"
        DIVORCED = "D", "Divorced"
        WIDOWED = "W", "Widowed"

    family_status = models.CharField(
        max_length=1,
        choices=FamilyStatus,
        default=None,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
