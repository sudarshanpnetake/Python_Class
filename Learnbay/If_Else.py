marks = 45

if marks > 60:
    if marks > 80:
        if marks > 90:
            print('grade A')
        else:
            print('grade B')
    else:
        print('grade C')
else:
    print('grade D')
    
# if-elif
    
    number = -78

if number > 0:
    print('positive number')
elif number < 0:
    print('negative number')
else:
    print('zero')

#-----------------------

languages = ['Java','Python','C','JS','React']
word = 'Python'

for l in languages:
    print(l)
    
for w in word:
    print(w)
    
    break
sum=0
for i in range(0,6):    # 0 to 5
    sum = sum + i
print('sum is', sum)