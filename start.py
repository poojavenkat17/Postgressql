from flask import Flask, request, render_template
import psycopg2

from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search_student.html')
    else:
        #------------- Enter SQL code below this line-----------------
        
        #-----------SQL code above this line---------------------
        return render_template('search_results.html', mylist=results)

@app.route('/search_scores', methods=['GET', 'POST'])
def search_scores():
    if request.method == 'GET':
        return render_template('search_scores.html')
    else:
        #------------- Enter SQL code below this line-----------------
        
        #-----------SQL code above this line---------------------
        if len(results) == 0:
            return 'There is no one by that student ID'


    
        else:
            return render_template('score_results.html', mylist=results)


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('add_student.html')
    else:
        studentname = request.form.get('studentname')
        sid = request.form.get('id')
        address = request.form.get('address')
        gender = request.form.get('gender')
        dob = request.form.get('dob')
        chem101 = request.form.get('chem101')
        math101 = request.form.get('math101')
        phys101 = request.form.get('phys101')
        
        if not studentname or not sid:
            return "Name and StudentID are required"
        else:
            sid = int(sid)
    #--------------------SQL code below----------------------------------------------
        
    #--------------------End SQL code ------------------------
        return f"The student {studentname} was created....OK"


@app.route('/courses')
def courses():
    #------------Enter SQL code below--------------


    
    #--------------------End SQL code ------------------------
    return render_template('course_info.html', course_details=all_data)

    

        