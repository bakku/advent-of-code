package puzzles

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"

	"bakku.dev/aog2022/shared"
)

type instruction struct {
	src    int
	dest   int
	amount int
}

func parseStacks(rawStacks []string) []shared.Stack[string] {
	stacks := make([]shared.Stack[string], strings.Count(rawStacks[len(rawStacks)-2], "["))

	for line := len(rawStacks) - 2; line >= 0; line-- {
		for column, stackIdx := 1, 0; column < len(rawStacks[line]); column, stackIdx = column+4, stackIdx+1 {
			if string(rawStacks[line][column]) != " " {
				stacks[stackIdx].Push(string(rawStacks[line][column]))
			}
		}
	}

	return stacks
}

func Day5(input string) {
	rawStacks := strings.Split(strings.Split(input, "\n\n")[0], "\n")
	rawInstructions := strings.Split(strings.TrimSuffix(strings.Split(input, "\n\n")[1], "\n"), "\n")

	re := regexp.MustCompile("\\d+")

	instructions := make([]instruction, len(rawInstructions))

	for _, rawInstruction := range rawInstructions {
		matches := re.FindAllString(rawInstruction, -1)
		amount, _ := strconv.Atoi(matches[0])
		src, _ := strconv.Atoi(matches[1])
		dest, _ := strconv.Atoi(matches[2])

		instructions = append(instructions, instruction{src - 1, dest - 1, amount})
	}

	stacks9000 := parseStacks(rawStacks)

	for _, instruction := range instructions {
		for i := 0; i < instruction.amount; i++ {
			stacks9000[instruction.dest].Push(stacks9000[instruction.src].Pop())
		}
	}

	fmt.Print("CrateMover 9000: ")

	for _, stack := range stacks9000 {
		fmt.Print(stack.Pop())
	}

	fmt.Println()

	stacks9001 := parseStacks(rawStacks)

	for _, instruction := range instructions {
		elements := make([]string, instruction.amount)

		for i := 0; i < instruction.amount; i++ {
			elements[i] = stacks9001[instruction.src].Pop()
		}

		stacks9001[instruction.dest].PushMultiple(elements)
	}

	fmt.Print("CrateMover 9001: ")

	for _, stack := range stacks9001 {
		fmt.Print(stack.Pop())
	}

	fmt.Println()
}
