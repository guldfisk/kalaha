import typing as t


from kalaha.interface import IoInterface
from kalaha.game.game import Game
from kalaha.game.board import Board
from kalaha.game.player import Player
from kalaha.game.turns import TurnOrder

class DummyInterface(IoInterface):

	def choose_move(self, player: Player, options: t.List[int], turn_order: TurnOrder) -> int:

		option_map = {
			option if player!=turn_order.first_player else 5-option: option
			for option in options
		}

		print('{}: choose options: {}'.format(player, option_map.keys()))

		while True:
			ind = input(': ')
			if not ind:
				return options[0]
			_ind = int(ind)
			if _ind in option_map:
				return option_map[_ind]

	def show_board(self, board: Board, active_player: Player, turn_order: TurnOrder) -> None:
		print(
			board.show(
				active_player == turn_order.first_player
			)
		)

	def end_game(self, winner: t.List[Player]) -> None:
		print(winner, 'wins!')


def test():
	interface = DummyInterface()
	game = Game(interface)
	game.play()


if __name__ == '__main__':
	test()