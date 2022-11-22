import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager as DjangoUserManager
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

# from notifications.tasks import send_email
# from api.utils import random_selected_model


from django.conf import settings


class UserManager(DjangoUserManager):
    def get_by_natural_key(self, username):
        return self.get(**{f'{self.model.USERNAME_FIELD}__iexact': username})


def upload_to_profile_pic(instance, filename):
    return f'uploads/profile/{uuid.uuid4()}/{filename}'


class User(AbstractBaseUser, PermissionsMixin):
    class UserGenderChoices(models.TextChoices):
        MALE = 'male', "Male"
        FEMALE = 'female', "Female"
        PREFERE_NOT_TO_ANSWER = 'prefer_not_to_answer', "Prefere not to answer"

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=50,
        unique=True,
        help_text=_('Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("This username already exists."),
        },
    )
    display_name = models.CharField(max_length=150)
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(blank=True, null=True, upload_to=upload_to_profile_pic)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    email_verification_code = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=25, choices=UserGenderChoices.choices, blank=True, null=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_deactivated = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_online = models.DateTimeField(_('last online'), blank=True, null=True)
    is_set_password = models.BooleanField(default=True)
    # This field is for Social users that didn't edit their profile, mainly Apple Users for now.
    is_new_user = models.BooleanField(default=False)

    last_active = models.DateTimeField(auto_now=True)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.display_name

    def get_short_name(self):
        """Return the short name for the user."""
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @cached_property
    def token(self):
        return RefreshToken.for_user(self)

    def send_email_verification(self, force_new_code=False):
        if force_new_code or self.email_verification_code is None:
            self.email_verification_code = get_random_string(6, '0123456789')
            self.save()

        context = {
            'display_name': self.display_name,
            'verification_code': self.email_verification_code
        }
        body = render_to_string('users/email_verification.html', context)
        send_mail(
            subject='Please confirm your email',
            body=body,
            email=self.email,
            fail_silently=False,
        )







