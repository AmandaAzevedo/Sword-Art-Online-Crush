#
#  The location to insert your code is clearly marked -- it begins on line 32.
#
from SimpleGraphics import *
from random import randrange, shuffle
from time import time, sleep
from math import sin, pi
from copy import deepcopy
from pprint import pprint
import tkinter as tk
import inspect
import sys
import traceback
import os

# Where is the 'hole' for the game board in the background image?
HOFF = 200
VOFF = 100

# Where should the score, target and turn counter boxes be centered?
SCORE_X = 700
SCORE_Y = 300

# Special game pieces
EMPTY = -1
BURST = 6

# Game state
RUNNING = 0
WIN = 1
LOSE = -1

###############################################################################
#
#  Only modify the file below this point
#
###############################################################################

#
#  Insert your implementation of createBoard here
#
def createBoard(nLinhas,nColunas,nOpcoes):
  lista = [[] for i in range(nLinhas)]
  for i in range(len(lista)):
    lista[i] = [ randrange(nOpcoes)for x in range(nColunas)]
  return lista
#
#  Modify the board by swapping two pieces.
#
#  Parameters:
#    board: The game board to modify by swapping the pieces
#    r1, c1: The row and column of the first piece involved in the swap
#    r2, c2: The row and column of the second piece to swap
#
#  Returns: None -- the game board passed as a parameter is modified
#
def swap(board, r1, c1, r2, c2):
  swap = board[r1][c1]
  board[r1][c1] = board[r2][c2]
  board[r2][c2] = swap

#
#  Modify the board to clear all occurences of a given piece, replacing them
#  with EMPTY.
#
#  Parameters:
#    board: The game board to modify by swapping the pieces
#    sym: The symbol that should be removed 
#
#  Returns: None -- the game board passed as a parameter is modified
#
def clearAll(board, sym):
  for i in range(len(board)):
    for k in range(len(board[i])):
      if(board[i][k] == sym):
        board[i][k] = EMPTY

#
#  Insert your implementations of vLineAt (linha) and hLineAt (coluna) here
#

def vLineAt(board, row, col):
     #COMPARANDO O ANTERIOR COM O PRÓXIMO
    if(row >=1 and row<= len(board)-2):
        if(board[row][col] == board[row-1][col]) and (board[row][col] == board[row+1][col]):
            return True    
    #COMPARANDO OS 2 ANTERIORES
    if (row <= len(board)-1 and row >= 2 ):
        if(board[row][col] == board[row-1][col]) and (board[row][col] == board[row-2][col]):
            return True    
    #COMPARANDO OS 2 SEGUINTES
    if(row >= 0 and row <= len(board)-2):
        if(board[row][col] == board[row+1][col]) and (board[row][col] == board[row+2][col]):
            return True
    return False
    
def hLineAt(board, row, col):    
    #COMPARANDO O ANTERIOR COM O PRÓXIMO
    if(col >=1 and col<= len(board[row])-2):
        if(board[row][col] == board[row][col-1]) and (board[row][col] == board[row][col+1]):
            return True    
    #COMPARANDO OS 2 ANTERIORES
    if (col <= len(board[row])-1 and col >= 2 ):
        if(board[row][col] == board[row][col-1]) and (board[row][col] == board[row][col-2]):
            return True    
    #COMPARANDO OS 2 SEGUINTES
    if(col >= 0 and col <= len(board[row])-2):
        if(board[row][col] == board[row][col+1]) and (board[row][col] == board[row][col+2]):
            return True
    return False
        


#
#  Report whether or not two pieces on the board can be swapped.  The function
#  should only return true when performing the swap results in a line being
#  formed.
#
#  Parameters:
#    board: The game board to be checked
#    r1, c1: The row and column of the first piece involved in the swap
#    r2, c2: The row and column of the second piece to swap
#
#  Returns: True if the proposed swap creates a line.  False otherwise.
#
def canSwap(board, r1, c1, r2, c2):
  swap(board, r1, c1, r2, c2)
  if (hLineAt(board, r1, c1 ) or hLineAt(board, r2, c2) or vLineAt(board, r1, c1) or vLineAt(board, r2, c2)):
    swap(board, r1, c1, r2, c2)
    return True
  else:
    swap(board, r1, c1, r2, c2)
  return False

#
#  Identify two adjacent positions on the board that can be swapped to 
#  form a line.
#
#  Parameters:
#    board: The game board to be checked
#
#  Returns: The row and column of the first piece, followed by the row and
#           column of the second piece involved in the swap.  If no swap
#           is possible then -1, -1, -1, -1 is returned.
#
def hint(board):
  return -1, -1, -1, -1

##############################################################################
#
# Only modify code above this point in the file
#
##############################################################################

##############################################################################
##
##  Code for testing the functions written by the students
##
##############################################################################

# Determine whether or not a function exists in the namespace at the time
# this function is called
# Parameters:
#   name: The name of the function to check the existence of
# Returns: True if the function exists, False otherwise
def functionExists(name):
  members = inspect.getmembers(sys.modules[__name__])
  for (n, m) in members:
    if n == name and inspect.isfunction(m):
      return True
  return False

# Run a series of tests on the createBoard function
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def test_createBoard():
  print("Testing createBoard...")
  # Does the createBoard function exist?

  if functionExists("createBoard"):
    print("  The function seems to exist...")
  else:
    print("  The createBoard function doesn't seem to exist...")
    return False

  for (rows, cols, syms) in [(8, 8, 6), (8, 7, 5), (7, 7, 4), (6, 7, 3)]:
    # Try and call the function
    try:
      print("  Attempting to create a board: %d rows, %d columns and %d symbols... " % (rows, cols, syms), end="")
      b = createBoard(rows, cols, syms)
    except Exception as e:
      print("\n  An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      return False

    # Does it have the correct return type?
    if type(b) is not list:
      print("\n  The value returned was a", str(type(b)) + ", not a list.")
      return False

    # Does the list have the corret number of elements?
    if len(b) != rows:
      print("\n  The board had", len(b), "rows when", rows, "were expected.")
      return False

    # Is each row a list?  Does each row have the correct length?
    for i in range(len(b)):
      if type(b[i]) is not list:
        print("\n  The row at index", i, "is a", str(type(b[i])) + ", not a list.")
        return False
      if len(b[i]) != cols:
        print("\n  The row at index", i, "had", len(b[i]), "elements when", cols, "were expected.")
        return False
  
    # Is every space on the board populated with an integer value between 
    # 0 and syms (not including syms)?
    for r in range(0, len(b)):
      for c in range(0, len(b[r])):
        if type(b[r][c]) is not int:
          print("\n  The value in row", r, "column", c, "is a", str(type(b[r][c])) + ", not an integer")
          return False
        if b[r][c] < 0 or b[r][c] >= syms:
          print("\n  The integer in row", r, "column", c, "is a", b[r][c], "which is less than 0 or greater than", syms-1)
          return False
    print("Success.")

  print()
  return True

#
# Run a series of tests on the hLineAt function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def test_hLineAt():
  print("Testing hLineAt...")

  # Does the hLineAt function exist?
  if functionExists("hLineAt"):
    print("  The function seems to exist...")
  else:
    print("  The hLineAt function doesn't seem to exist...\n")
    return

  passed = 0
  failed = 0
  for (b, r, c, a) in [ \
      ([[0, 0, 0, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, 0, True), \
      ([[0, 0, 0, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, 1, True), \
      ([[0, 0, 0, 3, 4], \
        [1, 2, 3, 1, 2], \
        [3, 4, 5, 2, 3], \
        [4, 5, 1, 4, 5], \
        [1, 2, 3, 0, 1], \
        [0, 1, 2, 5, 0]], 0, 2, True), \
      ([[0, 0, 0, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, 3, False), \
      ([[0, 0, 0, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 1, 0, False), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 5, 6, True), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 5, 5, True), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 5, 4, True), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 5, 3, False), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 5, 5, True), \
      ([[2, 3, 4, 2, 3, 4], \
        [1, 2, 3, 5, 1, 2], \
        [3, 4, 5, 1, 2, 3], \
        [4, 5, 1, 3, 4, 5], \
        [1, 2, 3, 5, 0, 1], \
        [0, 1, 2, 0, 0, 0]], 0, 5, False), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 5, 0, False), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [0, 0, 5, 0, 1, 2, 0], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 2, 0, False), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [0, 0, 5, 0, 1, 2, 0], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 2, 6, False), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [0, 0, 5, 0, 1, 2, 0], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 2, 6, False)]:

    # Attempt the function call
    try:
      print("  Attempting to use hLineAt with row", r, "and column", c, "... ", end="")
      result = hLineAt(b, r, c)
    except Exception as e:
      print("\nFAILED: An exception occurred during the attempt.")
      print("The board was:")
      pprint(b)
      print()
      traceback.print_exc(file=sys.stdout)
      failed += 1
      continue

    # Does it have the correct return type?
    if type(result) is not bool:
      print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
      print("The board was:")
      pprint(b)
      print()
      failed += 1
      continue

    # Did it return the correct value
    if result != a:
      print("\nFAILED: The value returned was", str(result), "when", str(a), "was expected.")
      print("The board was:")
      pprint(b)
      print()
      failed += 1
      continue

    print("Success.")
    passed += 1

  print()
  return (passed, failed)

