package puzzles

import (
	"fmt"
	"strconv"
	"strings"
)

type file struct {
	name string
	size int
}

type directory struct {
	name      string
	files     []file
	subdirs   []*directory
	parentDir *directory
}

func (d *directory) TotalSize() int {
	totalSize := 0

	for _, subdir := range d.subdirs {
		totalSize = totalSize + subdir.TotalSize()
	}

	for _, file := range d.files {
		totalSize = totalSize + file.size
	}

	return totalSize
}

func runCD(lines []string, currentLine *int, currentDir *directory) *directory {
	dirName := string(lines[*currentLine][5:])
	*currentLine = *currentLine + 1

	if dirName == ".." {
		return currentDir.parentDir
	}

	for _, dir := range currentDir.subdirs {
		if dir.name == dirName {
			return dir
		}
	}

	return nil
}

func runLS(lines []string, currentLine *int, currentDir *directory) *directory {
	*currentLine = *currentLine + 1

	for {
		if *currentLine >= len(lines) || lines[*currentLine][0:4] == "$ cd" || lines[*currentLine][0:4] == "$ ls" {
			break
		}

		lineParts := strings.Split(lines[*currentLine], " ")

		if lineParts[0] == "dir" {
			currentDir.subdirs = append(
				currentDir.subdirs,
				&directory{name: lineParts[1], files: []file{}, subdirs: []*directory{}, parentDir: currentDir},
			)
		} else {
			size, _ := strconv.Atoi(lineParts[0])

			currentDir.files = append(currentDir.files, file{name: lineParts[1], size: size})
		}

		*currentLine = *currentLine + 1
	}

	return currentDir
}

func runNextCommand(lines []string, currentLine *int, currentDir *directory) *directory {
	if string(lines[*currentLine][0:4]) == "$ cd" {
		return runCD(lines, currentLine, currentDir)
	}

	return runLS(lines, currentLine, currentDir)
}

func parseOutputLines(lines []string) directory {
	currentLine := 1
	directoryTree := directory{name: "/", files: []file{}, subdirs: []*directory{}}
	directoryWalker := &directoryTree

	for {
		if currentLine >= len(lines) {
			break
		}

		directoryWalker = runNextCommand(lines, &currentLine, directoryWalker)
	}

	return directoryTree
}

func directoriesToDirSizes(directoryTree *directory, dirSizes []int) []int {
	dirSizes = append(dirSizes, directoryTree.TotalSize())

	for _, subdir := range directoryTree.subdirs {
		dirSizes = directoriesToDirSizes(subdir, dirSizes)
	}

	return dirSizes
}

func Day7(input string) {
	terminalOutput := strings.Split(strings.Trim(input, "\n"), "\n")

	directoryTree := parseOutputLines(terminalOutput)

	var dirSizes []int
	dirSizes = directoriesToDirSizes(&directoryTree, dirSizes)

	sum := 0

	for _, dirSize := range dirSizes {
		if dirSize <= 100000 {
			sum = sum + dirSize
		}
	}

	fmt.Printf("Sum of total sizes of directories with at most 100000: %d\n", sum)

	unusedSpace := 70000000 - dirSizes[0]
	necessarySpace := 30000000 - unusedSpace

	bestDirSizeToDelete := 70000000

	for _, dirSize := range dirSizes {
		if dirSize >= necessarySpace && dirSize < bestDirSizeToDelete {
			bestDirSizeToDelete = dirSize
		}
	}

	fmt.Printf("Best directory size to delete: %d\n", bestDirSizeToDelete)
}
