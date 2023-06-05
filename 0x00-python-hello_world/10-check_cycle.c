#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *tmp;

	if (!list || !list->next)
		return (0);
	head = list->next;
	tmp = head->next;

	while (tmp && head && tmp->next)
	{
		if (tmp == head)
			return (1);
		head = head->next;
		tmp = tmp->next->next;
	}
	return (0);
}

