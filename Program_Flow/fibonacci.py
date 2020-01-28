def fibonacci(n):
    prevNum = 0
    currentNum = 1
    counter = 2

    print(prevNum)
    print(currentNum)

    while counter <= n:
        nextNum = prevNum + currentNum
        print(nextNum)
        prevNum = currentNum
        currentNum = nextNum
        counter += 1;


def fibonacciLimit(n):
     prevNum = 0
     currentNum = 1
     count = 2

     print(prevNum)
     print(currentNum)

     while(currentNum<n):
         nextNum = prevNum+currentNum
         prevNum =currentNum
         if nextNum < n:
             currentNum = nextNum
             print(nextNum)
             count+=1


# Test
fibonacci(7)
fibonacciLimit(40)
