# recursive function
def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)

# while loop

def fiboLoop(num):
    prev = 1
    prev_prev = 0
    curr = 0
    
    while num != 1:
        num -= 1
        curr = prev + prev_prev
        prev_prev = prev
        prev = curr
    
    return curr
        
#print(fiboLoop(5))
