
from past.builtins import long

y = 3
if isinstance(y, (int, long)):
    print (“y is an Integer”)
else:
    print (“y is not an integer”)