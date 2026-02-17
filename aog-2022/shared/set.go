package shared

type Set[T comparable] struct {
	Elements []T
}

func (set *Set[T]) Contains(n T) bool {
	for _, element := range set.Elements {
		if element == n {
			return true
		}
	}

	return false
}

func (set *Set[T]) Add(n T) {
	if !set.Contains(n) {
		set.Elements = append(set.Elements, n)
	}
}

func (set *Set[T]) IsSubsetOf(other *Set[T]) bool {
	for _, setElement := range set.Elements {
		currentElementContained := false

		for _, otherElement := range other.Elements {
			if setElement == otherElement {
				currentElementContained = true
			}
		}

		if !currentElementContained {
			return false
		}
	}

	return true
}

func (set *Set[T]) Intersection(other *Set[T]) *Set[T] {
	result := []T{}

	for _, setElement := range set.Elements {
		for _, otherElement := range other.Elements {
			if setElement == otherElement {
				result = append(result, setElement)
			}
		}
	}

	return NewSet(result)
}

func (set *Set[T]) Size() int {
	return len(set.Elements)
}

func NewSet[T comparable](elements []T) *Set[T] {
	s := &Set[T]{
		Elements: make([]T, 0),
	}

	for _, n := range elements {
		s.Add(n)
	}

	return s
}
