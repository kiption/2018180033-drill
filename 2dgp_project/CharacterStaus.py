from enum import Enum

class state(Enum):
    Mario_Idle = 0
    Mario_Move = 1
    Mario_Jump = 2
    Mario_Attaked = 3
    Mario_Die = 4
    Mario_landing = 5

class state_block(Enum):
    S_Idle = 0
    S_Hiting =1
    S_Brocking = 2
    S_Broken = 3
    S_Hited = 4

class Mario_state(Enum):
    mario =0
    Super_mario =1
    Fire_mario = 2