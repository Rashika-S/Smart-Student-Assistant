from flask import Flask, request, jsonify

app = Flask(__name__)

def assistant(user_input):
    user_input = user_input.lower()

    if "exam" in user_input:
        return "Revise key topics, practice questions, and get proper sleep."
    elif "stress" in user_input:
        return "Take a short break, breathe, and focus on one task at a time."
    elif "time" in user_input:
        return "Prioritize tasks using a simple plan: urgent → important → rest."
    else:
        return "Tell me more about your situation so I can help better."

@app.route("/")
def home():
    return "Smart Assistant Running 🚀"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    response = assistant(data["message"])
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
