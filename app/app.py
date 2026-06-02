from flask import Flask, request, jsonify
import redis
import os
app = Flask(__name__)

#redis config
r = redis.Redis(
	host=os.getenv("REDIS_HOST", "redis"),
	port=int(os.getenv("REDIS_PORT", "6379")),
	decode_responses=True	
)


#counter endpoint
@app.route('/')
def home():
	visits = r.incr("visits")
	
	return jsonify({
		"message": "Backend is running.",
		"visits": visits
	})


#set message
@app.route("/message", methods=["POST"])
def set_message():
	data = request.get_json()
	
	if not data or "message" not in data:
		return jsonify({
			"error": "message field is required"
		}), 400
	
	r.set("message", data["message"])

	return jsonify({
		"status": "saved",
		"message": data["message"]
	})


#read message
@app.route("/message", methods=["GET"])
def get_message():
	message = r.get("message")

	return jsonify({
		"message": message
	})


if __name__ == "__main__":
	app.run("0.0.0.0", 5000)
