import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
print(text_to_search[1:4])

for match in matches:
        print(match)


pattern = re.compile(r'abc')
pattern = re.compile(r'\.')  #matches only period
pattern = re.compile(r'coreyms\.com')
pattern = re.compile(r'.')   #matches Any Character Except New Line
pattern = re.compile(r'\d')  #Matches all digits
pattern = re.compile(r'\D')  #Matches all non-digits
pattern = re.compile(r'\w')  #Matches upper case, lower case, digits and underscore
pattern = re.compile(r'\W')  #Not any characters or digits and underscore
pattern = re.compile(r'\s')  #space, tab, newline
pattern = re.compile(r'\S')  #NOT[space, tab, newline]

#10:21 - Metacharacters continued. Anchors. Word boundaries.
pattern = re.compile(r'\bHa')                         #Word Boundary
pattern = re.compile(r'\BHa')                         #Not Word Boundary
pattern = re.compile(r'^Start')                       #Search at beginning
pattern = re.compile(r'end$')                         #Search at end

#14:00 Phone Numbers
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')       #match phone numbers of xxx[-*.]xxx[-*.]xxxx
pattern = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\d')     #match phone numbers of format xxx.xxx.xxxx


#16:10
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')      #all phone numbers from data.txt
with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)

#19:00[Character Set]
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') #match phone numbers ONLY of format xxx[-.]xxx[-.]xxxx. Matching either dash(-) or dot(.)No Need of Backslash
                                                      #[-.] is called CharacterSet. Any of the characters get matched
#21:00
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') #Match 800 or 900 starting numbers



#22:55[Range in Character Set]
pattern = re.compile(r'[1-5]')     #Any Digits between 1-5
pattern = re.compile(r'[a-zA-Z]')  #Any Lowercase or Uppercase
pattern = re.compile(r'[^a-zA-Z]') #Negate CharacterSet
pattern = re.compile(r'[^b]at')    #[not b]at. e.g cat,mat,pat

#25:00
#Quantifiers
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') #3digit[any char] 3digit[any char] 4digit


#28:00
pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*') 
#Mr. Schafer   #'(Mr|Mrs|Ms) -> Either Mr|Mrs|Ms
#Mr Smith      # \.?    Looks dot character .If not found that is Okay
#Ms Davis      # \s     is for space
#Mrs. Robinson # [A-Z]  followed by One character in Upper Case
#Mr. T         # \w*    0 or more [Word Character]
------------------------------------------------------------------------------
#46:37
#FINDALL
#Just return only matches as a list of strings
#If groups are there this only matches group  (Mr|Mrs|Ms)
pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*')
matches = pattern.findall(text_to_search)
print(matches)
#['Mr', 'Mr', 'Ms', 'Mrs', 'Mr']


#Multiple groups will be returned as a list of tuples. Tuples will contain all of groups
pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s([A-Z]\w*)')
matches = pattern.findall(text_to_search)
print(matches)
#[('Mr', 'Schafer'), ('Mr', 'Smith'), ('Ms', 'Davis'), ('Mrs', 'Robinson'), ('Mr', 'T')]

#If no groups all match will print as List of strings
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.findall(text_to_search)
print(matches)
#['321-555-4321', '123.555.1234', '123*555*1234', '800-555-1234', '900-555-1234']
------------------------------------------------------------------------------
                                  #MATCH
#48:00
#match at beginning
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'Start')
matches = pattern.match(sentence)
print(matches) #<re.Match object; span=(0, 5), match='Start'>
------------------------------------------------------------------------------
                                 #SEARCH
#search at beginning
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'sentence')
matches = pattern.search(sentence)
print(matches) #<re.Match object; span=(8, 16), match='sentence'>

pattern = re.compile(r'dne')
matches = pattern.search(sentence)
print(matches) #None


#Flags
#50:10
pattern = re.compile(r'sTaRt', re.IGNORECASE)
pattern = re.compile(r'sTaRt', re.I)
matches = pattern.search(sentence)
print(matches) #<re.Match object; span=(0, 5), match='Start'>
------------------------------------------------------------------------------