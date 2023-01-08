import datetime
import calendar
ob=datetime.datetime.now()
print(type(ob))
print("-"*30)
print(ob)
print(ob.year)
print(ob.month)
print(ob.day)
print(ob.hour)
print(ob.minute)
print(ob.second)
str1=str(ob.hour) + ':' + str(ob.minute) +':' +str(ob.second)
print(str1)
print("-"*30)
print("1 week ago it was: ",ob - datetime.timedelta(weeks=1))
print("100 days ago it was: ",ob - datetime.timedelta(days=100))
print("1 week from now it will be : ",ob + datetime.timedelta(weeks=1))
print("100 days later it will be: ",ob + datetime.timedelta(weeks=1))
bday_manohar=datetime.datetime(1997,6,19)
print('-'*30)
print('birthday in -------',ob - bday_manohar)
##my_date=date.today()
##print(calendar.day_name[my_date.weekday()])
#output
<class 'datetime.datetime'>
------------------------------
2023-01-08 12:17:26.352736
2023
1
8
12
17
26
12:17:26
------------------------------
1 week ago it was:  2023-01-01 12:17:26.352736
100 days ago it was:  2022-09-30 12:17:26.352736
1 week from now it will be :  2023-01-15 12:17:26.352736
100 days later it will be:  2023-01-15 12:17:26.352736
------------------------------
birthday in ------- 9334 days, 12:17:26.352736
