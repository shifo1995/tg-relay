   import os
   import requests
   from flask import Flask, request, abort

   TOKEN   = os.environ["BOT_TOKEN"]
   CHAT_ID = os.environ["CHAT_ID"]
   SECRET  = os.environ["SECRET"]

   app = Flask(__name__)

   @app.route("/")
   def home():
       return "running"

   @app.route("/webhook", methods=["POST"])
   def webhook():
       if request.args.get("key") != SECRET:
           abort(403)
       text = request.get_data(as_text=True).strip()
       if not text:
           return "empty", 400
       r = requests.post(
           f"https://api.telegram.org/bot{TOKEN}/sendMessage",
           json={"chat_id": CHAT_ID, "text": text},
           timeout=10,
       )
       return ("ok", 200) if r.ok else (r.text, 500)
