import json
import pytest
import unittest
import System
import Student
import User
import Professor
import TA
import Staff
import ast

@pytest.fixture
def sys1():
    testSystem = System.System()
    testSystem.load_data()
    return testSystem
      
"""
### 1. login - System.py

The login function takes a name and password and sets the user for the program. Verify
that the correct user is created with this test, and use the json files to check that 
it adds the correct data to the user.
"""
def test_login(sys1):
    name = "muna"
    passcode = "14321"
    try:
        assert sys1.users[name]['password'] == passcode
    except KeyError:
        data = {
            name: {
                "courses": {}, 
                "password": passcode,
                "role": "student"
            }
        }
        sys1.users.update(data)

"""
2. check_password - System.py

This function checks that the password is correct. Enter several different 
formats of passwords to verify that the password returns correctly if the passwords 
are the same.
"""
def test_check_password(sys1):
    name = "saab"
    passcode = "boomr345"
    assert sys1.users[name]['password'] == passcode

"""
3. change_grade - Staff.py

This function will change the grade of a student and updates the database. 
Verify that the correct grade is changed on the correct user in the database.
"""
def test_change_grade(sys1):
    ta = TA.TA("cmhbf5",sys1.users,sys1.courses)
    name = "hdjsr7"
    course = "cloud_computing"
    assignment = "assignment1"
    ta.change_grade(name,course,assignment,"80")
    sys1.update_users_db()

"""
4. create_assignment Staff.py

This function allows the staff to create a new assignment. Verify that an 
assignment is created with the correct due date in the correct course in the 
database.
"""
def test_create_assignment(sys1):
    prof = Professor.Professor("calyam",sys1.users,sys1.courses)
    course = "cloud_computing"
    assignment_name = "assignment3"
    due_date = "03/21/21"
    prof.create_assignment(assignment_name,due_date,course)
    sys1.update_courses_db()

"""
5. add_student - Professor.py

This function allows the professor to add a student to a course. Verify that a 
student will be added to the correct course in the database.
"""
def test_add_student(sys1):
    prof_name = "goggins"
    prof = Professor.Professor(prof_name,sys1.users,sys1.courses)
    name = "yted91"
    course_name = "databases"
    prof.add_student(name,course_name)
    sys1.update_users_db()

"""
6. drop_student Professor.py

This function allows the professor to drop a student in a course. Verify that the 
student is added and dropped from the correct course in the database.
"""
def test_drop_student(sys1):
    prof = Professor.Professor("goggins",sys1.users,sys1.courses)
    name = "akend3"
    course = "software_engineering"
    prof.drop_student(name,course)
    sys1.update_users_db()

"""
7. submit_assignment - Student.py

This function allows a student to submit an assignment. Verify that the database is 
updated with the correct assignment, submission, submission dateand in the correct course.
"""
def test_submit_assignment(sys1):
    student_name = "yted91"
    student = Student.Student(student_name,sys1.users,sys1.courses)
    course = "software_engineering"
    assignment_name = "assignment2"
    submission = "Blah Blah Blah"
    submission_date = "04/02/20"
    student.submit_assignment(course,assignment_name,submission,submission_date)

"""
8. check_ontime - Student.py

This function checks if an assignment is submitted on time. Verify that it will return true 
if the assignment is on time, and false if the assignment is late.
"""
def test_check_ontime(sys1):
    student_name = "yted91"
    student = Student.Student(student_name,sys1.users,sys1.courses)
    submission_date = "04/02/20"
    due_date = "07/11/20"
    assert student.check_ontime(submission_date,due_date)

"""
### 9. check_grades - Student.py

This function returns the users grades for a specific course. Verify the correct grades
 are returned for the correct user.
"""
def test_check_grades(sys1):
    student = Student.Student("akend3",sys1.users,sys1.courses)
    student.check_grades("databases")


"""
### 10. view_assignments - Student.py

This function returns assignments and their due dates for a specific course. Verify that 
the correct assignments for the correct course are returned.
"""
def test_view_assignments(sys1):
    user = "hdjsr7"
    student = Student.Student(user,sys1.users,sys1.courses)
    classes = sys1.users[user]['courses']
    assignments = []
    for key in classes:
        assignments = student.view_assignments(key)
        verify = sys1.courses[key]['assignments']
        for hw in assignments:
            assert hw[0] in verify.keys()

"""
11. drop_course - Student.py

This function allows the student to drop a course.
"""
def test_drop_course(sys1):
    name = "yted91"
    course_name = "comp_sci"
    student = Student.Student(name,sys1.users,sys1.courses)
    student.drop_course(course_name)
    sys1.update_users_db()

"""
12. remove_assignment - Staff.py

This function allows the staff to remove any assignment. 
"""
def test_remove_assignment(sys1):
    prof = Professor.Professor("calyam",sys1.users,sys1.courses)
    course = "cloud_computing"
    assignment_name = "assignment3"
    due_date = "03/21/21"
    prof.remove_assignment(course,assignment_name)
    sys1.update_courses_db()

"""
13. check_student - Staff.py

This function allows the staff to search students in a course.
"""
def test_check_student(sys1):
    prof = Professor.Professor("calyam",sys1.users,sys1.courses)
    course = "cloud_computing"
    name = "yted91" 
    assert prof.check_student(name,course)
    sys1.update_courses_db()

"""
14. extend_deadline - Staff.py

This function allows Staff to postpone the deadline of an assignment. If the assignment
does not exist, it is then created
"""
def test_extend_deadline(sys1):
    prof = Professor.Professor("calyam",sys1.users,sys1.courses)
    course = "web_dev"
    prof.extend_deadline(course,"assignment2","04/11/20")
    sys1.update_courses_db()


"""
15. check_course - Student.py

This function allows the student to search for the course they are enrolled in.
"""
def test_check_course(sys1):
    name = "yted91"
    course_name = "comp_sci"
    student = Student.Student(name,sys1.users,sys1.courses)
    student.check_course(course_name)