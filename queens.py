
# 1) Start in the leftmost column
# 2) If all queens are placed
#     return true
# 3) Try all rows in the current column. 
#   Do following for every tried row.
#     a) If the queen can be placed safely in this row 
#       then mark this [row, column] as part of the 
#       solution and recursively check if placing
#       queen here leads to a solution.
#     b) If placing the queen in [row, column] leads to
#       a solution then return true.
#     c) If placing queen doesn't lead to a solution then
#       unmark this [row, column] (Backtrack) and go to 
#       step (a) to try other rows.
# 3) If all rows have been tried and nothing worked,
#   return false to trigger backtracking.

N = 4



def is_valid(board, row, col):

  in_range = False

  if row >=0 and row < N and \
     col >= 0 and col < N:
     in_range = True

  left = True

  for i in range(col):
    if board[row][i] == 1:
      left = False

  upper_left = True

  i, j = row-1, col-1

  while(i >= 0 and j >= 0):

    if (board[i][j] == 1):
      upper_left = False
      break

    i -= 1
    j -= 1

  lower_left = True

  i, j = row+1, col-1

  while(i < N and j >= 0):

    if (board[i][j] == 1):
      lower_left = False
      break

    i += 1
    j -= 1

  return in_range and left and upper_left and lower_left


def QueensUtil(board, col):

  if col >= N:
    return True

  for i in range(N):

    if is_valid(board, i, col):
      board[i][col] = 1

      if QueensUtil(board, col+1) == True:
        return True
      board[i][col] = 0

  return False

def Queens():

  board = [[0 for _ in range(4)] for _ in range(4)]
  sol = QueensUtil(board, 0)
  print("sol :", sol)
  print("board : ",board)

def main():

  Queens()

if __name__ == "__main__":
  main()