<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }

        .content {
            text-align: center;
        }

        table {
            margin-top: 20px;
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }

        a {
            text-decoration: none;
            color: blue;
        }
    </style>
</head>
<body>
    <div class="content">
        <h2>List of Students</h2>
        <a href="/add_student">Add New Student</a>
        <a href="/course_students" style="margin-left: 20px;">Course Students</a>
        <table border="1">
            <tr>
                <th>Student ID</th>
                <th>Student Name</th>
                <th>Enrolled Course ID</th>
                <th>Actions</th>
            </tr>
            % for student in students:
                <tr>
                    <td>{{student['StudentId']}}</td>
                    <td>{{student['StudentName']}}</td>
                    <td>{{student['EnrolledCourseId']}}</td>
                    <td>
                        <a href="/update_student/{{student['StudentId']}}">Update</a> 
                        <a href="/delete_student/{{student['StudentId']}}">Delete</a>
                    </td>
                </tr>
            % end
        </table>
    </div>
</body>
</html>
