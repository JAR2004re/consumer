import threading
import queue
import time
# Define a shared queue
shared_queue = queue.Queue()
# Define a producer function
def producer():
    for i in range(10):
        # Produce some data
        data = f"Data {i}"
        print(f"Produced: {data}")

        # Put the data into the shared queue
        shared_queue.put(data)

        # Sleep for some time to simulate production time
        time.sleep(1)
# Define a consumer function
def consumer():
    while True:
        # Get data from the shared queue
        data = shared_queue.get()

        # Consume the data
        print(f"Consumed: {data}")

        # Sleep for some time to simulate consumption time
        time.sleep(2)

        # Mark the data as consumed
        shared_queue.task_done()
# Create and start the producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
# Wait for the producer thread to finish
producer_thread.join()
# Wait for the shared queue to be empty
shared_queue.join()
# Print a message indicating that the program has finished
print("Program finished.")