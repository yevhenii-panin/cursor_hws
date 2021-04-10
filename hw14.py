import glob
import time
from concurrent.futures import ThreadPoolExecutor


def find_by_pattern(filename, pattern):
    line_container = set()
    with open(filename) as f:
        for line in f:
            if pattern in line:
                line_container.add(line)
    return line_container


def find_all_files(directory_path, pattern):
    files = glob.glob(f'{directory_path}\**\*.py', recursive=True)
    container = set()
    with ThreadPoolExecutor(5) as pool:
        result = pool.map(find_by_pattern, files, pattern)
        for res in result:
            container.update(res)
    return container


if __name__ == "__main__":
    start = time.time()
    # your directory
    search_by_pattern = find_all_files("C:/Users/YPanin01/PycharmProjects/pythonProject5", pattern='import')
    end_time = time.time() - start
    for line in search_by_pattern:
        print(line)
    print(f'search time {end_time} seconds in 5 threads')
