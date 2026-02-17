package shared_test

import (
	"testing"

	"bakku.dev/aog2022/shared"
)

func compareSlices(slice1, slice2 []int) bool {
	if len(slice1) != len(slice2) {
		return false
	}

	for i := 0; i < len(slice1); i++ {
		if slice1[i] != slice2[i] {
			return false
		}
	}

	return true
}

func TestNewSet_Should_CreateASetOfUniqueElements(t *testing.T) {
	tests := []struct {
		input    []int
		expected []int
	}{
		{
			input:    []int{1, 1, 2, 3, 4},
			expected: []int{1, 2, 3, 4},
		},
		{
			input:    []int{1, 2, 3},
			expected: []int{1, 2, 3},
		},
	}

	for _, test := range tests {
		result := shared.NewSet(test.input)

		if !compareSlices(result.Elements, test.expected) {
			t.Fatalf("Expected %v, Got %v\n", test.expected, result.Elements)
		}
	}
}

func TestAdd_Should_AddElementsToTheSet(t *testing.T) {
	tests := []struct {
		initial    []int
		newElement int
		expected   []int
	}{
		{
			initial:    []int{1, 2},
			newElement: 3,
			expected:   []int{1, 2, 3},
		},
		{
			initial:    []int{1, 2, 3},
			newElement: 3,
			expected:   []int{1, 2, 3},
		},
	}

	for _, test := range tests {
		set := shared.NewSet(test.initial)

		set.Add(test.newElement)

		if !compareSlices(set.Elements, test.expected) {
			t.Fatalf("Expected %v, Got %v\n", test.expected, set.Elements)
		}
	}
}

func TestContains_ShouldCheckWhetherAnElementIsInTheSet(t *testing.T) {
	tests := []struct {
		initial        []int
		checkedElement int
		expected       bool
	}{
		{
			initial:        []int{1, 2},
			checkedElement: 2,
			expected:       true,
		},
		{
			initial:        []int{1, 2},
			checkedElement: 3,
			expected:       false,
		},
	}

	for _, test := range tests {
		set := shared.NewSet(test.initial)

		if set.Contains(test.checkedElement) != test.expected {
			if test.expected {
				t.Fatalf("Expected %v to contain %d\n", set.Elements, test.checkedElement)
			}

			if !test.expected {
				t.Fatalf("Expected %v not to contain %d\n", set.Elements, test.checkedElement)
			}
		}
	}
}

func TestIsSubsetOf_ShouldCheckWhetherTheSetIsASubsetOfTheGivenSet(t *testing.T) {
	tests := []struct {
		set      []int
		other    []int
		expected bool
	}{
		{
			set:      []int{1, 2, 3, 4, 5},
			other:    []int{2, 3, 4},
			expected: false,
		},
		{
			set:      []int{2, 3, 4},
			other:    []int{2, 3, 4, 5, 6},
			expected: true,
		},
	}

	for _, test := range tests {
		set := shared.NewSet(test.set)
		other := shared.NewSet(test.other)

		if set.IsSubsetOf(other) != test.expected {
			if test.expected {
				t.Fatalf("Expected %v to be a subset of %v\n", set.Elements, other.Elements)
			}

			if !test.expected {
				t.Fatalf("Expected %v not to be a subset of %v\n", set.Elements, other.Elements)
			}
		}
	}
}

func TestIntersection_Should_ReturnTheIntersectionOfTheSets(t *testing.T) {
	tests := []struct {
		set      []int
		other    []int
		expected []int
	}{
		{
			set:      []int{1, 2, 3, 4, 5},
			other:    []int{2, 3, 4},
			expected: []int{2, 3, 4},
		},
		{
			set:      []int{1, 2},
			other:    []int{2, 3, 4, 5, 6},
			expected: []int{2},
		},
		{
			set:      []int{1, 2},
			other:    []int{3, 4, 5, 6},
			expected: []int{},
		},
	}

	for _, test := range tests {
		set := shared.NewSet(test.set)
		other := shared.NewSet(test.other)

		result := set.Intersection(other)

		if !compareSlices(result.Elements, test.expected) {
			t.Fatalf("Expected %v, Got %v\n", test.expected, result.Elements)
		}
	}
}
