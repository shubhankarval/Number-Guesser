'''
Copyright (c) 2022, Shubhankar Valimbe
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

'''

import random
import math

# returns a random integer between given range
def generateRandomInt(a,b):
    return random.randint(a,b)

# returns number of guesses provided
def numGuess(a,b):
    diff = b-a
    return max(1, math.floor(math.log(diff,2)-1))

# to increase difficulty of the game, reduce no. of guesses provided

