from django.conf import settings
from django_cognito_jwt import JSONWebTokenAuthentication
from django_cognito_jwt.validator import TokenValidator

from .models import CustomerUser


class CustomerAuthentification(JSONWebTokenAuthentication):
    def get_user_model(self):
        return CustomerUser

    def get_token_validator(self, request):
        return TokenValidator(
            settings.AWS_REGION,
            settings.COGNITO_CUSTOMER_USER_POOL_ID,
            settings.COGNITO_CUSTOMER_APP_CLIENT_ID,
        )
