/* 20. Valid Parentheses - Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'. */

package main

import (
	"fmt" // Pacote para formatar a saída
)

func isValid(s string) bool {
	fmt.Printf("\n")
	if len(s) < 2 || len(s)%2 != 0 {
		return false
	}

	match := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}

	stack := []rune{}

	for _, char := range s {
		_, closing := match[char]
		opening := !closing

		if opening {
			stack = append(stack, char)

		} else {
			if len(stack) > 0 && stack[len(stack)-1] == match[char] {
				stack = stack[:len(stack)-1]

			} else {
				return false
			}
		}

	}
	return len(stack) == 0

}

func main20() {
	fmt.Println(isValid("()"))
	fmt.Println(isValid("()[]{}"))
	fmt.Println(isValid("(]"))
}
