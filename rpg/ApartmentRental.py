from .Rental import Rental
from .Apartment import Apartment
from .Property import get_valid_input

class ApartmentRental(Rental, Apartment):
	def prompt_init():
		init = Apartment.prompt_init()
		init.update(Rental.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)
	