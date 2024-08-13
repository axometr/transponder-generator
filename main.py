import random

# squawk codes can only have digits 0-7 in them
digits = "01234567"
transCode = ""
# index the generator codes as to not regenerate
generatedCodes = []
# ICAO emergency codes
forbiddenCodes = [7500, 7600, 7700]


for i in range(0,4):
    randDigit = random.choice(digits)
    transCode += randDigit