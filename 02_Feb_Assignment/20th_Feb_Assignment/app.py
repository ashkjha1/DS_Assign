from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/welcome", methods = ['POST'])
def welcome():
    if (request.method == 'POST'):
        name = request.form['student_name'] 
        course = request.form['course_name']
        loc = request.form['location']
        
        result = "Hi " + str(name) + " from " + str(loc) + " your enrolled course is " + str(course)
        return render_template('results.html' , result = result)

@app.route("/welcome_postman", methods = ['POST'])
def welcome_postman():

    if (request.method == 'POST'):
        name = request.json['student_name']
        course = request.json['course_name']
        loc = request.json['location']

    result = "Hi " + str(name) + " from " + str(loc) + " your enrolled course is " + str(course)

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")