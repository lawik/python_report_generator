import base64
import sys

data = ''
with open(sys.argv[1]) as f:
    for line in f:
        data += line

insert = base64.b64encode(data)

program = ''
with open('template.py') as f:
    for line in f:
        program += line

program = program.replace('PLACEHOLDER', insert)
print program
