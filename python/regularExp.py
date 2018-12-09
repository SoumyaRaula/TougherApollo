import re

text_to_search = '''
Contrary to popular belief, Lorem Ipsum is not simply random text. 
It has roots in a piece of classical Latin literature from 45 BC,
 making it over 2000 years old. Richard McClintock, a
  Latin professor at Hampden-Sydney College in Virginia, 
  looked up one of the more obscure Latin words, consectetur, 
  from a Lorem Ipsum passage, and going through the cites of the 
  word in classical literature, discovered the undoubtable source. 
  Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum"
   (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics,
    very popular during the Renaissance. The first line of Lorem Ipsum,
     "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
    www.google.com
    <h1> Hello <\h1>
    123-1222-123
    12.232.121
212.255.23.22
Fi FiFi
soumya.raula@gmail.com
'''

pattern = re.compile(r'ab')
matches = pattern.finditer(text_to_search)

for match in matches:
	print(match.span())
	print(text_to_search[match.span()[0]:match.span()[1]])

#^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$

#pattern = re.compile(r'\d{2,4}[-.]\d{2,4}[-.]\d{2,4}')
#pattern = re.compile(r'<[^>]*>')
#pattern = re.compile(r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
#pattern = re.compile(r'[a-zA-z.]+@[a-zA-Z-]+\.(com|edu)')

matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)