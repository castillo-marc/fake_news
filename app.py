from flask import Flask, request, render_template, redirect
# from flask_sqlalchemy import SQLAlchemy
import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.decomposition import TruncatedSVD
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from process_text import scraper, clean_text

from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import FunctionTransformer

app = Flask(__name__)

model_path = "models/"

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
sent_embedding_transformer = FunctionTransformer(lambda text: model.encode(text))
xgb_with_bert = pickle.load(open(model_path + "xgb_with_bert.pkl", "rb"))
pipe_bert = Pipeline([("embeddings", sent_embedding_transformer), ("xgb", xgb_with_bert)])

# TODO:
# can have sample links to try
# visualizations: frequency plot, wordcloud
# oh, also a word counter under text box
# also a loading animation after clicking button, if necessary

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["article_text"]
        # url = request.form["article_url"] # couldn't get beautifulsoup to work on too many websites bc of paywalls
        # text = scraper(url)
        text = clean_text(text)
        pred = pipe_bert.predict([text])
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
