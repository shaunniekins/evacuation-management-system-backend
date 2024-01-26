from rest_framework import fields, serializers
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from backend.models import Resident, Municipality, Barangay, Evacuation, ResidentInEvacuation, Calamity, Item, Inventory, InventoryPerBarangay, DistributionBarangay, StockedIn, Repacked, Distributed, CashDonation

# from rest_framework import serializers
from backend.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True, required=False,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])]
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'is_superuser', 'username', 'first_name', 'last_name',
                  'email', 'is_staff', 'municipality', 'barangay', 'position', 'contact_number', 'image')


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ('id',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'municipality',
                  'barangay',
                  'contact_num',
                  'gender',
                  'birthday',
                  'civil_status',
                  'occupation',
                  'resident_status',
                  'is_pwd',
                  'is_ip',
                  'is_head',
                  'household_num')


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ('id', 'name', 'province')


class BarangaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Barangay
        fields = ('id', 'name', 'municipality')


class EvacuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evacuation
        fields = ('id', 'name', 'municipality', 'barangay', 'capacity')


class ResidentInEvacuationSerializer(serializers.ModelSerializer):
    resident = serializers.PrimaryKeyRelatedField(
        queryset=Resident.objects.all())
    evacuation = serializers.PrimaryKeyRelatedField(
        queryset=Evacuation.objects.all(), allow_null=True,  required=False)

    class Meta:
        model = ResidentInEvacuation
        fields = ('id', 'resident', 'evacuation', 'isHead', 'date')


class CalamitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Calamity
        fields = ('id', 'name', 'date')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'unit')


class InventorySerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    unit = serializers.SerializerMethodField()

    class Meta:
        model = Inventory
        fields = ('id', 'item', 'unit', 'qty')

    def get_unit(self, obj):
        return obj.item.unit


class InventoryPerBarangaySerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryPerBarangay
        fields = ('id', 'item', 'unit', 'qty', 'barangay')


class DistributionBarangaySerializer(serializers.ModelSerializer):

    class Meta:
        model = DistributionBarangay
        fields = ('id', 'item', 'unit', 'qty', 'barangay', 'date')


class StockedInSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    unit = serializers.SerializerMethodField()

    class Meta:
        model = StockedIn
        fields = ('id', 'givenBy', 'donor', 'dateReceived',
                  'item', 'unit', 'qty')

    def get_unit(self, obj):
        return obj.item.unit


# class RepackedListSerializerList(serializers.ModelSerializer):
#     class Meta:
#         model = RepackedList
#         fields = ('id', 'items', 'qty', 'reason')

    # def get_unit(self, obj):
    #     return obj.items.qty


class RepackedSerializer(serializers.ModelSerializer):
    # items = serializers.PrimaryKeyRelatedField(
    #     queryset=RepackedList.objects.all())
    # qty = serializers.SerializerMethodField()

    # class Meta:
    #     model = Repacked
    #     fields = ('id', 'items', 'qty', 'instance')

    # def get_qty(self, obj):
    #     return obj.items.qty
    class Meta:
        model = Repacked
        fields = ('id', 'items', 'units', 'qty',
                  'instance', 'reason', 'barangay')


class DistributeReliefGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributed
        fields = ('id', 'repackedItem', 'calamity', 'calamityDate',
                  'dateDistributed', 'evacuee', 'headFamily', 'is_distributed')


class CashDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashDonation
        fields = ('id', 'controlNumber', 'givenBy', 'donor',
                  'amount', 'modeOfTransfer', 'date')
