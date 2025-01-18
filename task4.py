message = "Today is a beatiful day! The sun is shining and the birds are singing."

def count_unique_characters(string):
    lower_string = string.lower()
    unique_chars = list(filter(lambda c: lower_string.count(c.lower()) == 1, lower_string))
    return len(unique_chars)

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке: ", unique_count)