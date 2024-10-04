import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

#----------------------------------------------------------------
#39:0
#Catch from Information Groups
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(urls)
for match in matches:
    print(match)

#<re.Match object; span=(1, 23),  match='https://www.google.com'>
#<re.Match object; span=(24, 42), match='http://coreyms.com'>
#<re.Match object; span=(43, 62), match='https://youtube.com'>
#<re.Match object; span=(63, 83), match='https://www.nasa.gov'>



#42:0
#GROUP-1 = (www\.)
#GROUP-2 = (\w+)
#GROUP-3 = (\.\w+)
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match)
#<re.Match object; span=(1, 23),  match='https://www.google.com'>
#<re.Match object; span=(24, 42), match='http://coreyms.com'>
#<re.Match object; span=(43, 62), match='https://youtube.com'>
#<re.Match object; span=(63, 83), match='https://www.nasa.gov'>



for match in matches:
    print(match.group(0), match.group(1),match.group(2),match.group(3))
	
#group(0)               group(1)     group(2)    group(3)
#https://www.google.com www.         google      .com
#http://coreyms.com     None         coreyms     .com
#https://youtube.com    None         youtube     .com
#https://www.nasa.gov   www.         nasa        .gov

#----------------------------------------------------------------
#44:07
#Back Reference
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

#google.com
#coreyms.com
#youtube.com
#nasa.gov
#----------------------------------------------------------------

#My Method
pattern = re.compile(r'[a-z]+\.(com|gov)')
matches = pattern.finditer(urls)
for match in matches:
    print(match)

#<re.Match object; span=(13, 23), match='google.com'>
#<re.Match object; span=(31, 42), match='coreyms.com'>
#<re.Match object; span=(51, 62), match='youtube.com'>
#<re.Match object; span=(75, 83), match='nasa.gov'>