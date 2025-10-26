import threading
import time
import random

central_inventory = 0
inventory_lock = threading.Lock()
MAX_CAPACITY = 100
PRODUCERS = 2
CONSUMERS = 3

def producer(name):
    global central_inventory
    while True:
        time.sleep(random.uniform(0.5, 2))
        items = random.randint(1, 10)
        with inventory_lock:
            if central_inventory + items <= MAX_CAPACITY:
                central_inventory += items
                print(f"[Producer {name}] Added {items} items. Central Inventory: {central_inventory}")
            else:
                print(f"[Producer {name}] Cannot add {items} items. Inventory Full ({central_inventory})")

def consumer(name):
    global central_inventory
    while True:
        time.sleep(random.uniform(0.5, 3))
        items = random.randint(1, 5)
        with inventory_lock:
            if central_inventory >= items:
                central_inventory -= items
                print(f"[Consumer {name}] Bought {items} items. Central Inventory: {central_inventory}")
            else:
                print(f"[Consumer {name}] Not enough inventory for {items} items. Current stock: {central_inventory}")

producer_threads = []
for i in range(PRODUCERS):
    t = threading.Thread(target=producer, args=(i+1,))
    t.daemon = True
    t.start()
    producer_threads.append(t)

consumer_threads = []
for i in range(CONSUMERS):
    t = threading.Thread(target=consumer, args=(i+1,))
    t.daemon = True
    t.start()
    consumer_threads.append(t)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Simulation stopped.")
