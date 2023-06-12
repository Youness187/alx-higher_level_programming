#include "lists.h"
/**
 * comp_s_e - compare start and end
 * @head: start
 * @end: end
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int comp_s_e(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (comp_s_e(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	return (comp_s_e(head, *head));
}
