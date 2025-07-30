from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79123456789"),
    Smartphone("Samsung", "Galaxy S23", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79345678901"),
    Smartphone("Google", "Pixel 7", "+79456789012"),
    Smartphone("OnePlus", "11 Pro", "+79567890123")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")