"""
20 - AI/ML Preparation: Python Habits That Matter for AI/ML
Runnable examples matching the lesson.
"""

# Example 1: a believable "before you learn ML" data-cleaning snippet
raw_rows = [
    {"age": "25", "score": "90"},
    {"age": "N/A", "score": "78"},
    {"age": "31", "score": "not recorded"},
]


def safe_float(text):
    try:
        return float(text)
    except ValueError:
        return None


cleaned = [
    {"age": safe_float(row["age"]), "score": safe_float(row["score"])}
    for row in raw_rows
]
print(cleaned)


# Example 2: splitting data, using unpacking
def split_dataset(data, train_ratio=0.8):
    split_point = int(len(data) * train_ratio)
    return data[:split_point], data[split_point:]


all_data = list(range(10))
train_data, test_data = split_dataset(all_data)
print(train_data)
print(test_data)


# Example 3: the object/method pattern
class SimpleAverager:
    def __init__(self):
        self.values = []

    def fit(self, data):
        self.values = data

    def predict(self):
        return sum(self.values) / len(self.values)


model = SimpleAverager()
model.fit([10, 20, 30])
print(model.predict())

# Example 4: ranking results with key=
predictions = [
    {"label": "cat", "confidence": 0.72},
    {"label": "dog", "confidence": 0.95},
    {"label": "bird", "confidence": 0.41},
]

ranked = sorted(predictions, key=lambda p: p["confidence"], reverse=True)
for prediction in ranked:
    print(prediction["label"], prediction["confidence"])
