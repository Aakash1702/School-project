from pymongo import MongoClient
mongo_connection_string = "mongodb+srv://Aakash_17:Aakash2002@adds.w2f7rr6.mongodb.net/?retryWrites=true&w=majority"

db = client['school_database']

courses_collection = db['Courses']
students_collection = db['Students']

courses_collection.delete_many({})
students_collection.delete_many({})

courses = [
    {"CourseId": 1, "CourseName": 'Mathematics', "InstructorName": 'Dr. Alice Smith', "InstructorID": 'I100'},
    {"CourseId": 2, "CourseName": 'Physics', "InstructorName": 'Dr. Bob Johnson', "InstructorID": 'I101'},
    {"CourseId": 3, "CourseName": 'Literature', "InstructorName": 'Dr. Carol Williams', "InstructorID": 'I102'}
]
courses_collection.insert_many(courses)

students = [
    {"StudentId": 1, "StudentName": 'John Doe', "EnrolledCourseId": 1},
    {"StudentId": 2, "StudentName": 'Mary Jane', "EnrolledCourseId": 1},
    {"StudentId": 3, "StudentName": 'Alex Brown', "EnrolledCourseId": 1}
]
students_collection.insert_many(students)

print("Database setup completed successfully.")
