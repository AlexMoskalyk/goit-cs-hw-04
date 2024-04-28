import threading

def search_in_file(file_path, keywords, result_dict, lock):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    with lock:
                        if keyword in result_dict:
                            result_dict[keyword].append(file_path)
                        else:
                            result_dict[keyword] = [file_path]
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def threaded_search(file_path, keywords):
    result_dict = {}
    lock = threading.Lock()
    thread = threading.Thread(target=search_in_file, args=(file_path, keywords, result_dict, lock))
    thread.start()
    thread.join()
    return result_dict

keywords = ['example', 'test']
results = threaded_search('text.txt', keywords)
print(results)
