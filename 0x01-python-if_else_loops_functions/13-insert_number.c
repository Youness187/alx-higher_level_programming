#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current, *hnext;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	current = *head;
	hnext = *head->next;

	while (current && hnext)
	{
		if (number >= current->n && number <= hnext->n)
		{
			current->next = new;
			new->next = hnext;
			return (new);
		}
		current = hnext;
		hnext = hnext->next;
	}
	current->next = new;
	return (new);
}
