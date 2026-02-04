import re

text = 'The event will take place on 12/21/2002 and 11/13/20222 and 12/30/2025'
pattern =  r'(\d{2})/(\d{2})/(\d{4})'

formatted_text = re.sub(pattern, r'\3-\1-\2', text)
print(formatted_text)