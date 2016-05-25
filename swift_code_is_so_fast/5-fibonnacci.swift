func fibonacci(number: Int) -> (Int){
	if number <= 1 {
        return number
    } else {
        return fibonacci(number - 1) + fibonacci(number - 2)
    }
}