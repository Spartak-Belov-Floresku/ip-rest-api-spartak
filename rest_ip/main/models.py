from django.db import models

class CIDR(models.Model):
    AVAILABLE = 0
    ACQUIRED = 1
    STATUSES=(
        (AVAILABLE, "Available"),
        (ACQUIRED, "Acquired"),
    )
    address = models.CharField(max_length = 12)
    status = models.IntegerField(choices=STATUSES, default=AVAILABLE)

    lists = models.Manager()