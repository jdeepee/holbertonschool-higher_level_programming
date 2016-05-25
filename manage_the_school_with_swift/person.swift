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

enum Subject: String {
	case Math = "Math", English = "English", French = "French", History = "History"

	func get() -> String{
		switch self{
			case .Math:
				return "Math"

			case .English:
				return "English"

			case .French:
				return "French"

			case .History:
				return "History"
		}
	}
}

class Mentor: Person, Classify {
	let subject: Subject

	init (first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.subject = subject
	}

	func isStudent() -> Bool {
		return false
	}

	func stringSubject() -> String {
		return self.subject.get()
	}

}

class Student: Person, Classify {
	func isStudent() -> Bool{
		return true
	}
}

protocol Classify {
	func isStudent() -> Bool
}
