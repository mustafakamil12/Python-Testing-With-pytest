from students import Student
import pytest

class TestStudent:
    @classmethod
    def setup_class(cls):
        cls.student = Student("Mustafa","Al Ogaidi","Computer Engineering",44,"AI",1)
    def test_full_name(self):
        result = self.student.full_name()
        assert result == "Mustafa Al Ogaidi"

    def test_student_info(self):
        result = self.student.student_info()
        assert result == "Mustafa Al Ogaidi is 44 years old and studies AI"

    @classmethod
    def teardown_class(cls):
        print("Tearing down")