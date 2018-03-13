import typing as t

from kalaha.utils.ring import Ring

from kalaha.game.hole import AbstractHole


class Board(object):

	def __init__(self, holes: Ring[AbstractHole]) -> None:
		self._holes = holes

	@property
	def holes(self) -> Ring[AbstractHole]:
		return self._holes

	def __str__(self) -> str:
		return (
			'''
  {0} | {1} | {2} | {3} | {4} | {5}  
{13}                           {6}
  {12} | {11} | {10} | {9} | {8} | {7}  
			'''
		).format(
			*[
				str(hole.seeds).zfill(2)
				for hole in
				self.holes.all
			]
		)

	def show(self, top_active: bool = True):
		return (
			'''
{14}{0} | {1} | {2} | {3} | {4} | {5}  
{13}                           {6}
{15}{12} | {11} | {10} | {9} | {8} | {7}  
			'''
		).format(
			*[
				str(hole.seeds).zfill(2)
				for hole in
				self.holes.all
			]+[
				'->' if not top_active else '  ',
				'->' if top_active else '  ',
			]
		)