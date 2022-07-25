from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
import psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
 
DB_HOST = "localhost"
DB_NAME = "flaskql"
DB_USER = "postgres"
DB_PASS = "1234"
     
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)  
 
# @app.route('/')
# class Pet(db.Model):
#     __tablename__ = 'pets'
#     id = db.Column(db.Integer, primary_key = True)
#     pet_name = db. Column(db.String(100), nullable = False)
#     pet_age = db.Column(db.Integer(), nullable = False)
#     pet_description = db.Column(db.String(100), nullable = False)


#     def __repr__(self):
#         return "<Pet %r>" % self.pet_name
 
@app.route('/pets') 
def get_pets():
    try:
        id = request.args.get('pet_id')
        if id:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute("SELECT * FROM pets WHERE id=%s", id)
            row = cursor.fetchone()
            resp = jsonify(row)
            resp.status_code = 200
            return resp
        else:
            resp = jsonify('Pet "id" not found in query string')
            resp.status_code = 500
            return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
 
if __name__ == "__main__":
    app.run()
