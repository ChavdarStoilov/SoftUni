from project.student import Student

import unittest

class TestStudent(unittest.TestCase):
    NAME = 'Jonny'

    def test__init(self):
        student = Student(self.NAME)

        actual_name = student.name
        actual_courses = student.courses

        expect_name = self.NAME
        expect_courses = {}

        self.assertEqual(expect_name, actual_name)
        self.assertEqual(expect_courses, actual_courses)

    def test__enroll_course_to_student(self):
        student = Student(self.NAME)

        actual_add_new = student.enroll('Python', 'Note', 'N')
        actual_added_course = student.courses['Python']

        self.assertEqual('Course has been added.', actual_add_new)
        self.assertEqual([], actual_added_course)

        actual_update_course_note = student.enroll('Python', 'Note', '')
        self.assertEqual('Course already added. Notes have been updated.', actual_update_course_note)

        actual_add_course_and_note = student.enroll('Java', ['Note'], 'Y')
        self.assertEqual('Course and course notes have been added.', actual_add_course_and_note)


    def test__adding_note(self):
        student = Student(self.NAME)

        student.enroll('Java', ['Note'], '')
        actual_adding_note = student.add_notes('Java', 'JS')
        actual_added_note = student.courses['Java']

        self.assertEqual('Notes have been updated', actual_adding_note)
        self.assertEqual(['Note', 'JS'], actual_added_note)

        with self.assertRaises(Exception) as ex:
            student.add_notes('Python', 'Django')

        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test__leaving_course_from_student(self):
        student = Student(self.NAME)

        student.enroll('Java', 'Note', 'N')
        actual_leave_course = student.leave_course('Java')

        self.assertEqual('Course has been removed', actual_leave_course)

        with self.assertRaises(Exception) as ex:
            student.leave_course('Python')

        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))




if __name__ == '__main__':
    unittest.main()