#
# Run a series of tests on the hLineAt function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def test_vLineAt():
  print("Testing vLineAt...")

  # Does the vLineAt function exist?
  if functionExists("vLineAt"):
    print("  The function seems to exist...")
  else:
    print("  The vLineAt function doesn't seem to exist...\n")
    return

  passed = 0
  failed = 0
  for (b, r, c, a) in [ \
      ([[0, 1, 0, 1, 2, 3, 4], \
        [0, 2, 3, 4, 5, 1, 2], \
        [0, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, 0, True), \
      ([[0, 2, 1, 1, 2, 3, 4], \
        [0, 2, 3, 4, 5, 1, 2], \
        [0, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 1, 0, True), \
      ([[0, 2, 1, 3, 4], \
        [0, 2, 3, 1, 2], \
        [0, 4, 5, 2, 3], \
        [4, 5, 1, 4, 5], \
        [1, 2, 3, 0, 1], \
        [0, 1, 2, 5, 0]], 2, 0, True), \
      ([[0, 5, 2, 1, 2, 3, 4], \
        [0, 2, 3, 4, 5, 1, 2], \
        [0, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 3, 0, False), \
      ([[0, 5, 3, 1, 2, 3, 4], \
        [0, 2, 3, 4, 5, 1, 2], \
        [0, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, 1, False), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 2], \
        [1, 2, 3, 4, 5, 0, 2], \
        [0, 1, 2, 3, 5, 4, 2]], 5, 6, True), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 4], \
        [1, 2, 3, 4, 5, 0, 4], \
        [0, 1, 2, 3, 0, 2, 4]], 4, 6, True), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 5], \
        [0, 1, 2, 3, 0, 0, 5]], 4, 6, True), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 5, 3, False), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 0, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 5, 5, True), \
      ([[2, 3, 4, 2, 3, 0], \
        [1, 2, 3, 5, 1, 0], \
        [3, 4, 5, 1, 2, 3], \
        [4, 5, 1, 3, 4, 5], \
        [1, 2, 3, 5, 0, 1], \
        [0, 1, 2, 0, 0, 0]], 0, 5, False), \
      ([[0, 3, 4, 1, 2, 3, 4], \
        [0, 2, 3, 4, 5, 1, 2], \
        [3, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 5, 0, False), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 4, 4, 5, 1, 2], \
        [0, 0, 5, 0, 1, 2, 0], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 4, 3, 0, 0, 0]], 0, 2, False), \
      ([[2, 3, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [0, 0, 5, 0, 1, 2, 0], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 2, 6, False), \
      ([[2, 3, 4, 3, 2, 3, 4], \
        [1, 2, 3, 3, 5, 1, 2], \
        [0, 0, 5, 0, 1, 2, 0], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 3, 5, 0, 1], \
        [0, 1, 2, 3, 0, 0, 0]], 5, 3, False)]:

    # Attempt the function call
    try:
      print("  Attempting to use vLineAt with row", r, "and column", c, "... ", end="")
      result = vLineAt(b, r, c)
    except Exception as e:
      print("\nFAILED: An exception occurred during the attempt.")
      print("The board was:")
      pprint(b)
      print()
      traceback.print_exc(file=sys.stdout)
      failed += 1
      continue

    # Does it have the correct return type?
    if type(result) is not bool:
      print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
      print("The board was:")
      pprint(b)
      print()
      failed += 1
      continue

    # Did it return the correct value
    if result != a:
      print("\nFAILED: The value returned was", str(result), "when", str(a), "was expected.")
      print("The board was:")
      pprint(b)
      print()
      failed += 1
      continue

    print("Success.")
    passed += 1

  print()
  return (passed, failed)

# Run a series of tests on the swap function
# Parameters: (None)
# Returns: True if all tests passed.  False if any test fails.
def test_swap():
  print("Testing swap...")
  # Does the swap function exist?

  if functionExists("swap"):
    print("  The function seems to exist...")
  else:
    print("  The swap function doesn't seem to exist...")
    return False

  for (board, r1, c1, r2, c2, ans) in [ \
      ([[0, 1, 2, 3], \
        [4, 5, 0, 1], \
        [2, 3, 4, 5], \
        [0, 1, 2, 3]], 
        0, 0, 1, 0, \
       [[4, 1, 2, 3], \
        [0, 5, 0, 1], \
        [2, 3, 4, 5], \
        [0, 1, 2, 3]]), \
      ([[0, 1, 2, 3, 4], \
        [4, 5, 0, 1, 3], \
        [2, 3, 4, 5, 2], \
        [0, 1, 2, 3, 1]], 
        3, 4, 3, 3, \
       [[0, 1, 2, 3, 4], \
        [4, 5, 0, 1, 3], \
        [2, 3, 4, 5, 2], \
        [0, 1, 2, 1, 3]]), \
      ([[0, 1, 2, 3, 4], \
        [4, 5, 0, 1, 3], \
        [2, 3, 4, 5, 2], \
        [4, 5, 0, 1, 3], \
        [2, 3, 4, 5, 2], \
        [0, 1, 2, 3, 1]], 
        4, 2, 5, 2, \
       [[0, 1, 2, 3, 4], \
        [4, 5, 0, 1, 3], \
        [2, 3, 4, 5, 2], \
        [4, 5, 0, 1, 3], \
        [2, 3, 2, 5, 2], \
        [0, 1, 4, 3, 1]]) \
    ]:
    # Try and call the function
    try:
      print("  Attempting to swap row %d col %d with row %d col %d... " % (r1, c1, r2, c2), end="")
      old_board = deepcopy(board)
      swap(board, r1, c1, r2, c2)
    except Exception as e:
      print("\n  An exception occurred during the attempt.")
      traceback.print_exc(file=sys.stdout)
      return False

    # Does board still have the correct type?
    if type(board) is not list:
      print("\n  The value returned was a", str(type(board)) + ", not a list.")
      return False

    # Does the list have the corret number of elements?
    if len(board) != len(old_board):
      print("\n  The board had", len(board), "rows when", len(old_board), "were expected.")
      return False

    # Is each row a list?  Does each row have the correct length?
    for i in range(len(board)):
      if type(board[i]) is not list:
        print("\n  The row at index", i, "is a", str(type(board[i])) + ", not a list.")
        return False
      if len(board[i]) != len(old_board[i]):
        print("\n  The row at index", i, "had", len(board[i]), "elements when", len(old_board[i]), "were expected.")
        return False
  
    if board == ans:
      print("Success.")
    else:
      print("\nThe swap function returned:")
      pprint(board)
      print("The expected result was:")
      pprint(ans)
      print()
      return False

  print()
  return True

