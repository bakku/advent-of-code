package puzzles

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func calculateSignalStrength(cycle, X int) int {
	if cycle == 20 || (cycle > 20 && ((cycle-20)%40) == 0) {
		return cycle * X
	}

	return 0
}

func draw(image [][]string, X, cycle int) {
	y := int(cycle / 40)
	x := (cycle - 1) % 40

	if math.Abs(float64(X-x)) <= 1 {
		image[y][x] = "#"
	} else {
		image[y][x] = "."
	}
}

func printImage(image [][]string) {
	for i := range image {
		for j := range image[i] {
			fmt.Print(image[i][j])
		}
		fmt.Println()
	}
}

func Day10(input string) {
	cycle := 0
	X := 1

	signalStrengthSum := 0

	instructions := strings.Split(strings.TrimSuffix(input, "\n"), "\n")

	for _, instruction := range instructions {
		command := strings.Split(instruction, " ")[0]

		switch command {
		case "addx":
			num, _ := strconv.Atoi(strings.Split(instruction, " ")[1])
			cycle++
			signalStrengthSum += calculateSignalStrength(cycle, X)
			cycle++
			signalStrengthSum += calculateSignalStrength(cycle, X)
			X += num
		case "noop":
			cycle++
			signalStrengthSum += calculateSignalStrength(cycle, X)
		}
	}

	fmt.Println(signalStrengthSum)

	image := make([][]string, 6)

	for i := range image {
		image[i] = make([]string, 40)
	}

	cycle = 0
	X = 1

	for _, instruction := range instructions {
		command := strings.Split(instruction, " ")[0]

		switch command {
		case "addx":
			num, _ := strconv.Atoi(strings.Split(instruction, " ")[1])
			cycle++
			draw(image, X, cycle)
			cycle++
			draw(image, X, cycle)
			X += num
		case "noop":
			cycle++
			draw(image, X, cycle)
		}

		if cycle == 239 {
			break
		}
	}

	printImage(image)
}
