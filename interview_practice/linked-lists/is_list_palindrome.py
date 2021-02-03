"""Goal: O(n) runtime using O(1) additional space

Given a singly linked list of integers, determine whether or not it's a palindrome.
"""
# Definition for singly-linked list:

class ListNode(object):
	def __init__(self, x):
		self.value = x
		self.next = None


def list_to_linked_list(l):
	"""return a linked list of integers provided in list l"""

	# instantiate the head node of the linked list
	head_node = ListNode(l.pop(0))

	# placeholder for the current node s.t. current_node.next can be defined iteratively
	current_node = head_node

	# iterate until every element of the list has been popped and added to the linked list
	while len(l) > 0:
		# Pop the next element of the list and instantiate a ListNode object with its value
		next_node = ListNode(l.pop(0))

		# Add that ListNode object as the next node of the current node
		current_node.next = next_node

		# Update the current_node placeholder with the next_node ListNode object
		current_node = next_node

		# Loop ends - if condition is not met, repeat

	return head_node


def isListPalindrome(l):
	"""return bool indicating if linked list l is a palindrome"""
	if l == None:
		return True

	placeholder_list = []
	current_node = l

	# iterate through linked list
	# at each node, add value to placeholder_list. 
	# If it is the tail node, break the loop.
	# Otherwise, update current_node placeholder and repeat.
	while True:
		placeholder_list.append(current_node.value)
		if current_node.next == None:
			break
		current_node = current_node.next

	return placeholder_list == list(reversed(placeholder_list))


# Testing
l = [0, 1, 0]

ll = list_to_linked_list(l)

print(isListPalindrome(ll))

