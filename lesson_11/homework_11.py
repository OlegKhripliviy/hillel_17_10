from threading import Thread

result_list = []


def get_primes(start: int, end: int) -> list[int]:
    results = []
    for number in range(start, end + 1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            results.append(number)
    [result_list.append(i) for i in results]
    return results


def run_threads(start, stop, num_of_threads):
    threads: list[Thread] = []
    step = int((stop - start) / num_of_threads)

    for i in range(1, num_of_threads + 1):
        end = start + step
        threads.append(Thread(target=get_primes, args=(start, end)))
        start = end

    for thread in threads:
        thread.start()
        thread.join()


run_threads(10, 20, 5)
print(result_list)
