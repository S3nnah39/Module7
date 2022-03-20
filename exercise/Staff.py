import json
import User

class Staff(User.User):

    def update_course_db(self):
        with open('Data/courses.json', 'w') as fp:
            json.dump(self.all_courses, fp)

    def create_assignment(self,assignment_name, due_date, course):
        assignment = {
            assignment_name: {
                'due_date': due_date
            }
        }
        self.all_courses[course]['assignments'].update(assignment)
        self.update_course_db()

    def change_grade(self,user,course,assignment,grade):
        self.users[user]['courses'][course][assignment]['grade'] = 0
        self.update_user_db()

    def check_grades(self,name,course):
        assignments = self.users[name]['courses'][course]
        grades = []
        for key in assignments:
            grades.append([key, assignments[key]['grade']])
        return grades

    def remove_assignment(self, course, assignment):
        del self.all_courses[course]['assignments'][assignment]
        self.update_user_db()

    def check_student(self,name,course):
        courseList = self.users[name]['courses']
        if course in courseList:
            return True
        return False

    def extend_deadline(self,course, assignment,new_date):
        courseList = self.all_courses[course]['assignments']
        if assignment in courseList:
            courseList[assignment]['due_date'] = new_date
        else:
            self.create_assignment(assignment,new_date,course)
        self.update_course_db()
