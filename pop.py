TV = int(input("How many TVs:"))
DVD = int(input("How many DVD players:"))
Audio = int(input("How many Audio System:"))

sum = TV * 6000 + DVD *1500 + Audio * 3000

print("Total price is %.2f baht" % sum)

sale = sum

if sum >= 24000 :

     discount =  0.2 * sum
     sale = sum - discount
     print("You’ve got a discount of %.2f baht" % discount)

print("Your payment is %.2f baht" % sale )