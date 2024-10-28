from address import Address
from mailing import Mailing


address_to = Address("123456", "Москва", "Тверская", "1", "1")
address_from = Address("654321", "Санкт-Петербург", "Невский", "2", "2")


mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=150,
    track="TRACK123",  # noqa: E501
)


print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."  # noqa: E501
)