#
# Run a series of tests on the canSwap function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def test_canSwap():
  print("Testing canSwap...")

  # Does the canSwap function exist?
  if functionExists("canSwap"):
    print("  The function seems to exist...")
  else:
    print("  The canSwap function doesn't seem to exist...")
    quit()

  passed = 0
  failed = 0
  for (b, r1, c1, r2, c2, a) in [ \
      ([[0, 1, 0, 1, 2, 3, 4], \
        [2, 0, 3, 4, 5, 1, 2], \
        [0, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, 1, 1, 1, True), \
      ([[0, 1, 0, 1, 2, 3, 4], \
        [2, 2, 3, 4, 5, 1, 2], \
        [0, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, 1, 1, 1, False), \
      ([[2, 1, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [1, 5, 1, 2, 3, 4, 5], \
        [3, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, 0, 0, 1, True), \
      ([[2, 1, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [1, 5, 1, 2, 3, 4, 5], \
        [3, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, 1, 0, 0, True), \
      ([[2, 1, 4, 1, 2, 3, 4], \
        [1, 2, 3, 4, 5, 1, 2], \
        [4, 5, 1, 2, 3, 4, 5], \
        [3, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, 1, 0, 0, False), \
      ([[3, 2, 1, 3, 4], \
        [0, 2, 3, 1, 2], \
        [0, 4, 5, 2, 3], \
        [4, 5, 1, 3, 1], \
        [1, 2, 3, 0, 1], \
        [0, 1, 2, 1, 0]], 5, 4, 5, 3, True), \
      ([[3, 2, 1, 3, 4], \
        [0, 2, 3, 1, 2], \
        [0, 4, 5, 2, 3], \
        [4, 5, 1, 3, 1], \
        [1, 2, 3, 0, 1], \
        [0, 1, 2, 1, 0]], 5, 3, 5, 4, True), \
      ([[3, 2, 1, 3, 4], \
        [0, 2, 3, 1, 2], \
        [0, 4, 5, 2, 3], \
        [4, 5, 1, 3, 1], \
        [1, 2, 3, 0, 2], \
        [0, 1, 2, 1, 0]], 5, 3, 5, 4, False), \
]:

    # Attempt the function call
    try:
      print("  Attempting to use canSwap with (%d, %d) and (%d, %d) ... " % (r1, c1, r2, c2), end="")
      result = canSwap(b, r1, c1, r2, c2)
    except Exception as e:
      print("\nFAILED: An exception occurred during the attempt.")
      print("The board was:")
      pprint(b)
      print()
      traceback.print_exc(file=sys.stdout)
      failed += 1
      continue

    # Does it have the correct return type?
    if type(result) is not bool:
      print("\nFAILED: The value returned was a", str(type(result)) + ", not a Boolean.")
      print("The board was:")
      pprint(b)
      print()
      failed += 1
      continue

    # Did it return the correct value
    if result != a:
      print("\nFAILED: The value returned was", str(result), "when", str(a), "was expected.")
      print("The board was:")
      pprint(b)
      print()
      failed += 1
      continue

    print("Success.")
    passed += 1

  print()
  return (passed, failed)

#
# Run a series of tests on the hint function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def test_hint():
  print("Testing hint...")

  # Does the hint function exist?
  if functionExists("hint"):
    print("  The function seems to exist...")
  else:
    print("  The hint function doesn't seem to exist...")
    quit()

  passed = 0
  failed = 0
  for (b, a1, a2, a3, a4) in [ \
      ([[0, 1, 0, 2, 2, 3, 3], \
        [4, 0, 4, 5, 5, 4, 4], \
        [3, 3, 2, 2, 1, 1, 0], \
        [4, 4, 5, 5, 4, 4, 2], \
        [3, 3, 2, 2, 1, 1, 0], \
        [4, 4, 5, 5, 4, 4, 2]], 0, 1, 1, 1), \
      ([[0, 0, 1, 1, 2, 2, 3], \
        [5, 5, 4, 4, 5, 5, 4], \
        [0, 0, 1, 1, 2, 2, 3], \
        [5, 5, 4, 4, 5, 5, 4], \
        [0, 0, 1, 1, 2, 2, 3], \
        [5, 5, 4, 4, 5, 5, 4]], -1, -1, -1, -1), \
      ([[3, 5, 1, 3, 4], \
        [0, 2, 3, 1, 2], \
        [0, 4, 5, 2, 3], \
        [4, 5, 1, 3, 1], \
        [1, 2, 3, 0, 2], \
        [0, 1, 2, 1, 0]], -1, -1, -1, -1), \
      ([[3, 0, 1, 3, 4], \
        [0, 2, 3, 1, 2], \
        [0, 4, 5, 2, 3], \
        [4, 5, 1, 3, 1], \
        [1, 2, 3, 0, 2], \
        [0, 1, 2, 1, 0]], 0, 0, 0, 1), \
]:

    # Attempt the function call
    try:
      print("  Attempting to use hint ... ", end="")
      result = hint(b)
    except Exception as e:
      print("\nFAILED: An exception occurred during the attempt.")
      print("The board was:")
      pprint(b)
      print()
      traceback.print_exc(file=sys.stdout)
      failed += 1
      continue

    # Does it have the correct return type?
    if type(result) is not tuple:
      print("\nFAILED: The value returned was a", str(type(result)) + ", not a tuple")
      print("The board was:")
      pprint(b)
      print()
      failed += 1
      continue

    if len(result) != 4:
      print("\nFAILED: The length of the returned tuple was", len(result), "when it should have been 4")
      print("The board was:")
      pprint(b)
      print()
      failed += 1
      continue

    # Did it return the correct value
    h1, h2, h3, h4 = result
    if result != (a1, a2, a3, a4) and result != (a3, a4, a1, a2):
      print("\nFAILED: The value returned was", h1, h2, h3, h4, "when", a1, a2, a3, a4, "or", a3, a4, a1, a2, "was expected.")
      print("The board was:")
      pprint(b)
      print()
      failed += 1
      continue

    print("Success.")
    passed += 1

  print()
  return (passed, failed)

#
# Run a series of tests on the clearAll function
# Parameters: (None)
# Returns: True if all tests passed.  False otherwise.
def test_clearAll():
  print("Testing clearAll...")

  # Does the clearAll function exist?
  if functionExists("clearAll"):
    print("  The function seems to exist...")
  else:
    print("  The clearAll function doesn't seem to exist...")
    quit()

  passed = 0
  failed = 0
  for (board, sym, ans) in [ \
      ([[0, 1, 0, 1, 2, 3, 4], \
        [2, 0, 3, 4, 5, 1, 2], \
        [0, 4, 5, 0, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, 0, 1], \
        [0, 1, 2, 3, 4, 5, 0]], 0, \
       [[-1, 1, -1, 1, 2, 3, 4], \
        [2, -1, 3, 4, 5, 1, 2], \
        [-1, 4, 5, -1, 1, 2, 3], \
        [4, 5, 1, 2, 3, 4, 5], \
        [1, 2, 3, 4, 5, -1, 1], \
        [-1, 1, 2, 3, 4, 5, -1]]), \
      ([[3, 5, 1, 3, 4], \
        [0, 2, 3, 1, 2], \
        [0, 4, 5, 2, 3], \
        [4, 5, 1, 3, 1], \
        [1, 2, 3, 0, 2], \
        [0, 1, 2, 1, 0]], 1, \
       [[3, 5, -1, 3, 4], \
        [0, 2, 3, -1, 2], \
        [0, 4, 5, 2, 3], \
        [4, 5, -1, 3, -1], \
        [-1, 2, 3, 0, 2], \
        [0, -1, 2, -1, 0]]) \
]:

    # Attempt the function call
    try:
      print("  Attempting to use clearAll with symbol %d ... " % sym, end="")
      result = deepcopy(board)
      clearAll(result, sym)
    except Exception as e:
      print("\nFAILED: An exception occurred during the attempt.")
      print("The board was:")
      pprint(board)
      print()
      traceback.print_exc(file=sys.stdout)
      failed += 1
      continue

    # Does it have the correct return type?
    if type(result) is not list:
      print("\n  The value returned was a", str(type(result)) + ", not a list.")
      return False

    # Does the list have the corret number of elements?
    if len(result) != len(board):
      print("\n  The board had", len(result), "rows when", len(board), "were expected.")
      return False

    # Is each row a list?  Does each row have the correct length?
    for i in range(len(result)):
      if type(result[i]) is not list:
        print("\n  The row at index", i, "is a", str(type(result[i])) + ", not a list.")
        return False
      if len(result[i]) != len(ans[i]):
        print("\n  The row at index", i, "had", len(result[i]), "elements when", cols, "were expected.")
        return False

    # Did it return the correct value
    if str(result) != str(ans):
      print("\nFAILED: The value returned was:")
      pprint(result)
      print("when")
      pprint(ans)
      print("was expected.")
      print("The board was:")
      pprint(board)
      print()
      failed += 1
      continue

    print("Success.")
    passed += 1

  print()
  return (passed, failed)


#
#  Load the sprites stored in fname
#
def loadSpriteSheet(fname):
  sheet = loadImage(fname)

  bg = tk.PhotoImage()
  bg.tk.call(bg, 'copy', sheet, '-from', 0, 0, 800, 600, '-to', 0, 0)

  images = []
  sel_images = []
  y = 600
  for i in range(7):
    images.append(tk.PhotoImage())
    images[-1].tk.call(images[-1], 'copy', sheet, '-from', 0, y, 50, y+50, '-to', 0, 0)
    y += 50

    sel_images.append(tk.PhotoImage())
    sel_images[-1].tk.call(sel_images[-1], 'copy', sheet, '-from', 0, y, 50, y+50, '-to', 0, 0)
    y += 50

  images.append(tk.PhotoImage())
  images[-1].tk.call(images[-1], 'copy', sheet, '-from', 0, y, 50, y+50, '-to', 0, 0)
  sel_images.append(tk.PhotoImage())
  sel_images[-1].tk.call(sel_images[-1], 'copy', sheet, '-from', 0, y, 50, y+50, '-to', 0, 0)
  y += 50

  win_image = tk.PhotoImage()
  win_image.tk.call(win_image, 'copy', sheet, '-from', 0, y, 400, y+200, '-to', 0, 0)

  lose_image = tk.PhotoImage()
  lose_image.tk.call(lose_image, 'copy', sheet, '-from', 0, y+200, 400, y+400, '-to', 0, 0)

  cc_m = tk.PhotoImage()
  cc_m.tk.call(cc_m, 'copy', sheet, '-from', 0, 1750, 379, 1750+44, '-to', 0, 0)

  cc_b = tk.PhotoImage()
  cc_b.tk.call(cc_b, 'copy', sheet, '-from', 0, 1794, 379, 1794+44, '-to', 0, 0)

  return bg, images, sel_images, win_image, lose_image, cc_m, cc_b

def drawItem(item, x, y, images):
  if item != EMPTY:
    drawImage(images[item], x, y)

def drawBoard(board, x, y, sr, sc, images, sel_images):
  background("black")
  for r in range(len(board)):
    for c in range(len(board[r])):
      # Draw an item that is selected in a different color
      if r == sr and c == sc and board[r][c] != EMPTY:
        drawImage(sel_images[board[sr][sc]], x + sc * 50, y + sr * 50)
      else:
        drawItem(board[r][c], x + c * 50, y + r * 50, images)

def allSame(a, b, c, d=None, e=None):
  if d == None and e == None:
    if a % 10 == b % 10 and b % 10 == c % 10:
      return True
    return False
  if e == None:
    if a % 10 == b % 10 and b % 10 == c % 10 and c % 10 == d % 10:
      return True
    return False
  if a % 10 == b % 10 and b % 10 == c % 10 and c % 10 == d % 10 and d % 10 == e % 10:
    return True
  return False

def collapse(board, syncAnim, asyncAnim, sf, num_syms):
#  print("Inside collapse...")

  l1 = list(range(50))
  l2 = list(range(50))
  l3 = list(range(50))
  l4 = list(range(50))
  l5 = list(range(50))
  shuffle(l1)
  shuffle(l2)
  shuffle(l3)
  shuffle(l4)
  shuffle(l5)

  old_board = deepcopy(board)
  changed = False

  # 5 horizontal
  for r in range(len(board) - 1, -1, -1):
    for c in range(len(board[0])-4):
      if board[r][c] != EMPTY and board[r][c] != BURST and allSame(board[r][c], board[r][c+1], board[r][c+2], board[r][c+3], board[r][c+4]):
        board[r][c] = EMPTY
        board[r][c+1] = EMPTY
        board[r][c+2] = BURST
        board[r][c+3] = EMPTY
        board[r][c+4] = EMPTY
        syncAnim.append(("crossfade", r, c+2, old_board[r][c+2], time()))
        changed = True
        asyncAnim.append(("score", r, c+2, old_board[r][c], 1000, time(), time()+1))
        sf += 1

  # 5 vertical
  for r in range(len(board) - 4 - 1, -1, -1):
    for c in range(len(board[0])):
      if board[r][c] != EMPTY and board[r][c] != BURST and allSame(board[r][c], board[r+1][c], board[r+2][c], board[r+3][c], board[r+4][c]):
        board[r][c] = EMPTY
        board[r+1][c] = EMPTY
        board[r+2][c] = BURST
        board[r+3][c] = EMPTY
        board[r+4][c] = EMPTY
        syncAnim.append(("crossfade", r+2, c, old_board[r+2][c], time()))
        changed = True
        asyncAnim.append(("score", r+2, c, old_board[r][c], 1000, time(), time()+1))
        sf += 1

  for r in range(len(board)):
    for c in range(len(board[r])):
      # T
      if (c > 0 and c < len(board[0]) - 1 and r < len(board) - 2 and 
          board[r][c] != EMPTY and board[r][c] != BURST and
          allSame(board[r][c], board[r][c-1], board[r][c+1], 
            board[r+1][c], board[r+2][c])):
        board[r][c] = BURST
        board[r][c-1] = EMPTY
        board[r][c+1] = EMPTY
        board[r+1][c] = EMPTY
        board[r+2][c] = EMPTY
        syncAnim.append(("crossfade", r, c, old_board[r][c], time()))
        changed = True
        asyncAnim.append(("score", r, c, old_board[r][c], 1000, time(), time()+1))
        sf += 1
    
      # Upside down T
      if (c > 0 and c < len(board[0]) - 1 and r >= 2 and
          board[r][c] != EMPTY and board[r][c] != BURST and
          allSame(board[r][c], board[r][c-1], board[r][c+1], 
            board[r-1][c], board[r-2][c])):
        board[r][c] = BURST
        board[r][c-1] = EMPTY
        board[r][c+1] = EMPTY
        board[r-1][c] = EMPTY
        board[r-2][c] = EMPTY
        syncAnim.append(("crossfade", r, c, old_board[r][c], time()))
        changed = True
        asyncAnim.append(("score", r, c, old_board[r][c], 1000, time(), time()+1))
        sf += 1
    
#      print("About to check |-- for row", r, "col", c)
      # |--
      if (c < len(board[0]) - 2 and r >= 1 and r < len(board) - 1 and
          board[r][c] != EMPTY and board[r][c] != BURST and
          allSame(board[r][c], board[r-1][c], board[r+1][c], 
            board[r][c+1], board[r][c+2])):
        board[r][c] = BURST
        board[r-1][c] = EMPTY
        board[r+1][c] = EMPTY
        board[r][c+1] = EMPTY
        board[r][c+2] = EMPTY
        syncAnim.append(("crossfade", r, c, old_board[r][c], time()))
        changed = True
        asyncAnim.append(("score", r, c, old_board[r][c], 1000, time(), time()+1))
        sf += 1
    
      # --|
      if (c >= 2 and r >= 1 and r < len(board) - 1 and
          board[r][c] != EMPTY and board[r][c] != BURST and
          allSame(board[r][c], board[r-1][c], board[r+1][c], 
            board[r][c-1], board[r][c-2])):
        board[r][c] = BURST
        board[r-1][c] = EMPTY
        board[r+1][c] = EMPTY
        board[r][c-1] = EMPTY
        board[r][c-2] = EMPTY
        syncAnim.append(("crossfade", r, c, old_board[r][c], time()))
        changed = True
        asyncAnim.append(("score", r, c, old_board[r][c], 1000, time(), time()+1))
        sf += 1
    
      # |_
      if (r >= 2 and c < len(board[0]) - 2 and
          board[r][c] != EMPTY and board[r][c] != BURST and
          allSame(board[r][c], board[r-1][c], board[r-2][c],
            board[r][c+1], board[r][c+2])):
        board[r][c] = BURST
        board[r-1][c] = EMPTY
        board[r-2][c] = EMPTY
        board[r][c+1] = EMPTY 
        board[r][c+2] = EMPTY 
        syncAnim.append(("crossfade", r, c, old_board[r][c], time()))
        changed = True
        asyncAnim.append(("score", r, c, old_board[r][c], 1000, time(), time()+1))
        sf += 1
    
      # _|
      if (r >= 2 and c >= 2 and
          board[r][c] != EMPTY and board[r][c] != BURST and
          allSame(board[r][c], board[r-1][c], board[r-2][c],
            board[r][c-1], board[r][c-2])):
        board[r][c] = BURST
        board[r-1][c] = EMPTY
        board[r-2][c] = EMPTY
        board[r][c-1] = EMPTY 
        board[r][c-2] = EMPTY 
        syncAnim.append(("crossfade", r, c, old_board[r][c], time()))
        changed = True
        asyncAnim.append(("score", r, c, old_board[r][c], 1000, time(), time()+1))
        sf += 1
    
      # |"
      if (r < len(board) - 2 and c < len(board[0]) - 2 and
          board[r][c] != EMPTY and board[r][c] != BURST and
          allSame(board[r][c], board[r+1][c], board[r+2][c],
            board[r][c+1], board[r][c+2])):
        board[r][c] = BURST
        board[r+1][c] = EMPTY
        board[r+2][c] = EMPTY
        board[r][c+1] = EMPTY 
        board[r][c+2] = EMPTY 
        syncAnim.append(("crossfade", r, c, old_board[r][c], time()))
        changed = True
        asyncAnim.append(("score", r, c, old_board[r][c], 1000, time(), time()+1))
        sf += 1
  
      # "|
      if (r < len(board) - 2 and c >= 2 and
          board[r][c] != EMPTY and board[r][c] != BURST and
          allSame(board[r][c], board[r+1][c], board[r+2][c],
            board[r][c-1], board[r][c-2])):
        board[r][c] = BURST
        board[r+1][c] = EMPTY
        board[r+2][c] = EMPTY
        board[r][c-1] = EMPTY 
        board[r][c-2] = EMPTY 
        syncAnim.append(("crossfade", r, c, old_board[r][c], time()))
        changed = True
        asyncAnim.append(("score", r, c, old_board[r][c], 1000, time(), time()+1))
        sf += 1
  
    
  # 4 horizontal
  for r in range(len(board) - 1, -1, -1):
    for c in range(len(board[0])-3):
      if board[r][c] != EMPTY and board[r][c] != BURST and allSame(board[r][c], board[r][c+1], board[r][c+2], board[r][c+3]):
        board[r][c] = EMPTY
        board[r][c+1] = EMPTY
        board[r][c+2] = EMPTY
        board[r][c+3] = EMPTY
        changed = True
        asyncAnim.append(("score", r, c+1, old_board[r][c], 60 * sf, time(), time()+1))
        sf += 1

  # 4 vertical
  for r in range(len(board) - 3 - 1, -1, -1):
    for c in range(len(board[0])):
      if board[r][c] != EMPTY and board[r][c] != BURST and allSame(board[r][c], board[r+1][c], board[r+2][c], board[r+3][c]):
        board[r][c] = EMPTY
        board[r+1][c] = EMPTY
        board[r+2][c] = EMPTY
        board[r+3][c] = EMPTY
        changed = True
        asyncAnim.append(("score", r+1, c, old_board[r][c], 60 * sf, time(), time()+1))
        sf += 1

  # 3 horizontal
  for r in range(len(board) - 1, -1, -1):
    for c in range(len(board[0])-2):
      if board[r][c] != EMPTY and board[r][c] != BURST and allSame(board[r][c], board[r][c+1], board[r][c+2]):
        board[r][c] = EMPTY
        board[r][c+1] = EMPTY
        board[r][c+2] = EMPTY
        changed = True
        asyncAnim.append(("score", r, c+1, old_board[r][c], 30 * sf, time(), time()+1))
        sf += 1

  # 3 vertical
  for r in range(len(board) - 2 - 1, -1, -1):
    for c in range(len(board[0])):
      if board[r][c] != EMPTY and board[r][c] != BURST and allSame(board[r][c], board[r+1][c], board[r+2][c]):
        board[r][c] = EMPTY
        board[r+1][c] = EMPTY
        board[r+2][c] = EMPTY
        changed = True
        asyncAnim.append(("score", r+1, c, old_board[r][c], 30 * sf, time()))
        sf += 1

  # Destroy everything that has been changed to empty
  num_destroyed = 0
  if changed:
    for c in range(len(board[0])):
      for r in range(len(board)):
        if board[r][c] == EMPTY:
          syncAnim.append(("destroy", r, c, old_board[r][c], l1, time(), time()+1))
          num_destroyed += 1

  #print("num_destroyed is", num_destroyed)
  if num_destroyed > 0:
    time_delay = 1
  else:
    time_delay = 0

  genFalls(board, time_delay, syncAnim, num_syms)

  if changed == False:
    return 1
  else:
    return sf

def genFalls(board, time_delay, syncAnim, num_syms):
  # Add falling to the animation queue
  for c in range(len(board[0])):
    b = blanksBelow(board, -1, c)
    if b > 0:
      for i in range(b):
        # New piece falling in from the top of the board
        syncAnim.insert(0, ("fall", -1 - i, c, randrange(num_syms), b, time()+time_delay, time()+time_delay+b*0.2))

    count = 0
    for r in range(len(board)):
      if board[r][c] != EMPTY:
        b = blanksBelow(board, r, c)
        if b > 0:
          # Pieces within the board fall
          syncAnim.insert(0, ("fall", r, c, board[r][c], b, time()+time_delay, time()+time_delay+b*0.2))
          board[r][c] = EMPTY


def blanksBelow(board, r, c):
  count = 0
  for i in range(r+1, len(board)):
    if board[i][c] == EMPTY:
      count = count + 1
  return count

def nonBlanksAbove(board, row, col, num, num_syms):
  r = row - 1
  count = 0
  while r >= 0 and count != num:
    if board[r][col] != EMPTY:
      count = count + 1
    r = r - 1

  if r >= 0:
    return board[r][col], r
  else:
    return randrange(num_syms), -1

def blanksImmediatelyAbove(board, row, col):
  count = 0
  r = row - 1
  while r >= 0 and board[r][col] == EMPTY:
    r = r - 1
    count = count + 1

  return count


def nextAbove(board, r, c):
  if board[r][c] != EMPTY:
    raise "Error: nextAbove called on a non-empty location"

  while r >= 0:
    if board[r][c] != EMPTY:
      return r 
    r = r - 1

  return r

def hasAnimType(anims, t):
  for a in anims:
    if a[0] == t:
      return True
  return False

def gray50(x, y, w, h):
  for i in range(x, x + w):
    if i % 2 == 0:
      line(i, y, i, y + h)

  for i in range(y, y + h):
    if i % 2 == 0:
      line(x, i, x + w, i)
  """
  for i in range(x, x + w):
    for j in range(y, y + h):
      if (i + j) % 2 == 0:
        line(i, j, i, j)
        """

#play(target_score, max_turns, rows, cols, syms)
def play(target_score, turns_left, num_rows, num_cols, num_syms, bg, cc_m, images, sel_images, win_image, lose_image):
  hoff = HOFF + (8 - num_cols) * 25
  voff = VOFF + (8 - num_rows) * 25

  frame_count = 0
  last_time = time()

  selected_r = -1
  selected_c = -1

  setFont("Arial", s=24)
  score_width = max(textWidth("Score:"), textWidth("000000"))
  score = 0
#  turns_left = 1

  syncAnim = []
#  syncAnim.append(("pause", time(), time()+3))
  asyncAnim = []

  #board = createBoard(8, 8, 5)
  board = createBoard(num_rows, num_cols, num_syms)
  clear()
  drawBoard(board, hoff, voff, -1, -1, images, sel_images)

  drawImage(bg, 0, 0)
  drawImage(cc_m, 23, 23)
  drawStatus(score, score_width, target_score, turns_left)
  update()
  sleep(0.5)
  clearMouseEvents()

  score_factor = collapse(board, syncAnim, asyncAnim, 1, num_syms)

  setAutoUpdate(False)

  game_state = RUNNING

  while not closed():
    clear()
    drawBoard(board, hoff, voff, selected_r, selected_c, images, sel_images)

    if len(syncAnim) == 0:
      score_factor = collapse(board, syncAnim, asyncAnim, score_factor, num_syms)
    if game_state == LOSE and len(syncAnim) == 0:
      syncAnim.append(("Lose", time() + 0.1))
    if game_state == WIN and len(syncAnim) == 0:
      syncAnim.append(("Win", time() + 0.1))

    if turns_left == 0 and score < target_score:
      game_state = LOSE
    if score >= target_score:
      game_state = WIN

    if len(syncAnim) > 0:
      index = 0
      setColor("black")
      while index < len(syncAnim):
        if index < len(syncAnim) and syncAnim[index][0] == "Win":
          ct = time()
          et = syncAnim[index][1]
          if ct >= et:
            gray50(hoff, voff, 400, 400)
            drawImage(win_image, getWidth() // 2 - getWidth(win_image) // 2,
                      getHeight() // 2 - getHeight(win_image) // 2)
          index += 1
        if index < len(syncAnim) and syncAnim[index][0] == "Lose":
          ct = time()
          et = syncAnim[index][1]
          if ct >= et:
            gray50(hoff, voff, 400, 400)
            drawImage(lose_image, getWidth() // 2 - getWidth(lose_image) // 2,
                      getHeight() // 2 - getHeight(lose_image) // 2)
          index += 1
        if index < len(syncAnim) and syncAnim[index][0] == "fall":
          r1 = syncAnim[index][1]
          c1 = syncAnim[index][2]
          v1 = syncAnim[index][3]
          b = syncAnim[index][4]
          st = syncAnim[index][5]
          et = syncAnim[index][6]
          ct = time()

          percent = (ct - st) / (et - st)
          if percent > 1:
            syncAnim.pop(index)
            percent = 1
            board[r1+b][c1] = v1
          else:
            index = index + 1

          if percent <= 0:
            drawItem(v1, hoff + c1 * 50, voff + r1 * 50, images)
            pass
          if percent > 0:
            drawItem(v1, hoff + c1 * 50, voff + r1 * 50 + percent * b * 50, images)
          
          
        if index < len(syncAnim) and syncAnim[index][0] == "pause":
          st = syncAnim[index][0]
          et = syncAnim[index][1]
          ct = time()
          if ct < et:
            index = index + 1
          else:
            syncAnim.pop(index)

        if index < len(syncAnim) and syncAnim[index][0] == "destroy":
          r1 = syncAnim[index][1]
          c1 = syncAnim[index][2]
          v1 = syncAnim[index][3]
          cols = syncAnim[index][4]
          st = syncAnim[index][5]
          et = syncAnim[index][6]
          ct = time()


          percent = (ct - st) / (et - st)

          if percent >= 0:
            drawItem(v1, hoff + c1 * 50, voff + r1 * 50, images)
          if percent > 1:
            syncAnim.pop(index)
            percent = 1

            board[r1][c1] = EMPTY


          else:
            index = index + 1

          setColor("black")
          for i in range(0, round(50 * percent)):
            line(hoff + c1 * 50 + cols[i], voff + r1 * 50,
                 hoff + c1 * 50 + cols[i], voff + r1 * 50 + 49)

        if index < len(syncAnim) and syncAnim[index][0] == "swap":
          r1 = syncAnim[index][1]
          c1 = syncAnim[index][2]
          v1 = syncAnim[index][3]
          r2 = syncAnim[index][4]
          c2 = syncAnim[index][5]
          v2 = syncAnim[index][6]
          st = syncAnim[index][7]
          et = syncAnim[index][8]
          ct = time()

          percent = (ct - st) / (et - st)
          if percent > 1:
            syncAnim.pop(index)
            percent = 1
          else:
            index = index + 1

          setColor("black")
          rect(hoff + c1 * 50, voff + r1 * 50, 50, 50)
          rect(hoff + c2 * 50, voff + r2 * 50, 50, 50)

          if abs(c1 - c2) == 1:
            drawItem(v2, 
                     hoff + c2 * 50 + (c1 - c2) * (percent) * 50, 
                     voff + r2 * 50 + (r1 - r2) * (percent) * 50 + 
                       sin(percent * 3.14) * 25, images)
            drawItem(v1, 
                     hoff + c2 * 50 + (c1 - c2) * (1 - percent) * 50, 
                     voff + r2 * 50 + (r1 - r2) * (1 - percent) * 50 - 
                       sin(percent * 3.14) * 25, images)
          else:
            drawItem(v2, 
                     hoff + c2 * 50 + (c1 - c2) * (percent) * 50 + 
                       sin(percent * 3.14) * 25, 
                     voff + r2 * 50 + (r1 - r2) * (percent) * 50, images)
            drawItem(v1, 
                     hoff + c2 * 50 + (c1 - c2) * (1 - percent) * 50 - 
                       sin(percent * 3.14) * 25, 
                     voff + r2 * 50 + (r1 - r2) * (1 - percent) * 50, images)

        if index < len(syncAnim) and syncAnim[index][0] == "crossfade":
          r = syncAnim[index][1]
          c = syncAnim[index][2]
          v1 = syncAnim[index][3]
          st = syncAnim[index][4]
          et = st + 1
          ct = time()

          percent = (ct - st) / (et - st)
          if percent > 1:
            syncAnim.pop(index)
            percent = 1
          else:
            index = index + 1

          w = getWidth(images[v1])
          h = getHeight(images[v1])
          cf = createImage(w, h)

          image1 = images[v1]
          image2 = images[BURST]

          for x in range(w):
            for y in range(h):
              r1, g1, b1 = getPixel(image1, x, y)
              r2, g2, b2 = getPixel(image2, x, y)
              p2 = min(percent, 1.0)
              p1 = max(1 - percent, 0)
              putPixel(cf, x, y, 
                       round(r1 * p1 + r2 * p2),
                       round(g1 * p1 + g2 * p2),
                       round(b1 * p1 + b2 * p2))

          drawImage(cf, hoff + c * w, voff + r * h)


        if index < len(syncAnim) and syncAnim[index][0] == "swap_and_back":
          r1 = syncAnim[index][1]
          c1 = syncAnim[index][2]
          v1 = syncAnim[index][3]
          r2 = syncAnim[index][4]
          c2 = syncAnim[index][5]
          v2 = syncAnim[index][6]
          st = syncAnim[index][7]
          et = syncAnim[index][8]
          ct = time()

          percent = (ct - st) / (et - st)
          if percent > 1:
            syncAnim.pop(index)
            percent = 1
          else:
            index = index + 1

          rect(hoff + c1 * 50, voff + r1 * 50, 50, 50)
          rect(hoff + c2 * 50, voff + r2 * 50, 50, 50)

          if percent < 0.5:
            np = percent * 2
          else:
            np = (percent * -1 + 1) * 2

          if abs(c1 - c2) == 1:
            drawItem(v2, 
                     hoff + c2 * 50 + (c1 - c2) * (np) * 50, 
                     voff + r2 * 50 + (r1 - r2) * (np) * 50 + 
                       sin(np * 3.14) * 25, images)
            drawItem(v1, 
                     hoff + c2 * 50 + (c1 - c2) * (1 - np) * 50, 
                     voff + r2 * 50 + (r1 - r2) * (1 - np) * 50 - 
                       sin(np * 3.14) * 25, images)
          else:
            drawItem(v2, 
                     hoff + c2 * 50 + (c1 - c2) * (np) * 50 + 
                       sin(np * 3.14) * 25, 
                     voff + r2 * 50 + (r1 - r2) * (np) * 50, images)
            drawItem(v1, 
                     hoff + c2 * 50 + (c1 - c2) * (1 - np) * 50 - 
                       sin(np * 3.14) * 25, 
                     voff + r2 * 50 + (r1 - r2) * (1 - np) * 50, images)

      if len(syncAnim) == 0:
        clearMouseEvents()
    elif peekMouseEvent() != None:
      mv = getMouseEvent()
      # Deselect
      if mv[0] == "<Button-2>" or mv[0] == "<Button-3>":
        selected_r = -1
        selected_c = -1
      if mv[0] == "<Button-1>":
        if selected_r == -1 and selected_c == -1 and mv[1][1] >= voff and mv[1][0] > hoff and mv[1][1] < voff + len(board) * 50 and mv[1][0] < hoff + len(board[0]) * 50:
          selected_r = (mv[1][1] - voff) // 50
          selected_c = (mv[1][0] - hoff) // 50
        elif mv[1][1] >= voff and mv[1][0] > hoff and mv[1][1] < voff + len(board) * 50 and mv[1][0] < hoff + len(board[0]) * 50:
          second_r = (mv[1][1] - voff) // 50
          second_c = (mv[1][0] - hoff) // 50
          
          if selected_r == second_r and abs(selected_c - second_c) == 1 or \
             selected_c == second_c and abs(selected_r - second_r) == 1:
            if (board[selected_r][selected_c] == BURST and \
                board[second_r][second_c] != BURST) or \
               (board[second_r][second_c] == BURST and \
                board[selected_r][selected_c] != BURST):
              if board[second_r][second_c] == BURST and \
                 board[selected_r][selected_c] != BURST:
                   selected_r, second_r = second_r, selected_r
                   selected_c, second_c = second_c, selected_c
              turns_left -= 1
              target_color = board[second_r][second_c]
              syncAnim.append(("swap", selected_r, selected_c, 
                               board[selected_r][selected_c], 
                               second_r, second_c, board[second_r][second_c],
                               current_time, current_time+0.5))
              swap(board, selected_r, selected_c, second_r, second_c)

              new_board = deepcopy(board)
              clearAll(new_board, target_color)

              l1 = list(range(50))
              st = time()
              for r in range(len(board)):
                for c in range(len(board[0])):
                  if new_board[r][c] == EMPTY:
                    l1 = list(range(50))
                    shuffle(l1)
                    syncAnim.append(("destroy", r, c, target_color, l1, st+0.5, st+1.5))
                    asyncAnim.append(("score", r, c, target_color, 30, time()+0.5))
              syncAnim.append(("destroy", second_r, second_c, BURST, l1, st+0.5, st+1.5))
              asyncAnim.append(("score", second_r, second_c, target_color, 30, time()+0.5))


              board[second_r][second_c] = EMPTY
              board[selected_r][selected_c] = EMPTY

            elif canSwap(board, selected_r, selected_c, second_r, second_c):
              turns_left -= 1
              syncAnim.append(("swap", selected_r, selected_c, 
                               board[selected_r][selected_c], 
                               second_r, second_c, board[second_r][second_c],
                               current_time, current_time+0.5))
              swap(board, selected_r, selected_c, second_r, second_c)
            else:
              syncAnim.append(("swap_and_back", selected_r, selected_c, 
                               board[selected_r][selected_c], 
                               second_r, second_c, board[second_r][second_c],
                               current_time, current_time+0.75))
            selected_r = -1
            selected_c = -1
          else:
            selected_r = second_r
            selected_c = second_c
            second_r = -1
            second_c = -1
    if (8 - num_rows) * 25 > 0:
      setColor("black")
      rect(HOFF, VOFF, 400, (8 - num_rows) * 25)
    drawImage(bg, 0, 0)
    drawImage(cc_m, 23, 23)

    keys = getKeys()
    if (('h' in keys) or ('H' in keys)) and len(syncAnim) == 0:
      r1, c1, r2, c2 = hint(board)
      if (r1 == -1) and (c1 == -1) and (r2 == -1) and (c2 == -1):
        asyncAnim.append(("no moves", time()))
      else:
        asyncAnim.append(("hint", r1, c1, r2, c2, time()))

    if (('r' in keys) or ('R' in keys)) and \
       (hint(board) == (-1, -1, -1, -1)) and \
       len(syncAnim) == 0:
      for r in range(len(board)):
        for c in range(len(board[r])):
          board[r][c] = EMPTY


        
    drawStatus(score, score_width, target_score, turns_left)
    index = 0
    while index < len(asyncAnim):
      if index < len(asyncAnim) and asyncAnim[index][0] == "no moves":
        st = asyncAnim[index][1]
        et = st + 1.5
        ct = time()

        percent = (ct - st) / (et - st)
        if percent > 1:
          asyncAnim.pop(index)
          percent = 1
        else:
          index = index + 1

        # Technically not cross fading, but by only going back to (50, 50, 50)
        # we get something that is close enough that there isn't a visual 'pop'
        intensity = 50 + 205 * sin(percent * pi)

        setColor(intensity, intensity, intensity)
        text(getWidth() // 2, 550, "No Hint Available")

      if index < len(asyncAnim) and asyncAnim[index][0] == "hint":
        r1 = asyncAnim[index][1]
        c1 = asyncAnim[index][2]
        r2 = asyncAnim[index][3]
        c2 = asyncAnim[index][4]
        st = asyncAnim[index][5]
        et = st + 1
        ct = time()

        percent = (ct - st) / (et - st)
        if percent > 1:
          asyncAnim.pop(index)
          percent = 1
        else:
          index = index + 1

        if percent < 0.5:
          intensity = 255 * percent * 2
        else:
          intensity = 255 * (1 - percent) * 2

        setOutline(intensity, intensity, intensity)
        setFill(None)

        if abs(r1-r2) == 1 and abs(c1-c2) == 0:
          rect(hoff + c1 * 50, voff + min(r1, r2) * 50, 50, 100)
        elif abs(r1-r2) == 0 and abs(c1-c2) == 1:
          rect(hoff + min(c1, c2) * 50, voff + r1 * 50, 100, 50)
        else:
          rect(hoff + c1 * 50, voff + r1 * 50, 50, 50)
          rect(hoff + c2 * 50, voff + r2 * 50, 50, 50)

      if index < len(asyncAnim) and asyncAnim[index][0] == "score":
        r1 = asyncAnim[index][1]
        c1 = asyncAnim[index][2]
        v1 = asyncAnim[index][3]
        a1 = asyncAnim[index][4]
        st = asyncAnim[index][5]
        et = st + 0.75
        ct = time()

        percent = (ct - st) / (et - st)
        if percent > 1:
          asyncAnim.pop(index)
          percent = 1
          score = score + a1
        else:
          index = index + 1

        if percent >= 0:
          x1 = hoff + c1 * 50
          y1 = voff + r1 * 50

          x = x1 + (SCORE_X - x1) * percent
          y = y1 + (SCORE_Y - 100 + 22 - y1) * percent

          setColor("white")
          text(x, y, a1, "c")

    update()
    current_time = time()
    if current_time - last_time < 1/30:
      sleep(1/30 - (current_time - last_time))
    frame_count = frame_count + 1
    last_time = current_time

def drawStatus(score, score_width, target_score, turns_left):
    setColor("black")
    rect(SCORE_X - score_width // 2 - 5, SCORE_Y - 41 - 100, score_width + 10, 72 + 10)
    rect(SCORE_X - score_width // 2 - 5, SCORE_Y - 41, score_width + 10, 72 + 10)
    rect(SCORE_X - score_width // 2 - 5, SCORE_Y - 41 + 100, score_width + 10, 72 + 10)
    setColor("white")
    text(SCORE_X, SCORE_Y - 41 - 100 + 22, "Score:", "c")
    text(SCORE_X, SCORE_Y - 41 - 100 + 22 + 36, "%06d" % score, "c")
    text(SCORE_X, SCORE_Y - 41 + 22, "Target:", "c")
    text(SCORE_X, SCORE_Y - 41 + 22 + 36, "%06d" % target_score, "c")
    text(SCORE_X, SCORE_Y - 41 + 100 + 22, "Turns:", "c")
    text(SCORE_X, SCORE_Y - 41 + 100 + 22 + 36, "%d" % turns_left, "c")


def main():
  if os.path.isfile("sprites.gif") == False:
    print("sprites.gif must be located in the same folder / directory as")
    print("your .py file.  Ensure that the name of the file is in all")
    print("lowercase letters.")
    close()
    quit()

  if test_createBoard() == False:
    close()
    quit()

  test_hLineAt()
  test_vLineAt()
  test_swap()
  test_canSwap()
  test_hint()
  test_clearAll()

  bg, images, sel_images, win_image, lose_image, cc_m, cc_b = loadSpriteSheet("sprites.gif")
  setAutoUpdate(False)
  while not closed():
    clear()
    background("black")
    drawImage(bg, 0, 0)
    drawImage(cc_b, getWidth() // 2 - getWidth(cc_b) // 2, 150)
  
    # Draw the buttons
    setFont("Arial", s=24)
  
    mx, my = mousePos()

    y = 250
    selected = ""
    for difficulty in ["Casual", "Normal", "Hard", "Brutal"]:
      if my >= y - 20 and my <= y + 20 and mx >= 345 and mx <= 455:
        selected = difficulty
        setColor(254,199,0)
      else:
        setColor("White")
      text(400, y, difficulty)
      y += 70
    
    #play()
    update()

    if selected != "" and leftButtonPressed():
      break
  
  target_score = 5000
  max_turns = 35
  rows = 8
  cols = 8
  syms = 5 
  if selected == "Normal":
    target_score = 15000
    max_turns = 32
    rows = 8
    cols = 7 
    syms = 5 
  if selected == "Hard":
    target_score = 5000
    max_turns = 30
    rows = 7
    cols = 7 
    syms = 6
  if selected == "Brutal":
    target_score = 10000
    max_turns = 35
    rows = 6
    cols = 7 
    syms = 6

  play(target_score, max_turns, rows, cols, syms, bg, cc_m, images, sel_images, win_image, lose_image)

main()
