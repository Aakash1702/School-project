<html>
<body>
    <h2>{{course_name}}</h2>
    <h3>Instructor: {{instructor}}</h3>

    <h3>Students Enrolled:</h3>
    <ul>
        % for student in students:
            <li>{{student['StudentName']}}</li>
        % end
    </ul>
</body>
</html>
