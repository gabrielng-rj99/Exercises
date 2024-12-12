package main

import (
	"fmt"
)

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	if x < 10 {
		return true
	}

	if x < 100 {
		if x%10 == x/10 {
			return true
		}
		return false
	}

	if x%10 == 0 {
		return false
	}

	rev := 0
	temp := x

	for temp > 0 {
		rev = rev*10 + temp%10
		temp /= 10
	}

	return rev == x
}

// 7424 - 7 - 40 - 200 - 4000
// 5225 - 5 - 20 - 200 - 5000

func main9_1() {
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(123))
	fmt.Println(isPalindrome(10))
	fmt.Println(isPalindrome(313))
}
