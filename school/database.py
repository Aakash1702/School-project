from pymongo import MongoClient

mongo_connection_string = "mongodb+srv://Aakash_17:Aakash2002@adds.w2f7rr6.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(mongo_connection_string)
db = client['school_database']

courses_collection = db['Courses']
students_collection = db['Students']

def get_courses():
    return list(courses_collection.find())

def get_course(course_id):
    return courses_collection.find_one({"CourseId": course_id})

def add_course(course_data):
    courses_collection.insert_one(course_data)

def update_course(course_id, course_data):
    courses_collection.update_one({"CourseId": course_id}, {"$set": course_data})

def delete_course(course_id):
    courses_collection.delete_one({"CourseId": course_id})


def get_students():
    return list(students_collection.find())

def get_student(student_id):
    return students_collection.find_one({"StudentId": student_id})

def add_student(student_data):
    student_data['EnrolledCourseId'] = int(student_data['EnrolledCourseId'])
    students_collection.insert_one(student_data)

def update_student(student_id, student_data):
    students_collection.update_one({"StudentId": student_id}, {"$set": student_data})

def delete_student(student_id):
    students_collection.delete_one({"StudentId": student_id})
