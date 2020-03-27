from doubly_linked_list import DoublyLinkedList

"""
So this is basically a queue with a fixed size. FIFO.
I should check the length of the queue, maybe that's what current is for?
If current < capacity, just add the item to the head of the queue.
If the current = capacity, remove an item from the tail, then add to head.

I actually misunderstood. Looking at the tests, I understand it more.

It doesn't push out the oldest, it replaces them 
"""
class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = None
		self.storage = DoublyLinkedList()
	def append(self, item):
		# If the capacity is not reached, we can just add it to the tail
		if self.storage.length < self.capacity:
			self.storage.add_to_tail(item)
			# We can keep the current at the head, beause that's what we'll replace
			self.current = self.storage.head
		else:
			# Once capacity is reached, we need to set the current node to the next
			# but, if the next is none, which means we're at the end, we need to replace
			# that item, then set curent to head again
			if self.current.next == None:
				self.current.value = item
				self.current = self.storage.head
				# previous = self.current.prev
				# self.storage.delete(self.current)
				# previous.insert_after(item)
				# self.current = self.storage.head
			# else, if the next node is not the head
			else:
				self.current.value = item
				self.current = self.current.next


				# creating a temp variable for the next node
				# self.current.insert_before(item)
				# next = self.current.next
				# self.storage.delete(self.current)
				# self.current = next
				
				# next = self.current.next
				# self.storage.delete(self.current)
				# self.current = next
				# self.storage.length +=1
				# self.current.insert_before(item)

				# next = self.current.next
				# self.storage.delete(self.current)
				# self.current = next
				# self.storage.length +=1
				# self.current.insert_before(item)


				# next = self.current.next
				# self.current = next
				# self.storage.delete(next.prev)


	def get(self):
		list_buffer_contents = []
		start_value = self.storage.head.value
		current = self.storage.head
		while current is not None:
			list_buffer_contents.append(current.value)
			current = current.next
		# print(len(list_buffer_contents))
		# print(list_buffer_contents)
		return list_buffer_contents










# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
	def __init__(self, capacity):
		pass

	def append(self, item):
		pass

	def get(self):
		pass
