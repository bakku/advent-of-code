package puzzles

import (
	"fmt"
	"strings"

	"bakku.dev/aog2022/shared"
)

func isMarkerStart(chars []byte) bool {
	charSet := shared.NewSet[byte](chars)

	return charSet.Size() == len(chars)
}

func shift(chars []byte) {
	for i := 0; i < len(chars)-1; i++ {
		chars[i] = chars[i+1]
	}
}

func Day6(input string) {
	datastream := strings.Trim(input, "\n")
	lastFourChars := make([]byte, 4)

	lastFourChars[0] = datastream[0]
	lastFourChars[1] = datastream[1]
	lastFourChars[2] = datastream[2]

	for i := 3; i < len(datastream); i++ {
		lastFourChars[3] = datastream[i]

		if isMarkerStart(lastFourChars) {
			fmt.Printf("first packet marker after character %d\n", i+1)
			break
		}

		shift(lastFourChars)
	}

	lastFourteenChars := make([]byte, 14)

	for i := 0; i < 13; i++ {
		lastFourteenChars[i] = datastream[i]
	}

	for i := 13; i < len(datastream); i++ {
		lastFourteenChars[13] = datastream[i]

		if isMarkerStart(lastFourteenChars) {
			fmt.Printf("first message marker after character %d\n", i+1)
			break
		}

		shift(lastFourteenChars)
	}
}
