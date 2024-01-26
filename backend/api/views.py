from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.views import APIView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.views.decorators.csrf import csrf_exempt
from django.db import models

from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAdminUser

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
# from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
# from rest_framework.response import Response

from backend.models import Resident, Municipality, Barangay, Evacuation, ResidentInEvacuation, Calamity, Item, Inventory, InventoryPerBarangay, DistributionBarangay, StockedIn, Repacked, Distributed, CashDonation

from backend.api.serializers import ResidentSerializer, MunicipalitySerializer, BarangaySerializer, EvacuationSerializer, ResidentInEvacuationSerializer, CalamitySerializer, ItemSerializer, InventorySerializer, InventoryPerBarangaySerializer, DistributionBarangaySerializer, StockedInSerializer, RepackedSerializer, DistributeReliefGoodsSerializer, CashDonationSerializer

from .evacuees import get_evacuee_count, get_family_count, get_male_count, get_female_count, get_family_count, get_evacuation_center_count, get_barangay_count, get_barangay_items, get_municipality_items


from rest_framework import generics
from backend.models import CustomUser
from backend.api.serializers import CustomUserSerializer


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         # ...

#         return token


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


# @api_view(['GET', 'POST'])
# def getRoutes(request):
#     routes = [
#         'api/token',
#         'api/token/refresh'
#     ]
#     return Response(routes)


