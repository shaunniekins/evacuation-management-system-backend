from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    municipality = models.CharField(max_length=100)
    barangay = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='users/', null=True, blank=True)


class Resident(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    municipality = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    contact_num = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    civil_status = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50)
    resident_status = models.CharField(max_length=20)
    is_pwd = models.CharField(max_length=3)
    is_ip = models.CharField(max_length=3)
    is_head = models.CharField(max_length=3)
    household_num = models.CharField(max_length=15)
    # emergency_contact_num = models.CharField(
    #     max_length=15, blank=True)  # non-charField should have null=True


class Municipality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    province = models.CharField(max_length=30)


class Barangay(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    municipality = models.CharField(max_length=30)


class Evacuation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    municipality = models.CharField(max_length=30)
    barangay = models.CharField(max_length=30)
    capacity = models.IntegerField()


class ResidentInEvacuation(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    evacuation = models.ForeignKey(
        Evacuation, on_delete=models.CASCADE, blank=True)
    isHead = models.CharField(max_length=3)
    date = models.DateField()


class Calamity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    date = models.DateField()


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name} ({self.unit})"


class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=12, decimal_places=1)


class InventoryPerBarangay(models.Model):
    item = models.IntegerField()
    unit = models.CharField(max_length=5)
    qty = models.DecimalField(max_digits=12, decimal_places=1)
    barangay = models.IntegerField()


class DistributionBarangay(models.Model):
    item = models.IntegerField()
    unit = models.CharField(max_length=5)
    qty = models.DecimalField(max_digits=12, decimal_places=1)
    barangay = models.IntegerField()
    date = models.DateField()


class StockedIn(models.Model):
    givenBy = models.CharField(max_length=50)
    donor = models.CharField(max_length=50, blank=True)
    dateReceived = models.DateField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=12, decimal_places=1)


# class RepackedList(models.Model):
#     items = models.TextField()
#     qty = models.TextField()
#     reason = models.TextField()


class Repacked(models.Model):
    # items = models.ForeignKey(RepackedList, on_delete=models.CASCADE)
    items = models.TextField()
    units = models.TextField()
    qty = models.TextField()
    instance = models.IntegerField()
    reason = models.TextField()
    barangay = models.CharField(max_length=30)


class Distributed(models.Model):
    id = models.AutoField(primary_key=True)
    repackedItem = models.IntegerField()
    calamity = models.CharField(max_length=30)
    calamityDate = models.DateField()
    dateDistributed = models.DateField()
    evacuee = models.CharField(max_length=50)
    headFamily = models.CharField(max_length=3)
    is_distributed = models.IntegerField(default=0)


class CashDonation(models.Model):
    id = models.AutoField(primary_key=True)
    controlNumber = models.CharField(max_length=20)
    givenBy = models.CharField(max_length=50)
    donor = models.CharField(max_length=50, blank=True)
    amount = models.IntegerField()
    modeOfTransfer = models.CharField(max_length=20)
    date = models.DateField()
