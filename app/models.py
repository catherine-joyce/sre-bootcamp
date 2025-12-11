from dataclasses import dataclass

@dataclass(frozen=True)
class Student:
   id: str
   first_name: str
   last_name: str

class Subject:
    def __init__(self, name: str, size: int):
        self.name = name 
        self.size = size
        self._allocations = set()

    def add(self, student: Student):
        if self.allocated_students == self.size:
            raise ValueError("Subject is already full.")
        if student not in self._allocations:
            self._allocations.add(student)
    
    @property
    def allocated_students(self) -> int:
        return len(self._allocations)