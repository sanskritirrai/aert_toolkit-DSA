# 1) Stack ADT

class StackADT:
    def __init__(self):
        self.data=[]

    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.data.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.data[-1]
    def is_empty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)
    
# 2) Factorial (Recursive)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# 3) Fibonacci (Naive)

nc = 0
mc = 0

def fib_naive(n):
    global nc
    nc += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# 4) Fibonacci (Memoized)

def fib_memo(n, memo=None):
    global mc
    mc += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# 5) Tower of Hanoi (using stack)

def hanoi(n, source, aux, dest,stack):
    if n==1:
        stack.push(f"Move disk 1 from {source} to {dest}")
        return
    hanoi(n-1, source, dest, aux,stack)
    stack.push(f"Move disk {n} from {source} to {dest}")
    hanoi(n-1, aux, source, dest,stack)

# 6) Recusive Binary Search

def binary_search(arr, target, low, high):
    if low>high:
        return -1
    mid=(low+high)//2

    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr, target, low, mid-1)
    else:
        return binary_search(arr, target, mid+1, high)

# Main Function

def main():

    print ("------- Factorial -------")
    for n in [0,1,5,10]:
        print(f"Factorial of {n} is {factorial(n)}")
    
    print("\n------- Fibonacci -------")
    for n in [1,2,3,4,5]:
        global nc,mc
        nc=0
        mc=0
        print("\nn=",n)
        print(f"Navie Fibonacci of {n} is {fib_naive(n)} with {nc} calls")
        print(f"Memoized Fibonacci of {n} is {fib_memo(n)} with {mc} calls")
    
    print("\n------- Tower of Hanoi (n=3)-------")
    stack=StackADT()
    hanoi(3, 'A', 'B', 'C',stack)
    while not stack.is_empty():
        print(stack.pop())
    
    print("\n------- Binary Search -------")
    arr=[1,2,3,4,5,6,7,8,9,10]
    for target in [1,5,10,11]:
        print(f"Search {target} -> {binary_search(arr, target, 0, len(arr)-1)}")

    print ("Empty list search" , binary_search([], 1, 0, -1 ))

if __name__ == "__main__":
    main()