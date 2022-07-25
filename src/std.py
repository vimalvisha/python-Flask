from flask import  Flask, abort, jsonify, request
from flask_cors import cross_origin,CORS
from postgres import db,Pet
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost/flaskql"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = '1234'


CORS(app)


@cross_origin()
@app.route('/pets', methods = ['POST'])
def create_pet():
    pet_data = request.json

    pet_name = pet_data['pet_name']
    pet_age = pet_data['pet_age']
    pet_description = pet_data['pet_description']
    pet = Pet(pet_name = pet_name , pet_age = pet_age, pet_description = pet_description )
    db.session.add(pet)
    db.session.commit()
    

    return jsonify({"success": True,"response":"Pet added"})

@app.route("/pets/<string:data>", methods = ['GET'])
def get_petname(data):
    getPets = []
    apets = Pet.query.filter_by(pet_description =data)

    for pet in apets:
        result = {
            "pet_id": pet.id,
            "pet_name": pet.pet_name,
            "pet_age": pet.pet_age,
            "pet_description": pet.pet_description,
        }
        getPets.append(result)
    
    if len(getPets) < 1:
        return jsonify({'message': 'Not FOUND'})
    else:
        return jsonify({
            "pets":getPets,
            "Success":True,
        
    })

    

    


@app.route('/pets', methods = ['GET'])
def getPets():
    allPets = []
    pets = Pet.query.all()

    for pet in pets:
        results = {
            "pet_id": pet.id,
            "pet_name": pet.pet_name,
            "pet_age": pet.pet_age,
            "pet_description": pet.pet_description,

        }

        allPets.append(results)

    return jsonify(
            {
                "success": True,
                "pets": allPets,
                "total_pets": len(pets),
            }
        )   

@app.route("/pets/<int:pet_id>", methods = ["PATCH"])
def UpdatePets(pet_id):
    pet = Pet.query.get(pet_id) 
    pet_age = request.json['pet_age']
    pet_description = request.json['pet_description']

    if Pet is None:
        abort(404)
    else:
        pet.pet_age = pet_age
        pet.pet_description = pet_description
        db.session.add(pet)
        db.session.commit()
        return jsonify({"success": True, "response": "Pet Details updated"})

@app.route("/pets/<int:pet_id>", methods=["DELETE"])
def pet_delete(pet_id):
    pet = Pet.query.get(pet_id)
    db.session.delete(pet)
    db.session.commit()

    return jsonify({"success": True, "response": "Pet Details deleted"})

app.debug = True
db.init_app(app)
if __name__ == '__main__':
    db.create_all()
    app.run()


