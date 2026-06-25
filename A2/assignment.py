#Q1
def power(x: int, y: int) -> int:
    
    result = wrapper_power(x,y)

    print(f'Final Result: {result}')
    return result

def wrapper_power(x,y):

        print(f'power({x}, {y})')


        if y==0:
            return 1
        
        return x*wrapper_power(x,y-1)






#Q2
def isEven(n: int) -> bool:
    result = wrapper_even(abs(n))
    print(f"Final Result: {result}")
    return result


def isOdd(n: int) -> bool:
    result = wrapper_odd(abs(n))
    print(f"Final Result: {result}")
    return result


def wrapper_even(n):
    print(f"isEven({n})")

    if n == 0:
        return True

    return wrapper_odd(n - 1)


def wrapper_odd(n):
    print(f"isOdd({n})")

    if n == 0:
        return False

    return wrapper_even(n - 1)






#Q3
def count_paths(grid: list) -> int:
    result = wrapper_count_pat(grid,0,0)
    print(f"Final Result: {result}")
    return result

def wrapper_count_pat(grid,row,col):
    rows = len(grid)
    cols = len(grid[0])

    if row >= rows or col>=cols:
        return 0
    
    if grid[row][col] == 1:
        return 0
    
    if row == rows-1 and col == cols-1:
        return 1

    
    return wrapper_count_pat(grid,row+1,col) + wrapper_count_pat(grid,row,col+1)






#Q4
def is_palindrome(s: str) -> bool:
    clean_str = ''

    for char in s:
        if char.isalnum():
            clean_str += char.lower()

    result = wrapper_palindrome_check(clean_str,0,len(clean_str)-1)
    print(f"Final Result: {result}")
    return result

    
def wrapper_palindrome_check(st,left,right):
    if left>=right:
        return True
    
    print(f"Comparing: '{st[left]}' and '{st[right]}'")

    if st[left] != st[right]:
        return False
    
    return wrapper_palindrome_check(st,left+1,right-1)







#Q5
def generate_subsets(nums: list) -> list:
    result = []
    wrapper_generate_subsets(nums, 0, [], result)
    print(f"Final Result: {result}")
    return result


def wrapper_generate_subsets(li,index,current,result):
    if index == len(li):
        result.append(current.copy())
        return
    
    current.append(li[index])
    wrapper_generate_subsets(li,index+1,current,result)

    current.pop()
    wrapper_generate_subsets(li,index+1,current,result)