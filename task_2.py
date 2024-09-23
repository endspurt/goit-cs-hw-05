import requests
import re
import matplotlib.pyplot as plt
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

# Функція для завантаження тексту з URL
def download_text(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# Функція для очищення тексту і розбиття його на слова
def clean_text(text):
    text = re.sub(r'[^A-Za-z\s]', '', text)  # Видаляємо всі символи, окрім букв і пробілів
    return text.lower().split()

# Функція MapReduce для підрахунку частоти слів
def count_words(text):
    words = clean_text(text)
    word_counts = Counter(words)
    return word_counts

# Функція для злиття результатів Map (Reduce)
def merge_counters(counters):
    total = Counter()
    for counter in counters:
        total.update(counter)
    return total

# Функція для візуалізації результатів
def visualize_top_words(word_counts, top_n=10):
    common_words = word_counts.most_common(top_n)
    words, counts = zip(*common_words)

    plt.barh(words, counts, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title(f'Top {top_n} Most Frequent Words')
    plt.show()

# Основна функція
def main():
    url = 'https://www.gutenberg.org/files/1342/1342-0.txt'  # URL для завантаження тексту
    text = download_text(url)
    
    # Використовуємо багатопоточність для MapReduce
    with ThreadPoolExecutor() as executor:
        chunks = [text[i:i+10000] for i in range(0, len(text), 10000)]  # Ділимо текст на частини
        future_counters = executor.map(count_words, chunks)
        word_counts = merge_counters(future_counters)

    # Візуалізація топ-слова
    visualize_top_words(word_counts)

if __name__ == "__main__":
    main()
