package puzzles

import (
	"fmt"
	"strings"
)

func getSharedItem(firstCompartment, secondCompartment string) string {
	for i := 0; i < len(firstCompartment); i++ {
		for j := 0; j < len(secondCompartment); j++ {
			if firstCompartment[i] == secondCompartment[j] {
				return string(firstCompartment[i])
			}
		}
	}

	return ""
}

func getSharedBadge(firstRucksack, secondRucksack, thirdRucksack string) string {
	for i := 0; i < len(firstRucksack); i++ {
		for j := 0; j < len(secondRucksack); j++ {
			for k := 0; k < len(thirdRucksack); k++ {
				if firstRucksack[i] == secondRucksack[j] && firstRucksack[i] == thirdRucksack[k] {
					return string(firstRucksack[i])
				}
			}
		}
	}

	return ""
}

func Day3(input string) {
	priorities := make(map[string]int)

	for i, char := range "abcdefghijklmnopqrstuvwxyz" {
		priorities[string(char)] = i + 1
	}

	for i, char := range "ABCDEFGHIJKLMNOPQRSTUVWXYZ" {
		priorities[string(char)] = i + 27
	}

	rucksackItems := strings.Split(input, "\n")

	sum := 0

	// last element in the rucksackitems is the last empty line, just ignore it
	for _, items := range rucksackItems[:len(rucksackItems)-1] {
		firstCompartment := items[0 : len(items)/2]
		secondCompartment := items[len(items)/2 : len(items)]
		sharedItem := getSharedItem(firstCompartment, secondCompartment)

		priority, _ := priorities[sharedItem]

		sum = sum + priority
	}

	fmt.Printf("Sum of priorities: %d\n", sum)

	i := 0
	sum = 0

	for i < len(rucksackItems)-1 {
		firstRucksack := rucksackItems[i]
		secondRucksack := rucksackItems[i+1]
		thirdRucksack := rucksackItems[i+2]

		badge := getSharedBadge(firstRucksack, secondRucksack, thirdRucksack)

		priority, _ := priorities[badge]

		sum = sum + priority

		i = i + 3
	}

	fmt.Printf("Sum of badge priorities: %d\n", sum)
}
