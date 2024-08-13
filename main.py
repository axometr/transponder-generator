from flask import Flask, render_template_string
import random

app = Flask(__name__)

# squawk codes can only have digits 0-7 in them
digits = "01234567"
transCode = ""
# index the generator codes as to not regenerate
generatedCodes = []
# ICAO emergency codes
forbiddenCodes = [7500, 7600, 7700]

def generateCode():
    transCode = ""
    for _ in range(0,4):
        randDigit = random.choice(digits)
        transCode += randDigit
    if transCode not in generatedCodes or transCode not in forbiddenCodes:
        generatedCodes.append(transCode)
        return transCode