import datetime
from datetime import date
import time
from time import time

#pip module
from camelcase import CamelCase

#Import custom module

import validator
from validator import validate_email

today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('hello there world'))

email = 'test@test.com'


print(today)