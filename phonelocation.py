import phonenumbers
from phonenumbers import geocoder

c_name = phonenumbers.parse('+918511064485', "CH")
print(geocoder.description_for_number(c_name, "en"))

from phonenumbers import carrier

service_provider = phonenumbers.parse('+918511064485', "RO")
print(carrier.name_for_number(service_provider,"en"))