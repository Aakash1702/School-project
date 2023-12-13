<html>
<body>
<h2>Update Course</h2>
<form action="/update_course" method="post">
    <input type="hidden" name="course_id" value="{{course['CourseId']}}">
    Course Name: <input type="text" name="course_name" value="{{course['CourseName']}}"><br>
    Instructor Name: <input type="text" name="instructor_name" value="{{course['InstructorName']}}"><br>
    Instructor ID: <input type="text" name="instructor_id" value="{{course['InstructorID']}}"><br>
    <input type="submit" value="Update Course">
</form>
</body>
</html>
