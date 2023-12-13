<html>
<body>
<h2>Update Student</h2>
<form action="/update_student" method="post">
    <input type="hidden" name="student_id" value="{{student['StudentId']}}">
    Student Name: <input type="text" name="student_name" value="{{student['StudentName']}}"><br>
    Enrolled Course ID: <input type="text" name="enrolled_course_id" value="{{student['EnrolledCourseId']}}"><br>
    <input type="submit" value="Update Student">
</form>
</body>
</html>
