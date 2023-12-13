<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            display: flex; justify-content: center;
            align-items: center; height: 100vh;
            margin: 0; font-family: Arial, sans-serif;
        }

        .content {
            text-align: center; margin-top: 20px;
        }

        table {
            border-collapse: collapse;
            width: 100%; margin-top: 20px;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px; text-align: left;
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
        <h1>Cleveland High School</h1>
        <div>
            <form action="/search_course" method="GET">
                <input type="text" name="search" placeholder="Search Course...">
                <input type="submit" value="Search">
            </form>
        </div>
        <h2>List of Courses</h2>
        <a href="/add_course">Add New Course</a>
        <a href="/list_students" style="margin-left: 20px;">Students</a>

        <table>
            <tr>
                <th>Course ID</th>
                <th>Course Name</th>
                <th>Instructor Name</th>
                <th>Instructor ID</th>
                <th>Actions</th>
            </tr>
            % for course in courses:
                <tr>
                    <td>{{course['CourseId']}}</td>
                    <td>{{course['CourseName']}}</td>
                    <td>{{course['InstructorName']}}</td>
                    <td>{{course['InstructorID']}}</td>
                    <td>
                        <a href="/update_course/{{course['CourseId']}}">Update</a> |
                        <a href="/delete_course/{{course['CourseId']}}">Delete</a>
                    </td>
                </tr>
            % end
        </table>
    </div>
</body>
</html>
