from bottle import route, run, template, request, redirect, post
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Aakash_17:Aakash2002@adds.w2f7rr6.mongodb.net/?retryWrites=true&w=majority")
db = client["school_database"]

def get_courses():
    return list(db['Courses'].find())

def get_course(course_id):
    return db['Courses'].find_one({"CourseId": int(course_id)})

def add_course(course_data):
    db['Courses'].insert_one(course_data)

def update_course(course_id, course_data):
    db['Courses'].update_one({"CourseId": int(course_id)}, {"$set": course_data})

def delete_course(course_id):
    db['Courses'].delete_one({"CourseId": int(course_id)})

def get_students():
    return list(db['Students'].find())

def get_student(student_id):
    return db['Students'].find_one({"StudentId": int(student_id)})

def add_student(student_data):
    db['Students'].insert_one(student_data)

def update_student(student_id, student_data):
    db['Students'].update_one({"StudentId": int(student_id)}, {"$set": student_data})

def delete_student(student_id):
    db['Students'].delete_one({"StudentId": int(student_id)})


@route("/course_students")
def course_students():
    courses = get_courses()
    students = get_students()

    course_student_data = []
    for course in courses:
        enrolled_students = [student for student in students if student["EnrolledCourseId"] == course["CourseId"]]
        student_names = ", ".join(student["StudentName"] for student in enrolled_students)
        course_student_data.append({"CourseName": course["CourseName"], "StudentCount": len(enrolled_students), "StudentNames": student_names})

    return template("course_students.tpl", course_student_data=course_student_data)


@route('/search_course')
def search_course():
    search_query = request.query.search.strip()
    courses = get_courses()

    if search_query:
        filtered_courses = [course for course in courses if search_query.lower() in course['CourseName'].lower()]
        if filtered_courses:
            course_id = filtered_courses[0]['CourseId']
            instructor = filtered_courses[0]['InstructorName']
            enrolled_students = [student for student in get_students() if student['EnrolledCourseId'] == course_id]
            return template('search_course.tpl', course_name=search_query, instructor=instructor, students=enrolled_students)
        else:
            return "No matching course found."
    else:
        return "Please enter a search query."


@route('/')
def index():
    return template('index.tpl')

@route("/")
def get_index():
    redirect("/list_courses")

@route("/list_courses")
def list_courses():
    courses = get_courses()
    return template("list_courses.tpl", courses=courses)

@route("/add_course")
def get_add_course():
    return template("add_course.tpl")

@post("/add_course")
def post_add_course():
    course_id = request.forms.get("course_id")
    course_name = request.forms.get("course_name")
    instructor_name = request.forms.get("instructor_name")
    instructor_id = request.forms.get("instructor_id")
    add_course({"CourseId": int(course_id), "CourseName": course_name, "InstructorName": instructor_name, "InstructorID": instructor_id})
    redirect("/list_courses")

@route("/update_course/<id>")
def get_update_course(id):
    course = get_course(id)
    return template("update_course.tpl", course=course)

@post("/update_course")
def post_update_course():
    course_id = request.forms.get("course_id")
    course_name = request.forms.get("course_name")
    instructor_name = request.forms.get("instructor_name")
    instructor_id = request.forms.get("instructor_id")
    update_course(course_id, {"CourseName": course_name, "InstructorName": instructor_name, "InstructorID": instructor_id})
    redirect("/list_courses")

@route("/delete_course/<id>")
def delete_course_route(id):
    delete_course(id)
    redirect("/list_courses")

@route("/list_students")
def list_students():
    students = get_students()
    return template("list_students.tpl", students=students)

@route("/add_student")
def get_add_student():
    return template("add_student.tpl")

@post("/add_student")
def post_add_student():
    student_id = request.forms.get("student_id")
    student_name = request.forms.get("student_name")
    # enrolled_course_id = request.forms.get("enrolled_course_id")
    enrolled_course_id = int(request.forms.get("enrolled_course_id"))
    add_student({"StudentId": int(student_id), "StudentName": student_name, "EnrolledCourseId": enrolled_course_id})
    redirect("/list_students")

@route("/update_student/<id>")
def get_update_student(id):
    student = get_student(id)
    return template("update_student.tpl", student=student)

@post("/update_student")
def post_update_student():
    student_id = request.forms.get("student_id")
    student_name = request.forms.get("student_name")
    # enrolled_course_id = request.forms.get("enrolled_course_id")
    enrolled_course_id = int(request.forms.get("enrolled_course_id"))
    update_student(student_id, {"StudentName": student_name, "EnrolledCourseId": enrolled_course_id})
    redirect("/list_students")

@route("/delete_student/<id>")
def delete_student_route(id):
    delete_student(id)
    redirect("/list_students")

run(host='localhost', port=8080, reloader=True)
