# Example. You can change it with another function than open().
try:
   open(argv[1])
   open(argv[2])
except:
   print("Arguments is invalid.")

# Example 2. You can use the error label aka exception to specify the error type.
try:
   open(argv[1])
   open(argv[2])
except IndexError:
   print("Arguments is invalid.")
