from flask import flask
app =flask(_name_)
@app.route("/")
def home():
  return "Hello frome Docker!MY first container is running."
  if_name_=="_main_":
  app.run(host="0.0.0.0",port=5000)
