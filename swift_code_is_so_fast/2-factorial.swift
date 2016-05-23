func factorial(N: Int) -> (Int){
	if (N < 0){
		return 0
	}

	if (N == 0){
		return 1
	}
	var i = N-1
	var o = N

	while (i != 0){
		o = o*i
		i = i-1
	}

	return(o)
}