import re
from firebase import firebase
firebase = firebase.FirebaseApplication('https://tempandhum-4e7f3.firebaseio.com/', None)
result = firebase.get('/System Status',None)
print result
temp=firebase.get('/Coffee Temperature', None)
t1=float(re.search(r'\d+\.\d+', temp).group())
print t1
if result =='1':
    print'Yaay'
