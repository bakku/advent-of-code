package shared

type Stack[T interface{}] struct {
	elements []T
}

func (s *Stack[T]) Push(element T) {
	s.elements = append(s.elements, element)
}

func (s *Stack[T]) PushMultiple(elements []T) {
	for i := len(elements) - 1; i >= 0; i-- {
		s.Push(elements[i])
	}
}

func (s *Stack[T]) Pop() T {
	element := s.elements[s.Size()-1]

	s.elements = s.elements[:s.Size()-1]

	return element
}

func (s *Stack[T]) Size() int {
	return len(s.elements)
}

func NewStack[T interface{}](initial []T) *Stack[T] {
	stack := &Stack[T]{}

	for _, element := range initial {
		stack.Push(element)
	}

	return stack
}
