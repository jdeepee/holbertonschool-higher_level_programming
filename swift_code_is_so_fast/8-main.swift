
let strings = ["We", "Heart", "Swift"]

let string = strings.map({ (strings: String) -> String in
				var joiner = " "
				var joinedStrings = strings.joinWithSeparator(joiner)
				return joinedStrings
			})

print(string)
