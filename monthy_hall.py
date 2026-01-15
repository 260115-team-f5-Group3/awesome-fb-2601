import os, sys, warnings

# setting project path
gparent = os.path.join(os.pardir)
sys.path.append(gparent)

import numpy as np
import matplotlib.pyplot as plt

def monty_hall(n : int):
    """
    Input: An integer n specifying the number of games to be simulated.
    
    Return: The simulated probabilities of winning for each strategy
            after n games, and a graph of the simulated probabilities 
            of winning for each strategy over n games.
    """
    keep_count = [] # count of simutated wins if door is kept
    change_count = [] # count of simulated wins if door is changed
    P_keep = [] # proportion of keep wins after each game 
    P_change = [] # proportion of a change wins after each game
    
    for i in range(n):
        doors = [1, 2, 3] # door labels
        car_door = np.random.choice(range(1,4)) # set car door
        player_door = np.random.choice(range(1,4)) # set player door
        # set goats doors given car door and player door
        goat_doors = [door for door in doors if\
                      door != car_door and door != player_door]
        # set the door Monty reveals given the goat doors
        revealed_door = np.random.choice(goat_doors)
        # set the change door given the player door and the revealed door
        changed_door = [door for door in doors if\
                        door != player_door and door != revealed_door]
        
        if player_door == car_door:  # keep wins
            keep_count.append(1)
        else:                        # keep losses
            keep_count.append(0)
        if changed_door == car_door: # change wins
            change_count.append(1)
        else:                        # change losses
            change_count.append(0)
        
        P_k_i = np.mean(keep_count[:i]) # proportion of keep wins in i games
        P_keep.append(P_k_i)
        P_c_i = np.mean(change_count[:i]) # proportion of change wins i games
        P_change.append(P_c_i)
        print(P_change)
    # graphing the results



monty_hall(100000)