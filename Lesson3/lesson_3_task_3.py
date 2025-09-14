from address import Address
from mailing import Mailing

to_address = Address("123456", "Нижний Новгород", "Чаадаева", "10", "25")
from_address = Address("654321", "Североморск", "Северная Застава", "6", "10")

mail = Mailing(to_address, from_address, 500, "ABC123")

print(
    f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, "
    f"{mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)
