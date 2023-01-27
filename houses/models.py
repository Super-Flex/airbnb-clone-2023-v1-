from django.db import models

# Create your models here.


class House(models.Model):

    """Model definition for houses"""

    """DB Table"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(
        default=True,
        help_text="Does this house allow pets?",
        verbose_name="펫 가능?",
    )

    """Print"""

    def __str__(self) -> str:
        return self.name
