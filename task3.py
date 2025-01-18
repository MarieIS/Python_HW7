from collections import Counter

def can_be_poly(row: str) -> bool:
    char_counts = Counter(row)
    odd_count = len(list(filter(lambda x: x % 2, char_counts.values())))
    return odd_count < 2

print(can_be_poly(input('Введите ваше слово: ')))