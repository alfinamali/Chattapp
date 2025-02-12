from django.utils.translation import gettext_lazy as _
from django.db import models


class RoomType(models.TextChoices):
    GROUP = "G", _("Group")  # For group messages (multiple users can send messages)
    DIRECT = "D", _("Direct Room")  # For direct messages between two users


ROOM_TYPE_CHOICES = dict(RoomType.choices)
