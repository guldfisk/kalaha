
from abc import ABCMeta

class AbstractHole(object, metaclass=ABCMeta):

	def __init__(self) -> None:
		self._seeds = 0 #type: int

	@property
	def seeds(self) -> int:
		return self._seeds

	@seeds.setter
	def seeds(self, value: int) -> None:
		self._seeds = value