import typing as t

from abc import ABCMeta, abstractmethod

from kalaha.game.board import Board
from kalaha.game.player import Player
from kalaha.game.turns import TurnOrder

class IoInterface(object, metaclass=ABCMeta):

	@abstractmethod
	def choose_move(self, player: Player, options: t.List[int], turn_order: TurnOrder) -> int:
		pass

	@abstractmethod
	def show_board(self, board: Board, active_player: Player, turn_order: TurnOrder) -> None:
		pass

	@abstractmethod
	def end_game(self, winners: t.List[Player]) -> None:
		pass