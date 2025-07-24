for i in range(1, 101):
    div3 = i%3
    div5 = i%5
    if div3 == 0 and div5 != 0:
        print("Fizz")
    elif div5 == 0 and div3 != 0:
        print("Buzz")
    elif div3 == 0 and div5 ==0:
        print("Fizz Buzz")
    else:
        print(i)