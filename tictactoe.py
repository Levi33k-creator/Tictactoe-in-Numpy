import numpy as np

arr = np.full((3, 3), '#')

turn = 0

print("Input the row and column (i.e '1 3') to make the first move!\nEntries must be between 1 and 3.")

def win(arr, player):
    
    for i in range(3):
            
            if (np.all(arr[:, i] == player) or np.all(arr[i, :] == player)):
                  
                  return True
    
    if np.all(np.diag(arr) == player) or np.all(np.diag(np.fliplr(arr)) == player):

        return True
    
    return False

while not (win(arr, 'X') or win(arr, 'O')) and '#' in arr:
    
      while True:
          try:
             row, col = map(int, input("Enter row and col (1-3): ").split())

          except ValueError:
             
             print("Invalid input! Please enter two numbers like '2 3'")

             continue

          if not (1 <= row <= 3 and 1 <= col <= 3):
              
            print("Please ensure entries are from 1-3")

            continue

          if arr[row - 1, col - 1] != '#' :
              
            print("Please choose an empty cell")

            continue
          
          break

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
     
