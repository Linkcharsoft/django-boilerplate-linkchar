from django.utils import timezone
from datetime import datetime

def get_today():
    return timezone.make_aware(datetime.now(), timezone.get_default_timezone())