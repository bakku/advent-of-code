package puzzles

import (
	"fmt"
	"strconv"
	"strings"
)

func isVisible(x, y int, grid [][]int) bool {
	if x == 0 || y == 0 || x == (len(grid[0])-1) || y == (len(grid)-1) {
		return true
	}

	topVisible := true
	bottomVisible := true
	rightVisible := true
	leftVisible := true

	for i := (x - 1); i >= 0; i-- {
		if grid[y][i] >= grid[y][x] {
			leftVisible = false
		}
	}

	for i := (x + 1); i <= (len(grid[0]) - 1); i++ {
		if grid[y][i] >= grid[y][x] {
			rightVisible = false
		}
	}

	for i := (y - 1); i >= 0; i-- {
		if grid[i][x] >= grid[y][x] {
			topVisible = false
		}
	}

	for i := (y + 1); i <= (len(grid) - 1); i++ {
		if grid[i][x] >= grid[y][x] {
			bottomVisible = false
		}
	}

	return topVisible || bottomVisible || rightVisible || leftVisible
}

func scenicScore(x, y int, grid [][]int) int {
	var topVisibility int
	var rightVisibility int
	var bottomVisibility int
	var leftVisibility int

	for i := (x - 1); i >= 0; i-- {
		leftVisibility++

		if grid[y][x] <= grid[y][i] {
			break
		}
	}

	for i := (x + 1); i <= (len(grid[0]) - 1); i++ {
		rightVisibility++

		if grid[y][x] <= grid[y][i] {
			break
		}
	}

	for i := (y - 1); i >= 0; i-- {
		topVisibility++

		if grid[y][x] <= grid[i][x] {
			break
		}
	}

	for i := (y + 1); i <= (len(grid) - 1); i++ {
		bottomVisibility++

		if grid[y][x] <= grid[i][x] {
			break
		}
	}

	return leftVisibility * rightVisibility * topVisibility * bottomVisibility
}

func parseGrid(rawGrid string) [][]int {
	lines := strings.Split(strings.Trim(rawGrid, "\n"), "\n")

	var grid [][]int

	for i, line := range lines {
		grid = append(grid, []int{})

		for _, c := range line {
			num, _ := strconv.Atoi(string(c))

			grid[i] = append(grid[i], num)
		}
	}

	return grid
}

func Day8(input string) {
	grid := parseGrid(input)

	visibleTrees := 0
	maxScenicScore := 0

	for y := range grid {
		for x := range grid[y] {
			if isVisible(x, y, grid) {
				visibleTrees++
			}

			if scenicScore(x, y, grid) > maxScenicScore {
				maxScenicScore = scenicScore(x, y, grid)
			}
		}
	}

	fmt.Printf("Visible trees: %d\n", visibleTrees)
	fmt.Printf("Max scenic score: %d\n", maxScenicScore)
}
