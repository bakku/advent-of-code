package puzzles

import (
	"fmt"
	"log"
	"sort"
	"strconv"
	"strings"
)

func Day1(input string) {
	lines := strings.Split(input, "\n")
	var sums []int

	currentSum := 0

	for _, line := range lines {
		if line == "" {
			sums = append(sums, currentSum)
			currentSum = 0
		} else {
			num, err := strconv.Atoi(line)
			if err != nil {
				log.Fatal(fmt.Sprintf("number could not be converted: %s", line))
			}

			currentSum = currentSum + num
		}
	}

	sort.Slice(sums, func(a, b int) bool {
		return sums[a] > sums[b]
	})

	fmt.Printf("Max calories: %d\n", sums[0])
	fmt.Printf("Calories of top three: %d\n", sums[0]+sums[1]+sums[2])
}
