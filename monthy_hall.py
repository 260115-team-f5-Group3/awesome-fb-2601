import os, sys, warnings

gparent = os.path.join(os.pardir)
sys.path.append(gparent)

import numpy as np
import matplotlib.pyplot as plt

def monty_hall(n : int):
    """
    Input: 반복 횟수 int값
    Return: 예상 승률 
    """
    keep_count = [] # 이기는 횟수
    change_count = [] # 문이 열리거나 닫힐 때 추가로 이기는 횟수
    P_keep = [] # 게임 이후 승률 
    P_change = [] # 문 상태에 따른승률 변화 
    
    for i in range(n):
        doors = [1, 2, 3] # 문 3개
        car_door = np.random.choice(range(1,4))
        player_door = np.random.choice(range(1,4))
        # 염소의 문
        goat_doors = [door for door in doors if\
                      door != car_door and door != player_door]
        # Monty가 찾는 염소의 문
        revealed_door = np.random.choice(goat_doors)
        # 문 상태가 바뀐 문
        changed_door = [door for door in doors if\
                        door != player_door and door != revealed_door]
        
        if player_door == car_door:
            keep_count.append(1)
        else:                        
            keep_count.append(0)
        if changed_door == car_door: 
            change_count.append(1)
        else:                        
            change_count.append(0)
        
        P_k_i = np.mean(keep_count[:i]) # 이전까지 승률
        P_keep.append(P_k_i)
        P_c_i = np.mean(change_count[:i]) # 게임 반복 후 변화 승률
        P_change.append(P_c_i)
        print(P_change)
    


if __name__ == "__main__":
    monty_hall(100000)
