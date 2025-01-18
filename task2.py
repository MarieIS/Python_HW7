from typing import List, Tuple

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

results: List[Tuple[str, int]] = list(map(lambda x, y: (x, y), letters, numbers))

print(results)