from backend.models import Resident, Evacuation, Barangay, Municipality


def get_evacuee_count():
    return Resident.objects.count()


def get_family_count():
    return Resident.objects.filter(is_head='YES').count()


def get_male_count():
    return Resident.objects.filter(gender='MALE').count()


def get_female_count():
    return Resident.objects.filter(gender='FEMALE').count()


def get_family_count():
    return Resident.objects.filter(is_head='YES').count()


def get_evacuation_center_count():
    return Evacuation.objects.count()


def get_barangay_count():
    return Barangay.objects.count()


def get_barangay_items():
    return Barangay.objects.values_list('name', flat=True)


def get_municipality_items():
    return Municipality.objects.values_list('name', flat=True)
