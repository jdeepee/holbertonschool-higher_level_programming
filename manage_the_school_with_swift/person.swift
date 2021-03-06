class Person {
	var first_name: String
	var last_name: String
	var age: Int

	init (first_name: String, last_name: String, age: Int) {
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
	}

	func fullName() -> String {
		return self.first_name + " " + self.last_name
	}
}

protocol Classify {
	func isStudent() -> Bool
}

enum Subject: String {
	case Math, English, French, History
}

class Mentor: Person, Classify {
	let subject: Subject

	init (first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
		self.subject = subject
		super.init(first_name: first_name, last_name: last_name, age: age)
	}

	func isStudent() -> Bool {
		return false
	}

	func stringSubject() -> String {
		switch subject {
			case .Math: return "Math"
			case .English: return "English"
			case .French: return "French"
			case .History: return "History"
	}

}

class Student: Person, Classify {
	var list_exercises: [Exercise]

	init(first_name: String, last_name: String, age: Int, _ list_exercises: [Exercise] = []) {
		self.list_exercises = []
		super.init(first_name: first_name, last_name: last_name, age: age)
	}  

	func isStudent() -> Bool{
		return true
	}


	func addNewNote(subject: Subject, _ note: Int) {
		let ex = Exercise(subject: subject, note: note)
		self.list_exercises.append(ex)
	}

	func average(subject: Subject) -> Float {
		let list_subject = list_exercises.filter {$0.subject == subject}
		return list_subject.reduce(0) {$0 + Float($1.note)} / Float(list_subject.count)
	}

	func averageAll() -> Float {
		return list_exercises.reduce(0) {$0 + Float($1.note)} / Float(list_exercises.count)
	}
}

class School {
	var name: String
	var list_persons: [Person]

	init (name: String) {
		self.name = name
		self.list_persons = []
	}

	func average(subject: Subject) -> Float {
		return self.listStudents().reduce(0) {$0 + ($1 as! Student).average(subject) } / Float(self.listStudents().count)
	}

	func averageAll() -> Float {
		return self.listStudents().reduce(0) {$0 + ($1 as! Student).averageAll() } / Float(self.listStudents().count)
	}

	func addStudent(p: Person) -> Bool {
		if p is Student {
			list_persons.append(p)
			return true
		}
		return false
	}

	func addMentor(p: Person) -> Bool {
		if p is Mentor {
			list_persons.append(p)
			return true
		}
		return false
	}

	func listStudents() -> [Person] {
		return list_persons.filter({$0 is Student}).sort {return $0.age < $1.age}
	}

	func listMentors() -> [Person] {
		return list_persons.filter({$0 is Mentor}).sort {return $0.age < $1.age}
	}

	// The spec for this function contradicts the provided tests.
	func listMentorsBySubject() -> [Person] {
		return list_persons.filter({$0 is Mentor}).sort {return $0.age < $1.age}
	}

	func mentorsAgeAverage() -> Int {
		let mentors = self.listMentors()
		if mentors.count < 1 {
			return 0
		} else if mentors.count == 1 {
			return mentors[0].age
		} else { 
			return mentors.reduce(0, combine:{
				(first: Int, second: Person) -> Int in
				return first + second.age
			}) / mentors.count
		}
	}


	func mentorsAgeAverge() -> Int {
		return self.mentorsAgeAverage()
	}

	func studentsAgeAverage() -> Int {
		let students = self.listStudents()
		if students.count < 1 {
			return 0
		} else if students.count == 1 {
			return students[0].age
		} else {
			return students.reduce(0, combine:{
				(first: Int, second: Person) -> Int in
			return first + second.age
			}) / students.count
		}
	}

	func studentsAgeAverge() -> Int {
		return self.studentsAgeAverage()
	}
}

class Exercise {
	var subject: Subject
	var note: Int

	init(subject: Subject, note: Int = 0) {
		self.subject = subject
		self.note = note
		setNote(note)
	}

	func setNote(note: Int) {
		self.note = note
		if self.note < 0 {
			self.note = 0
		} else if self.note > 10 {
			self.note = 10
		}
	}
}
