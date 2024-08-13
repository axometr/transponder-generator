from flask import Flask, render_template_string
import random

app = Flask(__name__)

# squawk codes can only have digits 0-7 in them
digits = "01234567"
transCode = ""
# index the generator codes as to not regenerate
generatedCodes = []
# ICAO emergency codes
forbiddenCodes = ["7500", "7600", "7700"]

def generateCode():
    transCode = ""
    for _ in range(0,4):
        randDigit = random.choice(digits)
        transCode += randDigit
    if transCode not in generatedCodes or transCode not in forbiddenCodes:
        generatedCodes.append(transCode)
        return transCode
    
@app.route('/')
def index():
    flaskCode = generateCode()
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transponder code generator</title>
</head>
<body>
    <h1>Transponder code:</h1>
    <p>{{ code }}</p>
    <form action="/" method="get">
        <button type="submit">Generate New Code</button>
    </form>              
</body>
</html>
''', code = flaskCode)