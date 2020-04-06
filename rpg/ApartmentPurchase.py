from .Purchase import Purchase
from .Apartment import Apartment
from .Property import get_valid_input

class ApartmentPurchase(Purchase, Apartment):
	def prompt_init():
		init = Apartment.prompt_init()
		init.update(Purchase.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)