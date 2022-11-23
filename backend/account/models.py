from django.db import models
from django_extensions.db.models import TimeStampedModel
from rest_framework.exceptions import AuthenticationFailed
import uuid


class UserManager(models.Manager):
    def get_or_create_for_cognito(self, payload):
        try:
            return self.get(cognito_uuid=payload["cognito:username"])
        except self.model.DoesNotExist:
            return self.create(
                cognito_uuid=payload["cognito:username"],
                email=payload["email"],
            )


class CustomerUser(TimeStampedModel):
    objects = UserManager()

    class Statuses(models.TextChoices):
        ACTIVE = "ACTIVE"
        DISABLED = "DISABLED"
        INVITED = "INVITED"

    status = models.CharField(max_length=16, choices=Statuses.choices, default="ACTIVE")
    cognito_uuid = models.CharField(max_length=64, db_index=True)
    email = models.EmailField(unique=True)
    balance = models.DecimalField(max_digits=19, decimal_places=2, default=100.00)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.email
