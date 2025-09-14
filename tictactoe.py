import numpy as np

arr = np.full((3, 3), '#')

turn = 0

print("Input the row and column to make the first move!\nEntries must be between 1 and 3.")

def win(arr, player):
    
    for i in range(3):
            
            if (np.all(arr[:, i] == player) or np.all(arr[i, :] == player)):
                  
                  return True
    
    if np.all(np.diag(arr) == player) or np.all(np.diag(np.fliplr(arr)) == player):

        return True
    
    return False

while not (win(arr, 'X') or win(arr, 'O')) and '#' in arr:
      
      row, col = map(int, input().split())

      while not (1 <= row <= 3 and 1 <= col <= 3):
          
          print("Please ensure entries are from 1-3")

          row, col = map(int, input().split())

      row -= 1

      col -= 1

      if (turn % 2 == 0):

        arr[row,col] = 'X'

        print(arr)

      else:

        arr[row,col] = 'O'

        print(arr)
        
      turn += 1

if win(arr, 'X'):

    print(f"X wins on turn {turn}")

elif win(arr, 'O'):

    print(f"O wins on turn {turn}")

else:

    print("Draw")
     
