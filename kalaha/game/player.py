import typing as t

from kalaha.game.hole import AbstractHole


class Player(object):

	def __init__(self, name: str, holes: t.List[AbstractHole]) -> None:
		super().__init__()
		self._name = name
		self._holes = holes #type: t.List[AbstractHole]

	@property
	def name(self) -> str:
		return self._name

	@property
	def holes(self) -> t.List[AbstractHole]:
		return self._holes

	@property
	def house(self) -> AbstractHole:
		return self._holes[-1]

	@property
	def non_house_holes(self) -> t.List[AbstractHole]:
		return self._holes[:-1]

	def collect(self, hole: AbstractHole) -> None:
		self.house.seeds += hole.seeds
		hole.seeds = 0

	def score(self) -> int:
		return sum(hole.seeds for hole in self.holes)

	def __repr__(self) -> str:
		return self._name

