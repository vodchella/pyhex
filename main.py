from pkg.ai.pathfinders.chain import ChainPathfinder
from pkg.constants.game import PLAYER_ONE, PLAYER_VIRTUAL
from pkg.models.board import Board
from pkg.views.console_board_view import ConsoleBoardView

if __name__ == '__main__':
    board = Board(7, 7)

    board.set_cell(1, 4, PLAYER_ONE)
    board.set_cell(1, 5, PLAYER_ONE)
    board.set_cell(1, 6, PLAYER_ONE)
    board.set_cell(2, 6, PLAYER_ONE)
    board.set_cell(3, 6, PLAYER_ONE)

    board.set_cell(5, 3, PLAYER_ONE)
    board.set_cell(6, 2, PLAYER_ONE)
    board.set_cell(6, 1, PLAYER_ONE)
    board.set_cell(5, 1, PLAYER_ONE)
    board.set_cell(3, 1, PLAYER_ONE)
    board.set_cell(2, 1, PLAYER_ONE)
    board.set_cell(1, 2, PLAYER_ONE)

    pf = ChainPathfinder(board)
    path = pf.find_path(PLAYER_ONE, 5, 5, 0, 3)
    board.set_cells(path, PLAYER_VIRTUAL)

    c_view = ConsoleBoardView(board)
    c_view.render()

    if not path:
        print('Path not found')
    else:
        print(f'Path length: {len(path)}')
