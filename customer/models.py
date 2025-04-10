from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pic/Customer/", null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)

    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


class Claims(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="claims")
    policy_number = models.CharField(max_length=50)
    claim_reason = models.TextField()
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    supporting_document = models.ImageField(upload_to="claims/", blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")],
        default="Pending"
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Claim {self.policy_number} - {self.status}"
