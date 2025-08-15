import os
from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), 'static'),
    template_folder=os.path.join(os.path.dirname(__file__), 'templates')
)

@app.route("/")
def index():
    return render_template("index.html", nombre="Matías", edad=2)

if __name__ == "__main__":
    app.run(debug=True)
