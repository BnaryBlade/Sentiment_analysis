from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        sentiment = "позитивное"
    elif polarity < 0:
        sentiment = "негативное"
    else:
        sentiment = "нейтральное"

    return sentiment, polarity, subjectivity

reviews = [
    "Прекрасный продукт, я полностью удовлетворен!",
    "Качество ужасное, очень разочарован.",
    "Среднее качество, ничего особенного."
]

for review in reviews:
    sentiment, polarity, subjectivity = analyze_sentiment(review)
    print(f"Отзыв: {review}")
    print(f"Настроение: {sentiment}")
    print(f"Полярность: {polarity}")
    print(f"Субъективность: {subjectivity}")
    print("-------------------------")

