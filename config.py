CHAT_SIZE = 14
INDEX_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'w', 'y', 'z', 'v', 't', 's', 'r', 'q', 'n', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b','a']
YB = 'X'
PLAYER = '@'
EMPTY = ' '
PICK_N_LARGEST = 4
EvalUnit = 4
AGRESSIVE = 0.6
MATCH_YB_CONTINUE_DRESS = YB + '+'
MATCH_PLAYER_CONTINUE_DRESS = PLAYER + '+'

#about regex
''' 
#XXX__ __平均为 **2.5
#XXX_# _衰减 / unit
#XX_ _ _ left _ down to /unit
#XX__# left _ 衰减为/unit
#XX_#  _ down to /unit
#XX_X# _ down to / (unit)
'''
