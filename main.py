import phonenumbers
from phonenumbers import carrier , geocoder , timezone

number = input("Enter the phone number : ")
phoneNumber = phonenumbers.parse(number)
timeZone = timezone.time_zones_for_number(phoneNumber)
Carrier = carrier.name_for_number(phoneNumber, 'en')
Region = geocoder.description_for_number(phoneNumber, 'en')

print('Timezone : ', timeZone)
print('Carrier : ', Carrier)
print('Region : ', Region)
