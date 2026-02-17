package puzzles

import (
	"fmt"
	"strconv"
	"strings"

	"bakku.dev/aog2022/shared"
)

func pairToIntArray(pair string) []int {
	start, _ := strconv.Atoi(strings.Split(pair, "-")[0])
	end, _ := strconv.Atoi(strings.Split(pair, "-")[1])

	var result []int

	for i := start; i <= end; i++ {
		result = append(result, i)
	}

	return result
}

func Day4(input string) {
	pairs := strings.Split(strings.TrimSuffix(input, "\n"), "\n")

	count := 0

	for _, pair := range pairs {
		firstPair := strings.Split(pair, ",")[0]
		secondPair := strings.Split(pair, ",")[1]

		firstSet := shared.NewSet[int](pairToIntArray(firstPair))
		secondSet := shared.NewSet[int](pairToIntArray(secondPair))

		if firstSet.IsSubsetOf(secondSet) || secondSet.IsSubsetOf(firstSet) {
			count = count + 1
		}
	}

	fmt.Printf("Amount of pairs where one fully contains the other: %d\n", count)

	count = 0

	for _, pair := range pairs {
		firstPair := strings.Split(pair, ",")[0]
		secondPair := strings.Split(pair, ",")[1]

		firstSet := shared.NewSet[int](pairToIntArray(firstPair))
		secondSet := shared.NewSet[int](pairToIntArray(secondPair))

		if firstSet.Intersection(secondSet).Size() > 0 {
			count = count + 1
		}
	}

	fmt.Printf("Amount of pairs which overlap: %d\n", count)
}
