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

def rawCode():
    transCode = ""
    for _ in range(4):
        randDigit = random.choice(digits)
        transCode += randDigit
    return transCode

def generateCode():
    while True:
        transCode = rawCode()
        if transCode not in generatedCodes and transCode not in forbiddenCodes:
            generatedCodes.append(transCode)
            return transCode
    
    
@app.route("/")
def index():
    flaskCode = generateCode()
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transponder code generator</title>
    <style>
        html {
            font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 300%;
            text-align: center;
            line-height: 50%;
            margin-top: 30vh;
        }

        .transponder-code-p {
            font-size: 150%;
            font-weight: bold;
        }
                                  
        .button {
            background-color: #eb4034;
            color: white;
            padding: 15px 32px;
            text-align: center;
            display: inline-block;
            font-size: 16px;
            border: none;
            cursor: pointer;
            border-radius: 10px;
        }
                                  
        .button:hover {
            background-color: #c22217;
        }
    </style>
</head>
<body>
    <div>Transponder code:</div>
    <p class="transponder-code-p" id="transponder-code-p">{{ code }}</p>
    <button class="button" id="regenerate-button">Generate New Code</button>
    <script>
        document.getElementById("regenerate-button").addEventListener("click", function() {
            fetch("/regenerate").then(response => response.text())
            .then(code => {
                document.getElementById("transponder-code-p").textContent = code;
            });
        });
    </script>
</body>
</html>
''', code = flaskCode)

# if we get a request via the Flask button, then call the generate function again and return its output
@app.route("/regenerate")
def regenerateCode():
    return(generateCode())

if __name__ == '__main__':
    app.run(debug=True)