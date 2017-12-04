import six

y = 3
if isinstance(y, six.integer_types):
    print (“y is an Integer”)
else:
    print (“y is not an integer”)