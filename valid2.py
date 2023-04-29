# Function to check if all elements of the board[][] array store value in the range[1, 9]
def isinRange(board):
   
  N = 9
   
  # Traverse board[][] array
  for i in range(0, N):
    for j in range(0, N):
       
      # Check if board[i][j] lies in the range
      if ((board[i][j] <= 0) or
          (board[i][j] > 9)):
        return False
       
  return True
 
# Function to check if the solution of sudoku puzzle is valid or not
def isValidSudoku(board):
   
  N = 9
   
  # Check if all elements of board[][] stores value in the range[1, 9]
  if (isinRange(board) == False):
    return False
 
  # Stores unique value from 1 to N
  unique = [False] * (N + 1)
 
  # Traverse each row of the given array
  for i in range(0, N):
     
    # Initialize unique[] array to false
    for m in range(0, N + 1):
      unique[m] = False
 
    # Traverse each column of current row
    for j in range(0, N):
       
      # Stores the value of board[i][j]
      Z = board[i][j]
 
      # Check if current row stores duplicate value
      if (unique[Z] == True):
        return False
       
      unique[Z] = True
 
  # Traverse each column of the given array
  for i in range(0, N):
     
    # Initialize unique[] array to false
    for m in range(0, N + 1):
      unique[m] = False
 
    # Traverse each row of current column
    for j in range(0, N):
       
      # Stores the value of board[j][i]
      Z = board[j][i]
 
      # Check if current column stores duplicate value
      if (unique[Z] == True):
        return False
       
      unique[Z] = True
 
  # Traverse each block of size 3 * 3 in board[][] array
  for i in range(0, N - 2, 3):
     
    # j stores first column of each 3 * 3 block
    for j in range(0, N - 2, 3):
       
      # Initialize unique[] array to false
      for m in range(0, N + 1):
        unique[m] = False
 
      # Traverse current block
      for k in range(0, 3):
        for l in range(0, 3):
           
          # Stores row number of current block
          X = i + k
 
          # Stores column number of current block
          Y = j + l
 
          # Stores the value of board[X][Y]
          Z = board[X][Y]
 
          # Check if current block stores duplicate value
          if (unique[Z] == True):
            return False
           
          unique[Z] = True
           
  # If all conditions satisfied
  return True
 
# Driver Code
if __name__ == '__main__':
   
  board = [ [1, 2, 3, 4, 5, 8, 9, 6, 7],
            [9, 5, 8, 1, 6, 7, 3, 4, 2],
            [4, 6, 7, 9, 2, 3, 8, 1, 5],
            [8, 1, 9, 2, 3, 6, 5, 7, 4],
            [3, 4, 2, 5, 7, 1, 6, 8, 9],
            [5, 7, 6, 8, 9, 4, 1, 2, 3],
            [2, 8, 1, 3, 4, 9, 7, 5, 6],
            [6, 9, 4, 7, 8, 5, 2, 3, 1],
            [7, 3, 5, 6, 1, 2, 4, 9, 8] ]
 
  if (isValidSudoku(board)):
    print("Valid")
  else:
    print("Not Valid")