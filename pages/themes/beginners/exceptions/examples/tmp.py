def get_user_number():
  user_number = int(input("Enter a number: "))
  return user_number

try:
  x = get_user_number()
  res = 10/x
  print("Result is {}".format(res))
except ValueError:
  print("You did not enter a number!")
except ZeroDivisionError:
  print("Enter a number different from zero (0)!")
except:
  print("Oops! Something went wrong!")