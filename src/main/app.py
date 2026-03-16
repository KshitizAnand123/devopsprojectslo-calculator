from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calculate_sli(total_requests, successful_requests):
    if total_requests == 0:
        return 0
    return (successful_requests / total_requests) * 100


@app.route("/")
def home():
     return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.json

    total_requests = data["total_requests"]
    successful_requests = data["successful_requests"]
    slo_target = data["slo_target"]

    sli = calculate_sli(total_requests, successful_requests)

    status = "SLO Achieved" if sli >= slo_target else "SLO Violated"

    return jsonify({
        "SLI": round(sli,2),
        "SLO Target": slo_target,
        "Status": status
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)