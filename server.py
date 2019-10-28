from flask import Flask

app = Flak(__name__)

@app.route("/")
def hello():
  return "Ratas"

if __name__ = "__main__":
  app.run(host="0.0.0.0",port=80)
