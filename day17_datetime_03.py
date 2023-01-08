import datetime
import calendar
ob=datetime.datetime.now()
s1=str(ob.day)+ '_' +str(ob.month)+'_'+str(ob.year)
s2=str(ob.hour)+ '_' +str(ob.minute)+'_'+str(ob.second)
s3='bacup_'+s1+'_'+s2+'.db'
print(s3)
