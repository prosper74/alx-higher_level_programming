#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked list
 * has a cycle in it.
 * @list_head: head of linked list
 *
 * Return: return 1 if cycle detected, 0 otherwise
 */

int check_cycle(listint_t *list_head)
{
	listint_t *slow_ptr, *fast_ptr;

	if (!list_head)
		return (0);

	slow_ptr = list_head;
	fast_ptr = list_head->next;
	while (fast_ptr && slow_ptr && fast_ptr->next)
	{
		if (slow_ptr == fast_ptr)
			return (1);

		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}

	return (0);
}

