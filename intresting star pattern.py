# print this pattern
#    *
#   ***
#  *****
# ******* 
#*********
for i in range(1,6) :
    for j in range (1,6-i) :
        print(' ',end='')
    for k in range(0,2*i-1) :
        print('*',end='')
    print ('')
    
