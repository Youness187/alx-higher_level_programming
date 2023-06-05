#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *tmp = list;

	while (tmp)
	{
		tmp = tmp->next;

		if (tmp == NULL)
			return (0);
		else if (tmp == head)
			return (1);
	}
	return (0);
}

