import random  

secret = random.randint(1,100)

print("Guess the number between 1 and 100")

attempt = 0

while True:

     guess=int(input("Enter guess:"))
     attempt= attempt+1
     if guess < 1 or guess > 100:
         print("Enter number between 1 and 100")
         continue
     if guess > secret:
         print("too high")
     elif guess < secret:
         print("too low")      
     else:
         print("Correct, YOU WIN")
         print("Attempts:", attempt)
         break
