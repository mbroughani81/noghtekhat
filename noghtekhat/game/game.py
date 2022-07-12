import enum

EMPTYCELL_STR = "."
FULLCELL_STR = "x"

class Turn(enum.Enum):
    FIRST = "first"
    SECOND = "second"


class GameVerdict(enum.Enum):
    RUNNIG = 1
    FIRST_WON = 2
    SECOND_WON = 3
    DRAW = 4


class NotCurrentTurn(Exception):
    pass


class InvalidMove(Exception):
    pass


class Noghtekhat:
    def __init__(self, row_num, col_num):
        self.row_num = row_num
        self.col_num = col_num
        self.turn = Turn.FIRST
        self.table_hor = [[EMPTYCELL_STR for _i in range(self.col_num - 1)] for _t in range(self.row_num)]
        self.table_ver = [[EMPTYCELL_STR for _i in range(self.col_num)] for _t in range(self.row_num - 1)]
        self.first_point = 0
        self.second_point = 0
    
    def move(self, player: Turn, type: str, row: int, col: int):
        row = row - 1
        col = col - 1
        if player != self.turn:
            raise NotCurrentTurn
        if type == "hor":
            if self.table_hor[row][col] == FULLCELL_STR:
                raise InvalidMove("line already filled!")
            self.table_hor[row][col] = FULLCELL_STR
        else:
            if self.table_ver[row][col] == FULLCELL_STR:
                raise InvalidMove("line already filled!")
            self.table_ver[row][col] = FULLCELL_STR
        
        from game.logic import cal_point
        point = cal_point(self, type, row, col)
        if point == 0:
            if self.turn == Turn.FIRST:
                self.first_point += point

                self.turn = Turn.SECOND
            else:
                self.second_point += point
                self.turn = Turn.FIRST
        
        from game.logic import check_winner
        game_verdict = check_winner(self)
        if game_verdict != GameVerdict.RUNNIG:
            return f"it is player {self.turn.value}'s turn to play!"
        else:
            if game_verdict == GameVerdict.FIRST_WON:
                return "first player won!"
            if game_verdict == GameVerdict.SECOND_WON:
                return "second player won!"
            if game_verdict == GameVerdict.DRAW:
                return "draw!"        
