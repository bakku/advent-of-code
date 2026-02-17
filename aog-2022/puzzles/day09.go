package puzzles

import (
	"fmt"
	"math"
	"strconv"
	"strings"

	"bakku.dev/aog2022/shared"
)

type motion struct {
	direction string
	steps     int
}

type position struct {
	x, y int
}

func (p *position) string() string {
	return strconv.Itoa(p.x) + "," + strconv.Itoa(p.y)
}

func parseMotions(rawMotions []string) []motion {
	motions := make([]motion, len(rawMotions))

	for i, rawMotion := range rawMotions {
		direction := strings.Split(rawMotion, " ")[0]
		steps, _ := strconv.Atoi(strings.Split(rawMotion, " ")[1])

		motions[i] = motion{direction, steps}
	}

	return motions
}

func pullRope(head, tail *position) {
	if math.Abs(float64(head.x-tail.x)) <= 1 && math.Abs(float64(head.y-tail.y)) <= 1 {
		return
	}

	if head.y == tail.y {
		if head.x > tail.x {
			tail.x += 1
		} else {
			tail.x -= 1
		}

		return
	}

	if head.x == tail.x {
		if head.y > tail.y {
			tail.y += 1
		} else {
			tail.y -= 1
		}

		return
	}

	if head.x > tail.x {
		if head.y > tail.y {
			// T . .
			// . . H
			tail.x += 1
			tail.y += 1
		} else {
			// . . H
			// T . .
			tail.x += 1
			tail.y -= 1
		}
	} else {
		if head.y > tail.y {
			// . . T
			// H . .
			tail.x -= 1
			tail.y += 1
		} else {
			// H . .
			// . . T
			tail.x -= 1
			tail.y -= 1
		}
	}
}

func performNextMove(motion motion, visitedPositions *shared.Set[string], rope []*position) {
	switch motion.direction {
	case "R":
		for i := 0; i < motion.steps; i++ {
			rope[0].x += 1

			for i := 0; i < len(rope)-1; i++ {
				pullRope(rope[i], rope[i+1])
			}

			visitedPositions.Add(rope[len(rope)-1].string())
		}
	case "L":
		for i := 0; i < motion.steps; i++ {
			rope[0].x -= 1

			for i := 0; i < len(rope)-1; i++ {
				pullRope(rope[i], rope[i+1])
			}

			visitedPositions.Add(rope[len(rope)-1].string())
		}
	case "U":
		for i := 0; i < motion.steps; i++ {
			rope[0].y -= 1

			for i := 0; i < len(rope)-1; i++ {
				pullRope(rope[i], rope[i+1])
			}

			visitedPositions.Add(rope[len(rope)-1].string())
		}
	case "D":
		for i := 0; i < motion.steps; i++ {
			rope[0].y += 1

			for i := 0; i < len(rope)-1; i++ {
				pullRope(rope[i], rope[i+1])
			}

			visitedPositions.Add(rope[len(rope)-1].string())
		}
	}
}

func Day9(input string) {
	visitedPositions := shared.NewSet([]string{})
	motions := parseMotions(strings.Split(strings.TrimSuffix(input, "\n"), "\n"))

	head := position{0, 0}
	tail := position{0, 0}

	for _, motion := range motions {
		performNextMove(motion, visitedPositions, []*position{&head, &tail})
	}

	fmt.Printf("Visited positions for just head and tail: %d\n", visitedPositions.Size())

	rope := make([]*position, 10)
	visitedPositionsLongRope := shared.NewSet([]string{})

	for i := range rope {
		rope[i] = &position{0, 0}
	}

	for _, motion := range motions {
		performNextMove(motion, visitedPositionsLongRope, rope)
	}

	fmt.Printf("Visited positions for long rope: %d\n", visitedPositionsLongRope.Size())
}
