from flask import  Flask,jsonify, request
from flask_cors import cross_origin,CORS
from postgres import db,Student



std = Flask(__name__)
std.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost/flaskql"
std.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
std.secret_key = '1234'


CORS(std)


@cross_origin()
@std.route('/students', methods = ['POST'])
def create_student():

    data = request.json
    Full_Name = data['Full_Name']
    Mobile_No = data['Mobile_No']
    Reg_No = data['Reg_No']
    Branch = data['Branch']
    student = Student(Full_Name = Full_Name , Mobile_No = Mobile_No, Reg_No = Reg_No, Branch = Branch)
    db.session.add(student)
    db.session.commit()
    

    return jsonify({"success": True,"response":"Student added"})


@std.route("/students", methods = ['GET'])
def get_student_name():
    getStudent = []
    students = Student.query.all()

    for student in students:
        result = {
            "student_id": student.id,
            "student_Full_name": student.Full_Name,
            "student_Mobile_No": student.Mobile_No,
            "student_Reg_No": student.Reg_No,
            "student_Branch" : student.Branch,
            "student_date_Created": student.Date_Created,
        }
        getStudent.append(result)
    
    if len(getStudent) < 1:
        return jsonify({'message': 'Not FOUND'})
    else:
        return jsonify({
            "pets":getStudent,
            "Success":True,
        
    })


# r = requests.get("http://127.0.0.1:5000/students")
# j=r.json()
# print(j)






std.debug = True
db.init_app(std)
if __name__ == '__main__':
    db.create_all()
    std.run()
