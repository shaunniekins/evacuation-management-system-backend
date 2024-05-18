from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import CustomUser, Resident, Municipality, Barangay, Evacuation, ResidentInEvacuation, Calamity, Item, Inventory, InventoryPerBarangay, DistributionBarangay, StockedIn, Repacked, Distributed, CashDonation

admin.site.register(CustomUser)

models_list = [Resident, Municipality, Barangay, Evacuation, ResidentInEvacuation, Calamity,
               Item, Inventory, InventoryPerBarangay, DistributionBarangay, StockedIn, Repacked, Distributed, CashDonation]
admin.site.register(models_list)
