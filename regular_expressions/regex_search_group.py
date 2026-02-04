import re

pattern = r"(\w+) (\d{1,2}), (\d{4})"
test = "Some years ago I was born on July 26, 2001"
match = re.search(pattern, test)
if match is not None:
    print(match.group(3))
else:
    print("No match")

#findall_method
pattern_year = r'\d{4}'
test_string = '''The Snipe class sailboat was designed in 1931 by William Crosby, making it one of the oldest and most successful one-design racing classes in the world. Crosby created the Snipe as an affordable, small boat that could be built by amateur builders during the Great Depression. The original design called for a 15.5-foot hard-chine hull that was simple to construct from plywood.
The Snipe Class International Racing Association (SCIRA) was founded in 1932, just one year after the boat's creation, and quickly grew into a global organization. By the 1940s, Snipe fleets had spread across North and South America, Europe, and beyond. The class became particularly popular in countries like Brazil, Spain, Portugal, and Japan, where it remains a premier racing class to this day.
Throughout its history, the Snipe has undergone modest updates while maintaining its fundamental character as a tactical two-person dinghy. The boat features a mainsail and jib configuration, requiring precise teamwork between skipper and crew. Its relatively flat hull and responsive handling make it an excellent platform for learning racing tactics and boat-on-boat competition.
The Snipe World Championship has been held annually since 1934, making it one of the longest-running sailing world championships. Legendary sailors from around the globe have competed in the class, and winning a Snipe World Championship is considered a significant achievement in the sailing community. The class continues to thrive with active fleets in over 30 countries and thousands of registered boats worldwide.'''
years = re.findall(pattern_year, test_string)
print(years)


#complex findall example
pat = "meo*"
text = 'woof woof bark bark meow meow purrrr hisss chirp chirp tweet tweet squawk polly want a cracker bawk bawk cluck cluck moo wait thats not a pet neigh neigh okay maybe a horse ribbit ribbit croak splash splash blub blub glub glub squeak squeak wheek wheek thats a guinea pig oink oink some people have pet pigs hisssss rattle rattle thats a snake growl growl ruff ruff yip yip howoooo arf arf mrrrow prrrrp thats a cat trill chirrup chirrup budgie sounds psittacine screaming cockatoo AAAAHHH hamster wheel spinning squeakily thump thump rabbit foot gecko clicking bark bark bark the dog again meow feed me human purr purr knead knead slow blink hoot hoot screech owl sounds coo coo pigeon flutter flutter wing flaps splash betta fish bubble nest blorp tropical fish tank humming hermit crab clicking clack clack ferret dook dook dook chatter chatter chinchilla bark guinea pig rumblestrut purring'
sounds = re.findall(pat, text)
print(sounds)