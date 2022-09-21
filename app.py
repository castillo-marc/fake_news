from flask import Flask, request, render_template, redirect
# from flask_sqlalchemy import SQLAlchemy
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from process_text import scraper, clean_text

app = Flask(__name__)

model_path = "models/"

tfidf = pickle.load(open(model_path + "tfidf_vectorizer.pkl", "rb"))
svd = pickle.load(open(model_path + "svd.pkl", "rb"))
xgb_with_tfidf = pickle.load(open(model_path + "xgb_with_tfidf.pkl", "rb"))

pipe_tfidf = Pipeline([("tfidf", tfidf), ("svd", svd), ("xgb", xgb_with_tfidf)])


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["article_text"]
        # url = request.form["article_url"] # couldn't get beautifulsoup to work on too many websites bc of paywalls
        # text = scraper(url)
        text = clean_text(text)
        pred = pipe_tfidf.predict([text])
        if pred == 1:
            label="Fake"
        else:
            label="Real"

        return render_template("result.html", label=label, text=text)
    else:
        return render_template("index.html")

@app.route("/result/", methods=["GET"])
def result():
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)
