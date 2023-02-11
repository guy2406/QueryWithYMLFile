# app.py

from flask import render_template # Remove: import Flask
import connexion
import data


app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html",HEADERS = data.get_headers())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)