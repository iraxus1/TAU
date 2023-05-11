import pytest

class GameBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    def place_start_and_stop(self, start_row, start_col, stop_row, stop_col):
        self.board[start_row][start_col] = 'A'
        self.board[stop_row][stop_col] = 'B'
    
    def place_obstacles(self, obstacles):
        for obstacle in obstacles:
            row, col = obstacle
            self.board[row][col] = 'X'
    
    def is_valid_move(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        if self.board[row][col] == 'X':
            return False
        return True
    
    def print_board(self):
        for row in self.board:
            print(' '.join(row))

def find_path(board, current_row, current_col, path):
    if not board.is_valid_move(current_row, current_col):
        return False
    
    if board.board[current_row][current_col] == 'B':
        return True
    
    if board.board[current_row][current_col] == ' ':
        board.board[current_row][current_col] = '.'
        
        if find_path(board, current_row-1, current_col, path):
            path.append((current_row-1, current_col))
            return True
        if find_path(board, current_row+1, current_col, path):
            path.append((current_row+1, current_col))
            return True
        if find_path(board, current_row, current_col-1, path):
            path.append((current_row, current_col-1))
            return True
        if find_path(board, current_row, current_col+1, path):
            path.append((current_row, current_col+1))
            return True
        
        board.board[current_row][current_col] = ' '
    
    return False

@pytest.fixture
def game_board():
    board = GameBoard(5, 5)
    board.place_start_and_stop(0, 0, 4, 4)
    board.place_obstacles([(1, 1), (2, 2), (3, 3)])
    return board

class TestGame:
    @pytest.mark.parametrize('row, col', [
        (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (0, 2)
    ])
    def test_valid_move(self, game_board, row, col):
        assert game_board.is_valid_move(row, col)
    
    @pytest.mark.parametrize('row, col', [
        (-1, 0), (0, -1), (5, 0), (0, 5)
    ])
    def test_invalid_move(self, game_board, row, col):
        assert not game_board.is_valid_move(row, col)
    
    def test_find_path(self, game_board):
        path = [(0, 0)]
        assert find_path(game_board, 0, 0, path)
        assert path[-1] == (4, 4)
    
    @pytest.mark.xfail
    def test_impossible_path(self, game_board):
        path = [(0, 0)]
        assert not find_path(game_board, 0, 0, path)
    
    @pytest.mark.skip(reason="Not implemented")
    def test_custom_marker(self):
        assert False
    
    @pytest.mark.skipif(pytest.__version__ < "6.0", reason="Requires PyTest 6.0+")
    def test_pytest_version(self):
        assert True

