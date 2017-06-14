import time
import base64
import sys
import random
import string

content = """PLACEHOLDER"""

special_cases = {
    ".":    0.3,
    "\n":   0.4,
    ",":    0.2,
}

ascii_chars = range(65, 91)
ascii_chars.extend(range(97, 123))

chance_of_error = 10
error_size_limit = 5

speedfactor = 1.0
if len(sys.argv) > 1:
    try:
        speedfactor = float(sys.argv[1])
    except:
        pass

data = base64.b64decode(content)

def prnt(text):
    sys.stdout.write(text.encode('utf-8'))
    sys.stdout.flush()

for index, char in enumerate(unicode(data,"utf-8")):
    # print ord(char)
    if ord(char) in ascii_chars and random.randint(1, chance_of_error) == chance_of_error:
        error_size = random.randint(1, 3)
        # print "Error size: %s" % error_size
        for num in range(0, error_size):
            # print "\nfudging"
            prnt(chr(random.choice(ascii_chars)))
            time.sleep(0.1*speedfactor)
        for num in range(0, error_size):
            # print "\nbackspacing"
            prnt("\b")
            time.sleep(0.1*speedfactor)

    if char in special_cases:
        time.sleep(special_cases[char]*speedfactor)
    else:
        time.sleep(0.1*speedfactor)
    prnt(char)
