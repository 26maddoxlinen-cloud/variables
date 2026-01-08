intvar = 7
floatvar = (intvar) / 3.25
string1 = "calculus"
string2 = "Physics"

print(intvar)
print(floatvar)
print(string1)
print(string2)

print("use yes or no")
print("Do you want to change any variables?")
ans = input()
if ans == "yes":
      print("Do you want to change the first variable.")
      ans = input()
      if ans == "yes":
         intvar = input()


      print("Do you want to change the second variable.")
      ans = input()
      if ans == "yes":
         floatvar = input()

      print("Do you want to change the third variable.")
      ans = input()
      if ans == "yes":
         string1 = input()


      print("Do you want to change the last variable.")
      ans = input()
      if ans == "yes":
         string2 = input()

print(intvar)
print(floatvar)
print(string1)
print(string2)