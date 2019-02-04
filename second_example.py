from dwapi import datawiz
dw = datawiz.DW("test1@mail.com", "1qaz")
print(dw.get_shops())

from dwapi import datawiz_auth
dw = datawiz_auth.Auth()
a = dw.generate_secret("test1@mail.com", "1qaz")
print(a)