import multiprocessing

def process_file(file_path, keywords, queue):
    result_dict = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    if keyword in result_dict:
                        result_dict[keyword].append(file_path)
                    else:
                        result_dict[keyword] = [file_path]
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    queue.put(result_dict)

def multiprocessing_search(file_path, keywords):
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=process_file, args=(file_path, keywords, queue))
    process.start()
    process.join()
    result_dict = queue.get()
    return result_dict

# Обгорнення основної логіки в if __name__ == '__main__': для безпечного запуску мультипроцесінгу
if __name__ == '__main__':
    keywords = ['example', 'test']
    results = multiprocessing_search('text.txt', keywords)
    print(results)
