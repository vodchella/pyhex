from pkg.ai.pathfinders import Node, to_nodes
from pkg.constants.game import PLAYER_ONE, PLAYER_TWO, PLAYER_NONE
from pkg.models.board import Board


def build_path(to_node: Node):
    path = []
    while to_node is not None:
        path.append((to_node.x(), to_node.y()))
        to_node = to_node.get_previous()
    return path


class BasicPathfinder:
    _board: Board = None
    _walk_only_by_own_cells: bool = False

    def __init__(self, board, walk_only_by_own_cells=False):
        if type(self) == BasicPathfinder:
            raise Exception('Can\'t instantiate BasicPathfinder')
        self._board = board
        self._walk_only_by_own_cells = walk_only_by_own_cells

    def choose_node(self, nodes, dst_node: Node):
        return nodes[0]

    def find_path(self, for_player, src_x, src_y, dst_x, dst_y):
        board = self._board
        dst_node = Node(dst_x, dst_y)
        opponent = PLAYER_ONE if for_player == PLAYER_TWO else PLAYER_TWO
        exclude_players = [opponent, PLAYER_NONE] if self._walk_only_by_own_cells else [opponent]
        reachable = [Node(src_x, src_y)]
        explored = []

        while len(reachable) > 0:
            node = self.choose_node(reachable, dst_node)
            if node == dst_node:
                return build_path(node)

            reachable.remove(node)
            explored.append(node)

            cells = board.get_cell_neighbors(node.x(), node.y(), exclude_players=exclude_players)
            new_reachable = [n for n in filter(lambda n: n not in explored, to_nodes(cells))]

            next_cost = node.get_cost() + 1
            for adjacent in new_reachable:
                if adjacent not in reachable:
                    reachable.append(adjacent)

                if next_cost < adjacent.get_cost():
                    adjacent.set_previous(node)
                    adjacent.set_cost(next_cost)

        return []
