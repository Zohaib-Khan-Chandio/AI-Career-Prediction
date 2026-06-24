from flask import Flask, render_template, request, jsonify
import pickle, os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "trained_model.pkl")
with open(MODEL_PATH, "rb") as f:
    bundle = pickle.load(f)
clf     = bundle["clf"]
CLASSES = bundle["classes"]

CAT_MAPS = {
    "Q1": {"Arts / Humanities": 0, "Science with Biology": 1, "Science with Computer Science": 2},
    "Q2": {"FA / Humanities": 0, "FSc Pre-Engineering": 1, "FSc Pre-Medical": 2,
           "I.Com (Commerce)": 3, "ICS (Intermediate in Computer Science)": 4},
    "Q3": {"Below 60% (C Grade or lower)": 0, "60-70% (B Grade)": 1,
           "70-80% (A Grade)": 2, "Above 80% (A-1 Grade)": 3},
    "Q8": {"Short term (1-2 years / diploma / freelance)": 0,
           "Medium term (4-year Bachelor's degree)": 1,
           "Long term (5+ years: MBBS, CA, PhD)": 2},
    "Q9": {"Clinical / Hospital": 0, "Corporate / Desk Job": 1, "Fieldwork / Outdoor": 2},
}

CAREER_ICONS = {
    "Information Technology":     "💻",
    "Medical & Allied Health":    "🏥",
    "Engineering & Architecture": "⚙️",
    "Business & Finance":         "📈",
    "Creative Arts & Media":      "🎨",
    "Social Sciences & Law":      "⚖️",
    "Vocational & Technical":     "🔧",
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    try:
        row = [
            CAT_MAPS["Q1"].get(data["Q1"], 0),
            CAT_MAPS["Q2"].get(data["Q2"], 0),
            CAT_MAPS["Q3"].get(data["Q3"], 0),
            int(data["Q4"]), int(data["Q5"]),
            int(data["Q6"]), int(data["Q7"]),
            CAT_MAPS["Q8"].get(data["Q8"], 0),
            CAT_MAPS["Q9"].get(data["Q9"], 0),
        ]
        pred  = clf.predict([row])[0]
        proba = clf.predict_proba([row])[0]
        top3  = sorted(zip(CLASSES, proba), key=lambda x: -x[1])[:3]
        return jsonify({
            "prediction": pred,
            "icon": CAREER_ICONS.get(pred, "🎓"),
            "top3": [{"career": c, "prob": round(p*100,1),
                      "icon": CAREER_ICONS.get(c,"🎓")} for c,p in top3],
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
