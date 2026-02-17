package main

import (
	"log"
	"os"

	"bakku.dev/aog2022/puzzles"
)

func main() {
	bytes, err := os.ReadFile("./inputs/day10.txt")
	if err != nil {
		log.Fatal("input file could not be read")
	}

	puzzles.Day10(string(bytes))
}
