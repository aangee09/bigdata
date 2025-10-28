from functools import reduce

data = [
    "MapReduce is a programming model",
    "MapReduce helps in processing big data",
    "Python can implement MapReduce easily"
]

def mapper(sentence):
    
    for word in sentence.split():
        yield (word.lower(), 1)

def shuffle_and_sort(mapped_data):
    grouped_data = {}
    for word, count in mapped_data:
        grouped_data.setdefault(word, []).append(count)
    return grouped_data

def reducer(word, counts):
    return (word, sum(counts))

mapped = []
for line in data:
    mapped.extend(mapper(line))

grouped = shuffle_and_sort(mapped)

reduced = [reducer(word, counts) for word, counts in grouped.items()]

print("Word Count Results:")
for word, count in reduced:
    print(f"{word}: {count}")
