##date:14/12/2022

#import re
#s="Python is an Interpreted programming Language"
#match=re.search(r'programming',s)
#print('start index:',match.start())
#print('end index:',match.end())


#import re
#phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo=phoneNumRegex.search('My number is 639-802-6744.')
#print('Phone number found:'+mo.group())

import re
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo=phoneNumRegex.search('My number is 639-802-6744.')
print(mo.group(2))