from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from lab11.main.models.pencil import Pencil
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SmartPencil(Pencil, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price_in_hryvnia = db.Column(db.Float, unique=False)
    color = db.Column(db.String(32), unique=False)
    producer = db.Column(db.String(32), unique=False)
    target_age = db.Column(db.Integer, unique=False)
    hardeness_of_slate = db.Column(db.String(32), unique=False)

    def __init__(self, price_in_hryvnia=0.0, color='N/A', producer='N/A', target_age=0, hardeness_of_slate='N/A'):
        super().__init__(price_in_hryvnia, color, producer, target_age, hardeness_of_slate)


class SmartPencilSchema(ma.Schema):
    class Meta:
        fields = ('price_in_hryvnia', 'color', 'producer', 'target_age', 'hardeness_of_slate')


smart_pencil_schema = SmartPencilSchema()
smart_pencils_schema = SmartPencilSchema(many=True)


@app.route("/smart_pencil", methods=["POST"])
def add_smart_pencil():
    smart_pencil = SmartPencil(request.json['price_in_hryvnia'],
                               request.json['color'],
                               request.json['producer'],
                               request.json['target_age'],
                               request.json['hardeness_of_slate'])
    db.session.add(smart_pencil)
    db.session.commit()
    return smart_pencil_schema.jsonify(smart_pencil)


@app.route("/smart_pencil", methods=["GET"])
def get_smart_pencil():
    all_smart_pencil = SmartPencil.query.all()
    result = smart_pencils_schema.dump(all_smart_pencil)
    return jsonify({'smart_pencil': result})


@app.route("/smart_pencil/<id>", methods=["GET"])
def get_smart_pencil_detail(id):
    smart_pencil = SmartPencil.query.get(id)
    if not smart_pencil:
        abort(404)
    return smart_pencil_schema.jsonify(smart_pencil)


@app.route("/smart_pencil/<id>", methods=["PUT"])
def put_smart_stationery(id):
    smart_pencil = SmartPencil.query.get(id)
    if not smart_pencil:
        abort(404)
    old_smart_pencil = copy.deepcopy(smart_pencil)
    smart_pencil.price_in_hryvnia = request.json['price_in_hryvnia']
    smart_pencil.color = request.json['color']
    smart_pencil.producer = request.json['producer']
    smart_pencil.target_age = request.json['target_age']
    smart_pencil.hardeness_of_slate = request.json['hardeness_of_slate']
    db.session.commit()
    return smart_pencil_schema.jsonify(old_smart_pencil)


@app.route("/smart_pencil/<id>", methods=["DELETE"])
def delete_smart_pencil(id):
    smart_pencil = SmartPencil.query.get(id)
    if not smart_pencil:
        abort(404)
    db.session.delete(smart_pencil)
    db.session.commit()
    return smart_pencil_schema.jsonify(smart_pencil)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
