from string import Formatter
import gettext
s = 'Reply from 8.8.8.8: bytes=32 time=38ms TTL=60'

x1, x2, x3, x4, x5, x6 = s.split(' ')
x5 = str(x5.strip('time='))
x5 = str(x5.strip('ms'))
x3 = str(x3.strip(':'))
print(x3)
print(x5)
