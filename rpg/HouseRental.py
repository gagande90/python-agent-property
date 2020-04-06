from .Rental import Rental
from .House import House
from .Property import get_valid_input

class HouseRental(Rental, House):
	def prompt_init():
		init = House.prompt_init()
		init.update(Rental.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)