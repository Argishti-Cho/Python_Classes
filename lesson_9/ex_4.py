from turtle import title


age  = int(input('please enter your age:  '))
sex  = (input('please enter your sex M/F:  ')).title()
status  = (input('please enter your marital status Y/N :  '))
yes = 'Y'
no = 'NO'
male = 'M'
female = 'F'
# sex = sex.title(sex)
 
# ageOfUser = range(age[40:60])
if age >= 40 and age <= 60 and sex == male:
    print('he us working in urban areas')
else:
    print('error')