class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    parser_classes = [MultiPartParser, FileUploadParser]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            custom_user = self.get_object(pk)
            serializer = CustomUserSerializer(custom_user)
            return Response(serializer.data)
        else:
            custom_users = CustomUser.objects.all()
            serializer = CustomUserSerializer(custom_users, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        custom_user = self.get_object(pk)
        serializer = CustomUserSerializer(
            custom_user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        custom_user = self.get_object(pk)
        custom_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ResidentAPI(request, pk=0):
    if request.method == 'GET':
        evacuees = Resident.objects.all()
        evacuees_serializer = ResidentSerializer(evacuees, many=True)
        return Response(evacuees_serializer.data)

    elif request.method == 'POST':
        evacuees_serializer = ResidentSerializer(data=request.data)
        if evacuees_serializer.is_valid():
            evacuees_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(evacuees_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            evacuees = Resident.objects.get(id=pk)
        except Resident.DoesNotExist:
            return Response("Resident Not Found", status=status.HTTP_404_NOT_FOUND)

        evacuees_serializer = ResidentSerializer(
            evacuees, data=request.data)
        if evacuees_serializer.is_valid():
            evacuees_serializer.save()
            return Response("Updated Successfully")
        return Response(evacuees_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            evacuees = Resident.objects.get(id=pk)
        except Resident.DoesNotExist:
            return Response("Resident Not Found", status=status.HTTP_404_NOT_FOUND)

        evacuees.delete()
        return Response("Resident Info Deleted Successfully")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def MunicipalityAPI(request, pk=0):
    if request.method == 'GET':
        municipality = Municipality.objects.all()
        municipality_serializer = MunicipalitySerializer(
            municipality, many=True)
        return Response(municipality_serializer.data)

    elif request.method == 'POST':
        municipality_serializer = MunicipalitySerializer(data=request.data)
        if municipality_serializer.is_valid():
            municipality_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(municipality_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            municipality = Municipality.objects.get(id=pk)
        except Municipality.DoesNotExist:
            return Response("Municipality Not Found", status=status.HTTP_404_NOT_FOUND)

        municipality_serializer = MunicipalitySerializer(
            municipality, data=request.data)
        if municipality_serializer.is_valid():
            municipality_serializer.save()
            return Response("Updated Successfully")
        return Response(municipality_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            municipality = Municipality.objects.get(id=pk)
            # calamity.delete()
        except Municipality.DoesNotExist:
            return Response("Municipality Not Found", status=status.HTTP_404_NOT_FOUND)

        municipality.delete()
        return Response(municipality_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def BarangayAPI(request, pk=0):
    if request.method == 'GET':
        barangay = Barangay.objects.all()
        barangay_serializer = BarangaySerializer(
            barangay, many=True)
        return Response(barangay_serializer.data)

    elif request.method == 'POST':
        barangay_serializer = BarangaySerializer(data=request.data)
        if barangay_serializer.is_valid():
            barangay_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(barangay_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            barangay = Barangay.objects.get(id=pk)
        except Barangay.DoesNotExist:
            return Response("Barangay Not Found", status=status.HTTP_404_NOT_FOUND)

        barangay_serializer = BarangaySerializer(
            barangay, data=request.data)
        if barangay_serializer.is_valid():
            barangay_serializer.save()
            return Response("Updated Successfully")
        return Response(barangay_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            barangay = Barangay.objects.get(id=pk)
            # calamity.delete()
        except Barangay.DoesNotExist:
            return Response("Barangay Not Found", status=status.HTTP_404_NOT_FOUND)

        barangay.delete()
        return Response(barangay_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def EvacuationAPI(request, pk=0):
    if request.method == 'GET':
        evacuation = Evacuation.objects.all()
        evacuation_serializer = EvacuationSerializer(evacuation, many=True)
        return Response(evacuation_serializer.data)

    elif request.method == 'POST':
        evacuation_serializer = EvacuationSerializer(data=request.data)
        if evacuation_serializer.is_valid():
            evacuation_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(evacuation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            evacuation = Evacuation.objects.get(id=pk)
        except Evacuation.DoesNotExist:
            return Response("Evacuation Not Found", status=status.HTTP_404_NOT_FOUND)

        evacuation_serializer = EvacuationSerializer(
            evacuation, data=request.data)
        if evacuation_serializer.is_valid():
            evacuation_serializer.save()
            return Response("Updated Successfully")
        return Response(evacuation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            evacuation = Evacuation.objects.get(id=pk)
            # calamity.delete()
        except Evacuation.DoesNotExist:
            return Response("Evacuation Not Found", status=status.HTTP_404_NOT_FOUND)

        evacuation.delete()
        return Response(evacuation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ResidentInEvacuationAPI(request, pk=0):
    queryset = ResidentInEvacuation.objects.all()
    # should be an instance of the serializer class
    serializer_class = ResidentInEvacuationSerializer

    if request.method == 'GET':
        items = ResidentInEvacuation.objects.all()
        item_serializer = ResidentInEvacuationSerializer(items, many=True)
        return Response(item_serializer.data)

    elif request.method == 'POST':
        item_serializer = ResidentInEvacuationSerializer(data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            item = ResidentInEvacuation.objects.get(id=pk)
        except ResidentInEvacuation.DoesNotExist:
            return Response("Item Not Found", status=status.HTTP_404_NOT_FOUND)

        item_serializer = ResidentInEvacuationSerializer(
            item, data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response("Updated Successfully")
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            item = ResidentInEvacuation.objects.get(id=pk)
            # calamity.delete()
        except ResidentInEvacuation.DoesNotExist:
            return Response("Item Not Found", status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response("Stocked in Item Deleted Successfully")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CalamityAPI(request, pk=0):
    if request.method == 'GET':
        calamity = Calamity.objects.all()
        calamity_serializer = CalamitySerializer(calamity, many=True)
        return Response(calamity_serializer.data)

    elif request.method == 'POST':
        calamity_serializer = CalamitySerializer(data=request.data)
        if calamity_serializer.is_valid():
            calamity_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(calamity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            calamity = Calamity.objects.get(id=pk)
        except Calamity.DoesNotExist:
            return Response("Calamity Not Found", status=status.HTTP_404_NOT_FOUND)

        calamity_serializer = CalamitySerializer(calamity, data=request.data)
        if calamity_serializer.is_valid():
            calamity_serializer.save()
            return Response("Updated Successfully")
        return Response(calamity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            calamity = Calamity.objects.get(id=pk)
            # calamity.delete()
        except Calamity.DoesNotExist:
            return Response("Calamity Not Found", status=status.HTTP_404_NOT_FOUND)

        calamity.delete()
        return Response(calamity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ItemList(APIView):
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ItemList(request, pk=0):
    if request.method == 'GET':
        item = Item.objects.all()
        item_serializer = ItemSerializer(
            item, many=True)
        return Response(item_serializer.data)

    elif request.method == 'POST':
        item_serializer = ItemSerializer(data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            item = Item.objects.get(id=pk)
        except Item.DoesNotExist:
            return Response("Item Not Found", status=status.HTTP_404_NOT_FOUND)

        item_serializer = ItemSerializer(
            item, data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response("Updated Successfully")
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            item = Item.objects.get(id=pk)
        except Item.DoesNotExist:
            return Response("Item Not Found", status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response("Item Deleted Successfully")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def InventoryList(request, pk=0):
    if request.method == 'GET':
        inventory = Inventory.objects.all()
        inventory_serializer = InventorySerializer(
            inventory, many=True)
        return Response(inventory_serializer.data)

    elif request.method == 'POST':
        inventory_serializer = InventorySerializer(
            data=request.data)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(inventory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            inventory = Inventory.objects.get(id=pk)
        except Inventory.DoesNotExist:
            return Response("Stocked-in Item Not Found", status=status.HTTP_404_NOT_FOUND)

        inventory_serializer = InventorySerializer(
            inventory, data=request.data)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return Response("Updated Successfully")
        return Response(inventory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            inventory = Inventory.objects.get(id=pk)
        except Inventory.DoesNotExist:
            return Response("Stocked In Item Not Found", status=status.HTTP_404_NOT_FOUND)

        inventory.delete()
        return Response("Stocked in Item Deleted Successfully")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def InventoryPerBarangayAPI(request, pk=0):
    if request.method == 'GET':
        item = InventoryPerBarangay.objects.all()
        item_serializer = InventoryPerBarangaySerializer(
            item, many=True)
        return Response(item_serializer.data)

    elif request.method == 'POST':
        item_serializer = InventoryPerBarangaySerializer(data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            item = InventoryPerBarangay.objects.get(id=pk)
        except InventoryPerBarangay.DoesNotExist:
            return Response("Item Not Found", status=status.HTTP_404_NOT_FOUND)

        item_serializer = InventoryPerBarangaySerializer(
            item, data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response("Updated Successfully")
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            item = InventoryPerBarangay.objects.get(id=pk)
        except InventoryPerBarangay.DoesNotExist:
            return Response("Item Not Found", status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response("Item Deleted Successfully")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def DistributeBarangayAPI(request, pk=0):
    if request.method == 'GET':
        item = DistributionBarangay.objects.all()
        item_serializer = DistributionBarangaySerializer(
            item, many=True)
        return Response(item_serializer.data)

    elif request.method == 'POST':
        item_serializer = DistributionBarangaySerializer(data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            item = DistributionBarangay.objects.get(id=pk)
        except DistributionBarangay.DoesNotExist:
            return Response("Item Not Found", status=status.HTTP_404_NOT_FOUND)

        item_serializer = DistributionBarangaySerializer(
            item, data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response("Updated Successfully")
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            item = DistributionBarangay.objects.get(id=pk)
        except DistributionBarangay.DoesNotExist:
            return Response("Item Not Found", status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response("Item Deleted Successfully")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def StockedInAPI(request, pk=0):
    if request.method == 'GET':
        stockedin = StockedIn.objects.all()
        stockedin_serializer = StockedInSerializer(
            stockedin, many=True)
        return Response(stockedin_serializer.data)

    elif request.method == 'POST':
        stockedin_serializer = StockedInSerializer(
            data=request.data)
        if stockedin_serializer.is_valid():
            stockedin_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(stockedin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            stockedin = StockedIn.objects.get(id=pk)
        except StockedIn.DoesNotExist:
            return Response("Stocked-in Item Not Found", status=status.HTTP_404_NOT_FOUND)

        stockedin_serializer = StockedInSerializer(
            stockedin, data=request.data)
        if stockedin_serializer.is_valid():
            stockedin_serializer.save()
            return Response("Updated Successfully")
        return Response(stockedin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            stockedin = StockedIn.objects.get(id=pk)
        except StockedIn.DoesNotExist:
            return Response("Stocked In Item Not Found", status=status.HTTP_404_NOT_FOUND)

        stockedin.delete()
        return Response("Stocked in Item Deleted Successfully")


# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def RepackedListAPI(request, pk=0):
#     if request.method == 'GET':
#         repacked = Repacked.objects.all()
#         repacked_serializer = RepackedSerializer(
#             repacked, many=True)
#         return Response(repacked_serializer.data)

#     elif request.method == 'POST':
#         repacked_serializer = RepackedSerializer(data=request.data)
#         if repacked_serializer.is_valid():
#             repacked_serializer.save()
#             return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
#         return Response(repacked_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'PUT':
#         try:
#             repacked = Repacked.objects.get(id=pk)
#         except Repacked.DoesNotExist:
#             return Response("Repacked Item Not Found", status=status.HTTP_404_NOT_FOUND)

#         repacked_serializer = RepackedSerializer(
#             repacked, data=request.data)
#         if repacked_serializer.is_valid():
#             repacked_serializer.save()
#             return Response("Updated Successfully")
#         return Response(repacked_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         try:
#             repacked = Repacked.objects.get(id=pk)
#         except Repacked.DoesNotExist:
#             return Response("Repacked Item Not Found", status=status.HTTP_404_NOT_FOUND)

#         repacked.delete()
#         return Response("Repacked Item Deleted Successfully")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def RepackedAPI(request, pk=0):
    if request.method == 'GET':
        repacked = Repacked.objects.all()
        repacked_serializer = RepackedSerializer(
            repacked, many=True)
        return Response(repacked_serializer.data)

    elif request.method == 'POST':
        repacked_serializer = RepackedSerializer(data=request.data)
        if repacked_serializer.is_valid():
            repacked_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(repacked_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            repacked = Repacked.objects.get(id=pk)
        except Repacked.DoesNotExist:
            return Response("Repacked Item Not Found", status=status.HTTP_404_NOT_FOUND)

        repacked_serializer = RepackedSerializer(
            repacked, data=request.data)
        if repacked_serializer.is_valid():
            repacked_serializer.save()
            return Response("Updated Successfully")
        return Response(repacked_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            repacked = Repacked.objects.get(id=pk)
        except Repacked.DoesNotExist:
            return Response("Repacked Item Not Found", status=status.HTTP_404_NOT_FOUND)

        repacked.delete()
        return Response("Repacked Item Deleted Successfully")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def DistributedAPI(request, pk=0):
    if request.method == 'GET':
        distributed = Distributed.objects.all()
        distributed_serializer = DistributeReliefGoodsSerializer(
            distributed, many=True)
        return Response(distributed_serializer.data)

    elif request.method == 'POST':
        distributed_serializer = DistributeReliefGoodsSerializer(
            data=request.data)
        if distributed_serializer.is_valid():
            distributed_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(distributed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            distributed = Distributed.objects.get(id=pk)
        except Distributed.DoesNotExist:
            return Response("Item Not Found", status=status.HTTP_404_NOT_FOUND)

        distributed_serializer = DistributeReliefGoodsSerializer(
            distributed, data=request.data)
        if distributed_serializer.is_valid():
            distributed_serializer.save()
            return Response("Updated Successfully")
        return Response(distributed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            distributed = Distributed.objects.get(id=pk)
        except Distributed.DoesNotExist:
            return Response("Distributed Item Not Found", status=status.HTTP_404_NOT_FOUND)

        distributed.delete()
        return Response("Distributed Item Deleted Successfully")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CashDonationAPI(request, pk=0):
    if request.method == 'GET':
        cash_donate = CashDonation.objects.all()
        cash_donate_serializer = CashDonationSerializer(cash_donate, many=True)
        return Response(cash_donate_serializer.data)

    elif request.method == 'POST':
        cash_donate_serializer = CashDonationSerializer(data=request.data)
        if cash_donate_serializer.is_valid():
            cash_donate_serializer.save()
            return Response("Data Added Successfully", status=status.HTTP_201_CREATED)
        return Response(cash_donate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            cash_donate = CashDonation.objects.get(id=pk)
        except CashDonation.DoesNotExist:
            return Response("Cash Donation Item Not Found", status=status.HTTP_404_NOT_FOUND)

        cash_donate_serializer = CashDonationSerializer(
            cash_donate, data=request.data)
        if cash_donate_serializer.is_valid():
            cash_donate_serializer.save()
            return Response("Updated Successfully")
        return Response(cash_donate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            cash_donate = CashDonation.objects.get(id=pk)
        except CashDonation.DoesNotExist:
            return Response("Cash Item Not Found", status=status.HTTP_404_NOT_FOUND)

        cash_donate.delete()
        return Response("Cash Item Deleted Successfully")


@api_view(['GET'])
def evacuee_count(request):
    count = get_evacuee_count()
    data = {'evacuee_count': count}
    return Response(data)


@api_view(['GET'])
def family_count(request):
    count = get_family_count()
    data = {'family_count': count}
    return Response(data)


@api_view(['GET'])
def male_count(request):
    count = get_male_count()
    data = {'male_count': count}
    return Response(data)


@api_view(['GET'])
def female_count(request):
    count = get_female_count()
    data = {'female_count': count}
    return Response(data)


@api_view(['GET'])
def family_count(request):
    count = get_family_count()
    data = {'family_count': count}
    return Response(data)


# @api_view(['GET'])
# def evacuation_center_count(request):
#     count = get_evacuation_center_count()
#     data = {'evacuation_center_count': count}
#     return Response(data)

@api_view(['GET'])
def evacuation_center_count(request):
    count = get_evacuation_center_count()
    data = {'evacuation_center_count': count}
    return Response(data)


@api_view(['GET'])
def barangay_count(request):
    count = get_barangay_count()
    data = {'barangay_count': count}
    return Response(data)


@api_view(['GET'])
def barangay_items(request):
    item = get_barangay_items()
    data = {'barangay_item': item}
    return Response(data)


@api_view(['GET'])
def municipality_items(request):
    item = get_municipality_items()
    data = {'municipality_item': item}
    return Response(data)
