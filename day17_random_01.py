for i in range(100):
    print(randint(1000,9999),end=',')

    
1998,4421,5853,5568,4076,6797,4305,3855,4019,7463,7411,8854,5495,8980,8108,6968,2611,4425,7754,2804,1315,2564,6012,9984,6076,9183,7708,8724,2259,7756,4316,5822,5658,7841,5556,7503,6730,9159,9824,3778,6113,6854,5779,5360,7365,4822,4748,3460,4322,5693,1661,1435,6571,6373,5588,3997,6277,7996,3945,1638,4646,9479,3065,2072,7270,9643,6731,1191,1175,3606,7097,1926,8552,9081,4586,9779,2840,1590,2606,1879,9257,5222,5529,6925,2974,8293,2972,1492,8412,9956,4094,9093,7932,9392,4191,7593,5802,1875,3806,2880,

================================ RESTART: Shell ================================
for i in range(100):
    print(randint(1000,9999),end=',')

    
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    print(randint(1000,9999),end=',')
NameError: name 'randint' is not defined
from random import *
uniform(1,100)
92.60954231995456
uniform(1,100)
58.077785017704265
uniform(1,1000)
512.7668073107329
random()
0.8458877511805364
import ramdom as r
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    import ramdom as r
ModuleNotFoundError: No module named 'ramdom'
import random as r
r.randint(1000,5000)
1791
r.randint(1000,9999)
6046
for i in range(100):
    print(r.randint(1000,9999),end=',')

#output    
5910,4039,3759,9467,5999,2902,2026,4085,9076,9544,
8316,5642,2070,4361,4543,1937,5747,7666,1867,4701,
5438,2595,8630,3511,2717,4772,1773,2006,5631,7972,
9316,9179,9858,4728,5815,8959,9926,2159,1542,9801,
9562,5468,7889,6448,1913,6441,3836,6207,9688,8947,
2899,6450,6513,4374,6406,7576,4306,2604,2007,4785,
2257,6586,3108,4418,4825,3473,7406,7931,2673,3977,
8862,6535,9729,7845,4555,9403,5207,9528,8547,4110,
4991,2939,1309,2794,7089,7798,6732,3003,4404,2668,
4519,5967,8065,6627,3302,7662,3177,3471,4250,6987,

r.uniform(10,1000)
559.386410840071
r.uniform(10,1000)
627.0789849398208
r.uniform(1,1000)
221.81620742794757
help(r.random)

'''Help on built-in function random:

random() method of random.Random instance
    random() -> x in the interval [0, 1).
'''
##help(r.randint())
##Traceback (most recent call last):
##  File "<pyshell#35>", line 1, in <module>
##    help(r.randint())
##TypeError: Random.randint() missing 2 required positional arguments: 'a' and 'b'
##help(r.randint(a,b))
##Traceback (most recent call last):
##  File "<pyshell#36>", line 1, in <module>
##    help(r.randint(a,b))
##NameError: name 'a' is not defined
help(r.randint)
'''Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
'''
help(r.uniform)

'''Help on method uniform in module random:

uniform(a, b) method of random.Random instance
    Get a random number in the range [a, b) or [a, b] depending on rounding.
'''
a=[12,'manohar',45,89,'**',35,'java']
r.shuffle(a)
a
[35, 45, 'java', 12, '**', 'manohar', 89]

help(r.shuffle)
'''Help on method shuffle in module random:

shuffle(x) method of random.Random instance
    Shuffle list x in place, and return None.
'''
