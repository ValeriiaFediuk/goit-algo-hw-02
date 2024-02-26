import queue
import time

def generate_request(queue):
    request = "Нова заявка"
    queue.put(request)
    print("Додано нову заявку до черги:", request)

def process_request(queue):
    if not queue.empty():
        request = queue.get()
        print("Оброблено заявку:", request)
    else:
        print("Черга порожня. Заявок на обробку немає.")

def main():
    request_queue = queue.Queue()

    while True:
        generate_request(request_queue)
        process_request(request_queue)
        time.sleep(2)

if __name__ == "__main__":
    main()
