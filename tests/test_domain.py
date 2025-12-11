import unittest
from app.models import Student, Subject

class TestStudentAllocation(unittest.TestCase):
    def setUp(self):
        self.adam = Student("001","Adam", "Smith")
        self.john = Student("002","John", "Smith")
        self.edward = Student("003","Edward", "Stepford")
        self.henry = Student("004","Henry", "Jones")
        self.ariel = Student("005","Ariel", "Miller")
        self.ned = Student("006","Ned", "Martin")
        self.emma = Student("007","Emma", "Wilson")
        self.harriet = Student("008","Harriet", "Evans")
        self.april = Student("009","April", "Roberts")
        self.catherine = Student("010","Catherine", "Green")
        self.paul = Student("011","Paul", "Hall")
        self.simon = Student("012","Simon", "Thomas")
        self.penelope = Student("013","Penelope", "Clarke")
        self.eugene = Student("014","Eugene", "Harris")
        self.keith = Student("015","Keith", "Robinson")
        self.anna = Student("016","Anna", "Wright")
        self.rebecca = Student("017","Rebecca", "Thompson")
        self.charlotte = Student("018","Charlotte", "Young")
        self.george = Student("019","George", "Bailey")
        self.greg = Student("020","Greg", "Carter")
        self.jim = Student("021","Jim", "Shaw")
        self.james = Student("022","James", "Mitchell")
        self.french = Subject("French", 20)
        self.german = Subject("German", 20)
        self.french.add(self.jim)
        self.french.add(self.james)
        self.french.add(self.greg)
        self.french.add(self.george)
        self.french.add(self.charlotte)
        self.german.add(self.jim)
        self.german.add(self.james)
        self.german.add(self.greg)
        self.german.add(self.george)
        self.german.add(self.charlotte)
        self.german.add(self.rebecca)
        self.german.add(self.anna)
        self.german.add(self.keith)
        self.german.add(self.eugene)
        self.german.add(self.penelope)
        self.german.add(self.simon)
        self.german.add(self.paul)
        self.german.add(self.catherine)
        self.german.add(self.april)
        self.german.add(self.harriet)
        self.german.add(self.emma)
        self.german.add(self.ned)
        self.german.add(self.ariel)
        self.german.add(self.henry)
        self.german.add(self.edward)


    def test_number_of_students_increases(self):
        self.french.add(self.adam)
        self.assertEqual(self.french.allocated_students, 6)

    def test_class_size_full(self):
        with self.assertRaises(ValueError):
            self.german.add(self.adam)
        self.assertEqual(self.german.allocated_students, 20)

    def test_allocation_does_not_happen_twice(self):
        self.french.add(self.john)
        self.assertEqual(self.french.allocated_students, 6)
        self.french.add(self.john)
        self.assertEqual(self.french.allocated_students, 6)
        
if __name__ == "__main__":
    unittest.main()