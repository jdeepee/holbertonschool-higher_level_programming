import time
import random
from threading import Lock

class Store:
    def __init__(self, item_number, person_capacity):
        self.items_remaining_lock = Lock()
        self.space_available_lock = Lock()
        self.item_number = item_number
        self.person_capacity = person_capacity
        self.items_remaining = self.item_number
        self.space_available = self.person_capacity

    def enter(self):
        while True:
            self.space_available_lock.acquire()
            if self.space_available > 0:
                self.space_available -= 1
                self.space_available_lock.release()
                break
                
            self.space_available_lock.release()

    def buy(self):
        self.items_remaining_lock.acquire()

        if self.items_remaining <= 0:
            return False

        self.items_remaining_lock.release()
        time.sleep(random.randint(5, 10))
        self.items_remaining_lock.acquire()

        if self.items_remaining <= 0:
            return False

        self.items_remaining -= 1
        self.items_remaining_lock.release()
        self.space_available_lock.acquire()
        self.space_available += 1
        self.space_available_lock.release()
        return True