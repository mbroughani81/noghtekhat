from noghtekhat.game.game import EMPTYCELL_STR, FULLCELL_STR, GameVerdict, Noghtekhat


def cal_point(noghtekhat_game: Noghtekhat, type: str, row: int, col: int):
    point = 0
    if type == "hor":
        if row < noghtekhat_game.row_num - 1 and \
            noghtekhat_game.table_hor[row][col] == FULLCELL_STR and noghtekhat_game.table_hor[row + 1][col] == FULLCELL_STR and \
            noghtekhat_game.table_ver[row][col] == FULLCELL_STR and noghtekhat_game.table_ver[row][col + 1]:
            point += 1
        if row > 0 and \
            noghtekhat_game.table_hor[row][col] == FULLCELL_STR and noghtekhat_game.table_hor[row - 1][col] == FULLCELL_STR and \
            noghtekhat_game.table_ver[row - 1][col] == FULLCELL_STR and noghtekhat_game.table_ver[row - 1][col + 1]:
            point += 1
    else:
        if col < noghtekhat_game.col_num - 1 and \
            noghtekhat_game.table_hor[row][col] == FULLCELL_STR and noghtekhat_game.table_hor[row + 1][col] == FULLCELL_STR and \
            noghtekhat_game.table_ver[row][col] == FULLCELL_STR and noghtekhat_game.table_ver[row][col + 1]:
            point += 1
        if col > 0 and \
            noghtekhat_game.table_hor[row][col - 1] == FULLCELL_STR and noghtekhat_game.table_hor[row + 1][col - 1] == FULLCELL_STR and \
            noghtekhat_game.table_ver[row][col] == FULLCELL_STR and noghtekhat_game.table_ver[row][col - 1]:
            point += 1
    return point

def check_winner(noghtekhat_game: Noghtekhat):
    # finished when all lines are filled
    # if finished, check the points
    for row in noghtekhat_game.table_hor:
        if row.count(EMPTYCELL_STR) > 0:
            return GameVerdict.RUNNIG
    for row in noghtekhat_game.table_ver:
        if row.count(EMPTYCELL_STR) > 0:
            return GameVerdict.RUNNIG
    
    # find winner
    if noghtekhat_game.first_point > noghtekhat_game.second_point:
        return GameVerdict.FIRST_WON
    if noghtekhat_game.second_point > noghtekhat_game.first_point:
        return GameVerdict.SECOND_WON
    return GameVerdict.DRAW
