from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv() 
app = Flask(__name__)
CORS(app)

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["board_monitor"]
alerts_collection = db["board_alerts"]

@app.route("/api/alerts", methods=["GET"])
def get_alerts():
    alerts = list(alerts_collection.find({}, {"_id": 0}))
    print("\n===============================")
    print("Fetched Alerts:")
    print("===============================\n")
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
