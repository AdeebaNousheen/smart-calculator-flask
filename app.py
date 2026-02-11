from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        text = request.form["text"].lower()
        numbers = [int(w) for w in text.split() if w.isdigit()]

        if "add" in text and len(numbers) == 2:
            result = numbers[0] + numbers[1]

        elif "subtract" in text and len(numbers) == 2:
            result = numbers[1] - numbers[0]

        elif "multiply" in text and len(numbers) == 2:
            result = numbers[0] * numbers[1]

        elif "divide" in text and len(numbers) == 2:
            if numbers[1] == 0:
                result = "Cannot divide by zero"
            else:
                result = numbers[0] / numbers[1]

        else:
            result = "Invalid input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
