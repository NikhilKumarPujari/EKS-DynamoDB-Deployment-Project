from flask import Flask, request, jsonify,send_from_directory
import boto3
from flask_cors import CORS
import uuid
app = Flask(__name__)
CORS(app)

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1'
)

table = dynamodb.Table('users')

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")
@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    user_id = str(uuid.uuid4())

    table.put_item(
        Item={
            'id': user_id,
            'name': data['name'],
            'email': data['email']
        }
    )

    return jsonify({"message": "User added"})


@app.route('/get', methods=['GET'])
def get_users():
    response = table.scan()
    return jsonify(response['Items'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
