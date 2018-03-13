import typing as t

from abc import ABCMeta, abstractmethod

from itertools import chain

from kalaha.utils.ring import Ring

from kalaha.game.hole import AbstractHole
from kalaha.game.player import Player
from kalaha.game.turns import Turn, TurnOrder
from kalaha.game.board import Board
from kalaha.interface import IoInterface


class Hole(AbstractHole):

	def __init__(self) -> None:
		super().__init__()
		self.opposite = None #type: Hole


class House(AbstractHole):
	pass


class Game(object):

	def __init__(self, interface: IoInterface) -> None:
		self._interface = interface

		_hole_types = (Hole,)*6+(House,)

		_holess = [
			[hole_type() for hole_type in _hole_types]
			for _ in range(2)
		]

		for i in range(6):
			_holess[0][i].opposite = _holess[1][i]
			_holess[1][i].opposite = _holess[0][i]

		self._turn_order = TurnOrder(
			(
				Player('player 1', _holess[0]),
				Player('player 2', _holess[1]),
			)
		)

		self._board = Board(
			Ring(
				chain(*_holess)
			)
		)

		for hole in self._board.holes.all:
			if isinstance(hole, Hole):
				hole.seeds = 6

	def end_game(self) -> None:
		players = {
			player: player.score()
			for player in
			self._turn_order.players
		}
		max_score = max(players.values())
		winners = [player for player, score in players.items() if score == max_score]
		self._interface.end_game(winners)

	def make_move(self, player: Player, hole: AbstractHole):
		seeds = hole.seeds
		hole.seeds = 0

		holes = self._board.holes.loop_after(hole)
		_hole = None #type: AbstractHole

		while seeds > 0:
			_hole = next(holes)
			if isinstance(_hole, Hole) or player.house==_hole:
				_hole.seeds += 1
				seeds -= 1

		if _hole == player.house:
			self._turn_order.add_extra_turn(Turn(player))
			# pass
		elif _hole.seeds == 1 and _hole in player.non_house_holes:
			player.collect(_hole)
			player.collect(_hole.opposite)
		else:
			# self.make_move(player, _hole)
			pass
		return

	def take_turn(self, player: Player) -> bool:
		self._interface.show_board(self._board, player, self._turn_order)
		options = [
			index
			for index, hole in
			enumerate(player.non_house_holes)
			if hole.seeds > 0
		]

		if not options:
			self.end_game()
			return True

		option = self._interface.choose_move(player, options, self._turn_order)
		self.make_move(player, player.non_house_holes[option])
		return False

	def play(self):
		while True:
			if self.take_turn(self._turn_order.next().player):
				break