user_input = int(input("enter the binary value"))

bits = list(str(user_input))

decimal = 0

counter = 0

for i in reversed(bits):
    decimal += 2**counter * int(i)
    counter+=1

print 'The corresponding decimal value is: ', decimal