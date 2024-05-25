# Greet the user Good Morning/ afternoon/ evening/ night depending on time 
# We will develop the program based on condition on current hour 

import time 
l_t = time.localtime(time.time())
#print(l_t)

h = l_t.tm_hour
# Night 10 pm to 6 am 
if h < 6:
    print("Good Night Sir")
elif h < 12:
    print("Good Morning Sir")
elif h < 18:
    print("Good Afternoon Sir")
elif h < 22:
    print("Good Evening")
else:
    print("Good Night")
