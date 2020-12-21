import re

txt = 'wutai'

x = re.findall('^[quit watching]*$', txt)
print(x)    