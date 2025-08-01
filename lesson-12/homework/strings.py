import threading


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_primes_in_range(start, end, result_list):
    for num in range(start, end):
        if is_prime(num):
            result_list.append(num)


def find_primes_in_range(start, end, num_threads):
    threads = []
    result = []

    
    result_lock = threading.Lock()
    shared_result = []

    
    step = (end - start) // num_threads

    for i in range(num_threads):
        range_start = start + i * step
        range_end = start + (i + 1) * step if i < num_threads - 1 else end

        
        def thread_task(rs=range_start, re=range_end):
            local_result = []
            check_primes_in_range(rs, re, local_result)
            with result_lock:
                shared_result.extend(local_result)

        thread = threading.Thread(target=thread_task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sorted(shared_result)

if __name__ == "__main__":
    start_range = 10
    end_range = 100
    num_threads = 4

    primes = find_primes_in_range(start_range, end_range, num_threads)
    print(f"Prime numbers between {start_range} and {end_range}:")
    print(primes)









import threading
from collections import Counter
import os


def count_words(lines, local_counter):
    for line in lines:
        words = line.strip().lower().split()
        local_counter.update(words)


def threaded_word_count(file_path, num_threads=4):
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    counters = []

    for i in range(num_threads):
        start_index = i * chunk_size
        
        end_index = (i + 1) * chunk_size if i < num_threads - 1 else total_lines
        chunk_lines = lines[start_index:end_index]
        
        local_counter = Counter()
        thread = threading.Thread(target=count_words, args=(chunk_lines, local_counter))
        threads.append((thread, local_counter))
        thread.start()

    
    for thread, _ in threads:
        thread.join()

    
    global_counter = Counter()
    for _, local_counter in threads:
        global_counter.update(local_counter)

    return global_counter


if __name__ == "__main__":
    file_path = "msg.txt"  

    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found. Please provide a valid file path.")
    else:
        word_counts = threaded_word_count(file_path, num_threads=4)
        print("Top 20 most common words:")
        for word, count in word_counts.most_common(20):
            print(f"{word}: {count}")
