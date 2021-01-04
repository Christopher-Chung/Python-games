# (c) Christopher Chung
# Solve a Sudoku

# Answers are of form: [[1,2,3,4],[3,4,1,2],[2,3,4,1],[4,1,2,3]]

import random
import copy

def border():
    """build a row"""
    s = '+' + '-' * 3
    s1 = s * 3 + '+'
    return ' ' * 20 + s1 * 3

def row(lis):
    """numbers of a row
    >>> row([1,2,3,4,5,6,7,8,9])
    '|1|2|3||4|5|6||7|8|9||'
    """
    s = " " * 20 + '|'
    for i in range(len(lis)):
        if lis[i] == 0:
            s = s + '   ' + "|"
        else:
            s = s + ' ' + str(lis[i]) + ' ' + "|"
        if i == 2 or i == 5:
            s += '|'
    return s

def draw(ans):
    """Draw entire thing"""
    print(border())
    for i in range(9):
        print(row(ans[i]))
        print(border())
        if i == 2 or i == 5:
            print(border())


def findempty(arr,l):
    """Finds the location in grid that is empty"""
    for row in range(9): 
        for col in range(9): 
            if not arr[row][col]: 
                l[0] = row 
                l[1] = col 
                return True
    return False
  
def usedrow(arr,row,num):
    for i in range(9): 
        if arr[row][i] == num: 
            return True
    return False
  

def usedcol(arr,col,num):
    for i in range(9):
        if arr[i][col] == num: 
            return True
    return False
   
def usedsq(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if arr[i+row][j+col] == num: 
                return True
    return False
  

def checklegal(arr,row,col,num):

    return not usedrow(arr,row,num) and not usedcol(arr,col,num) and not usedsq(arr,row - row%3,col - col%3,num)
  
 
def solve1(arr):
    l = [0,0]
    if not findempty(arr,l):
        return True
    row = l[0]
    col = l[1]
    for num in range(1,10):
        if checklegal(arr,row,col,num):
            arr[row][col] = num
            if solve1(arr):
                return True
            arr[row][col] = 0      
    return False

def solve2(arr):
    l2 = [0,0]
    if not findempty(arr,l2):
        return True
    row2 = l2[0]
    col2 = l2[1]
    for num2 in [9,8,7,6,5,4,3,2,1]:
        if checklegal(arr,row2,col2,num2):
            arr[row2][col2] = num2
            if solve2(arr):
                return True
            arr[row2][col2] = 0      
    return False


def poss(x,y,ans):
    """Consider the possibilities...
    x,y describe ans[x][y] position.
    Returns a list of possibilities if square is unfilled."""

    if not ans[x][y]:

        lis = [1,2,3,4,5,6,7,8,9]
        for i in range(9): #Check horizontal
            if ans[x][i]:
                try:
                    lis.remove(ans[x][i])
                except ValueError:
                    pass
        for i in range(9): #Check vertucal
            if ans[i][y]:
                try:
                    lis.remove(ans[i][y])
                except ValueError:
                    pass

        a,b = x//3,y//3 #Which cell is it in?
        for i in range(3): # Check cell
            for j in range(3):
                if ans[a*3 + i][b*3 + j]:
                    try:
                        lis.remove(ans[a*3 + i][b*3 + j])
                    except ValueError:
                        pass

        return lis

    else:
        return [ans[x][y]]

def rangen():
    ans = [[0 for a in range(9)] for b in range(9)]
    k = 0
    for i in range(0,9):
        for j in range(0,9):
            if k == 13:
                return ans
            else:
                if [i, j] == [0, 0]:
                    ans[i][j] = random.choice(poss(i,j,ans))
                else:
                    if random.random() > 0.6:
                        ans[i][j] = random.choice(poss(i,j,ans))
                        k += 1
    return False

def gen():
    ans = rangen()
    while not rangen() or not solve1(ans):
        ans = rangen()
    return ans

def remove(ans):
    i, j = random.randint(0,8), random.randint(0,8)
    while ans[i][j] == 0:
        i, j = random.randint(0,8), random.randint(0,8)
    k = ans[i][j]
    ans[i][j] = 0
    return [i,j,k]

def fullgen():
    a = gen()
    for i in range(70):
        k = remove(a)
        a1 = copy.deepcopy(a)
        a2 = copy.deepcopy(a)
        solve1(a1)
        solve2(a2)
        if a1 != a2:
            a[k[0]][k[1]] = k[2]
            break
    return a

def count(a):
    q = 0
    for i in range(9):
        for j in range(9):
            if a[i][j]:
                q += 1
    return q

def main():
    q = 81
    while q >= 33:
        a = fullgen()
        q = count(a)
    draw(a)
    a1 = copy.deepcopy(a)
    solve1(a1)
    for _ in range(20):
        print('')
    draw(a1)

if __name__ == '__main__':
    main()