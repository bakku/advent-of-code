package puzzles

import "testing"

func TestDirectoriesToDirSizes(t *testing.T) {
	dirTree := directory{
		name: "A",
		files: []file{
			{name: "a", size: 1000},
			{name: "b", size: 200},
		},
		subdirs: []*directory{
			&directory{
				name: "B",
				files: []file{
					{name: "c", size: 3000},
				},
				subdirs: []*directory{
					&directory{
						name: "C",
						files: []file{
							{name: "d", size: 5000},
						},
						subdirs: []*directory{},
					},
				},
			},
			&directory{
				name: "D",
				files: []file{
					{name: "e", size: 2000},
				},
				subdirs: []*directory{},
			},
		},
	}

	var dirSizes []int
	dirSizes = directoriesToDirSizes(&dirTree, dirSizes)

	if dirSizes[0] != 11200 {
		t.Fatalf("Expected %d, Got %d\n", 11200, dirSizes[0])
	}

	if dirSizes[1] != 8000 {
		t.Fatalf("Expected %d, Got %d\n", 8000, dirSizes[1])
	}

	if dirSizes[2] != 5000 {
		t.Fatalf("Expected %d, Got %d\n", 5000, dirSizes[2])
	}

	if dirSizes[3] != 2000 {
		t.Fatalf("Expected %d, Got %d\n", 2000, dirSizes[3])
	}
}

func TestParseOutputLines(t *testing.T) {
	lines := []string{
		"$ cd /",
		"$ ls",
		"dir a",
		"14848514 b.txt",
		"8504156 c.dat",
		"dir d",
		"$ cd a",
		"$ ls",
		"dir e",
		"29116 f",
		"2557 g",
		"62596 h.lst",
		"$ cd e",
		"$ ls",
		"584 i",
		"$ cd ..",
		"$ cd ..",
		"$ cd d",
		"$ ls",
		"4060174 j",
		"8033020 d.log",
		"5626152 d.ext",
		"7214296 k",
	}

	directoryTree := parseOutputLines(lines)

	if directoryTree.name != "/" {
		t.Fatalf("Expected name %s, Got %s\n", "/", directoryTree.name)
	}

	if directoryTree.subdirs[0].name != "a" {
		t.Fatalf("Expected name %s, Got %s\n", "a", directoryTree.name)
	}

}
