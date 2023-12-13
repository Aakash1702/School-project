<!DOCTYPE html>
<html>
<head>
    <title>Course Students</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }

        h2 {
            text-align: center;
        }

        table {
            border-collapse: collapse;
            width: 50%; /* Adjust table width as needed */
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h2>Course Students</h2>
    <table>
        <tr>
            <th>Course Name</th>
            <th>Student Count</th>
            <th>Student Names</th>
        </tr>
        % for course_data in course_student_data:
            <tr>
                <td>{{ course_data["CourseName"] }}</td>
                <td>{{ course_data["StudentCount"] }}</td>
                <td>{{ course_data["StudentNames"] }}</td>
            </tr>
        % end
    </table>
</body>
</html>
