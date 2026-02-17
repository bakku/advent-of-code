package puzzles

import (
	"fmt"
	"strings"
)

const opponentRock = "A"
const opponentPaper = "B"
const opponentScissors = "C"

const ownRock = "X"
const ownPaper = "Y"
const ownScissors = "Z"

const looseInstruction = "X"
const drawInstruction = "Y"
const winInstruction = "Z"

const winPoints = 6
const drawPoints = 3

func buildChoiceScores() func(string) int {
	choiceScores := map[string]int{
		ownRock:     1,
		ownPaper:    2,
		ownScissors: 3,
	}

	return func(choice string) int {
		value, _ := choiceScores[choice]
		return value
	}
}

func buildWins() func(string) string {
	wins := map[string]string{
		opponentRock:     ownPaper,
		opponentPaper:    ownScissors,
		opponentScissors: ownRock,
	}

	return func(choice string) string {
		value, _ := wins[choice]
		return value
	}
}

func buildDraws() func(string) string {
	draws := map[string]string{
		opponentRock:     ownRock,
		opponentPaper:    ownPaper,
		opponentScissors: ownScissors,
	}

	return func(choice string) string {
		value, _ := draws[choice]
		return value
	}
}

func buildLosses() func(string) string {
	losses := map[string]string{
		opponentRock:     ownScissors,
		opponentPaper:    ownRock,
		opponentScissors: ownPaper,
	}

	return func(choice string) string {
		value, _ := losses[choice]
		return value
	}
}

func Day2(input string) {
	choiceScores := buildChoiceScores()
	wins := buildWins()
	draws := buildDraws()
	losses := buildLosses()

	rounds := strings.Split(input, "\n")

	totalScore := 0

	// last element in the rounds is the last empty line, just ignore it
	for _, round := range rounds[:len(rounds)-1] {
		opponentChoice := string(round[0])
		ownChoice := string(round[2])

		choiceScore := choiceScores(ownChoice)

		if wins(opponentChoice) == ownChoice {
			totalScore = totalScore + choiceScore + winPoints
		} else if draws(opponentChoice) == ownChoice {
			totalScore = totalScore + choiceScore + drawPoints
		} else {
			totalScore = totalScore + choiceScore
		}
	}

	fmt.Printf("Total score for part 1: %d\n", totalScore)

	totalScore2 := 0

	for _, round := range rounds[:len(rounds)-1] {
		opponentChoice := string(round[0])
		instruction := string(round[2])

		if instruction == looseInstruction {
			ownChoice := losses(opponentChoice)
			totalScore2 = totalScore2 + choiceScores(ownChoice)
		} else if instruction == drawInstruction {
			ownChoice := draws(opponentChoice)
			totalScore2 = totalScore2 + choiceScores(ownChoice) + drawPoints
		} else {
			ownChoice := wins(opponentChoice)
			totalScore2 = totalScore2 + choiceScores(ownChoice) + winPoints
		}
	}

	fmt.Printf("Total score for part 2: %d\n", totalScore2)
}
