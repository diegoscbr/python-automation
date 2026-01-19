import re

joke = "I remixed a remix, it was back to normal."
match = re.search('remix', joke)
if match is not None:
    print("we found a remix")
else:
    print("no remix")

print("the match is", match.group())