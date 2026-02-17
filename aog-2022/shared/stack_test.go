package shared_test

import (
	"testing"

	"bakku.dev/aog2022/shared"
)

func TestStack_Should_BehaveAsAStack(t *testing.T) {
	stack := shared.NewStack[int]([]int{})

	stack.Push(1)
	stack.Push(2)

	if stack.Size() != 2 {
		t.Fatalf("Expected size %d, got %d\n", 2, stack.Size())
	}

	element := stack.Pop()

	if element != 2 {
		t.Fatalf("Expected first Pop() to return %d, got %d\n", 2, element)
	}

	if stack.Size() != 1 {
		t.Fatalf("Expected size %d, got %d\n", 1, stack.Size())
	}

	element = stack.Pop()

	if element != 1 {
		t.Fatalf("Expected second Pop() to return %d, got %d\n", 2, element)
	}

	if stack.Size() != 0 {
		t.Fatalf("Expected size %d, got %d\n", 0, stack.Size())
	}

	stack.PushMultiple([]int{1, 2})

	element = stack.Pop()

	if element != 1 {
		t.Fatalf("Expected second Pop() to return %d, got %d\n", 1, element)
	}
}
