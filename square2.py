First=int(input("First number: "))
Second=int(input("Second number: "))
squares = [i*i for i in range(First, Second+1)]
evens = [x for x in squares if x % 2 == 0]
odds = [x for x in squares if x % 2 != 0]
print("Squares:", squares, "\nEven:", evens, "\nOdd:", odds)