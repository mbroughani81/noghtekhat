from game.game import FULLCELL_STR, InvalidMove, Noghtekhat, NotCurrentTurn, Turn

class Cli:
    def __init__(self):
        pass

    def start(self):
        r = int(input("enter number of rows: "))
        c = int(input("enter number of cols: "))
        self.game = Noghtekhat(r, c)
        while True:
            turn = input("enter if it is player first or second move : ")
            move_type = input("enter move type. 'hor' or 'ver': ")
            row = int(input("enter row: "))
            col = int(input("enter col: "))
            
            turn = Turn.FIRST if turn == "first" else Turn.SECOND
            move_type = "hor" if move_type == "hor" else "ver"
            try:
                self.game.move(turn, move_type, row, col)
                print(">>OK")
            except NotCurrentTurn:
                print(f">>This is not {turn.value} turn!")
            except InvalidMove as e:
                print(">>" + repr(e))
            
            for row in self.game.table_hor:
                print(row)
            print("*" * 10)
            for row in self.game.table_ver:
                print(row)
            print("first player point : " + str(self.game.first_point))
            print("second player point : " + str(self.game.second_point))
            print("-" * 10)
