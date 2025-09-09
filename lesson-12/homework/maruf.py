Exercise 1: Threaded Prime Number Checker
import threading
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_primes(start, end, result_list):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    result_list.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    results = []
    # List to hold primes found by all threads
    primes_found = []

    # Calculate size of each chunk
    range_size = (end - start) // num_threads
    for i in range(num_threads):
        chunk_start = start + i * range_size
        # Make sure the last thread covers up to 'end'
        chunk_end = start + (i + 1) * range_size if i != num_threads - 1 else end
        thread_result = []
        t = threading.Thread(target=check_primes, args=(chunk_start, chunk_end, thread_result))
        threads.append((t, thread_result))
        t.start()

    for t, thread_result in threads:
        t.join()
        primes_found.extend(thread_result)

    primes_found.sort()
    return primes_found

if __name__ == "__main__":
    start_range = 1
    end_range = 100
    num_threads = 4

    primes = threaded_prime_checker(start_range, end_range, num_threads)
    print(f"Prime numbers between {start_range} and {end_range}:\n{primes}")

Exercise 2: Threaded File Processing - Word Count
import threading
from collections import Counter

def count_words(lines, result_list):
    word_counter = Counter()
    for line in lines:
        words = line.strip().split()
        word_counter.update(words)
    result_list.append(word_counter)

def threaded_word_count(file_path, num_threads=4):
    # Read all lines from file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else total_lines
        thread_result = []
        t = threading.Thread(target=count_words, args=(lines[start:end], thread_result))
        threads.append((t, thread_result))
        t.start()

    combined_counter = Counter()
    for t, thread_result in threads:
        t.join()
        combined_counter.update(thread_result[0])

    return combined_counter

if __name__ == "__main__":
    file_path = "large_text.txt"  # Replace with your file path
    num_threads = 4

    word_counts = threaded_word_count(file_path, num_threads)
    print("Word count summary:")
    for word, count in word_counts.most_common():
        print(f"{word}: {count}")
