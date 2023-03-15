# 11.3
import re

email = "liaukouskaya01@gmail.hghg.com"
email1 = "liaukouskaya01@gmail..com"
email2 = "liaukouskaya01@-gmail.com"

def is_valid(x):
    # pattern = r'(^[^.-]+[a-zA-Z0-9.!#%&\'*=?^_{|}~]+[^.]+@[^.-]+[a-zA-Z0-9-][^-.]+\.[a-zA-Z0-9-]{1,63}+[^.-]+$)'

    if re.fullmatch(r'(^[^.-]+[a-zA-Z0-9.!#%&\'*=?^_{|}~]+[^.]+@[^.-]+([a-zA-Z0-9-][^-.]+\.[a-zA-Z0-9-]{1,63}[^.-])+$)', x):
        print("Проверка пройдена")
    else:
        print("Проверка не пройдена")


is_valid(email)
is_valid(email1)
is_valid(email2)
