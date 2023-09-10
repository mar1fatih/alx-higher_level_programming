#include "lists.h"
/**
 * is_palindrome - check the code
 * @head: head
 * Return: 0 if palindrome 1 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *ptr = NULL;
	int s = 0, i = 0;

	if (!(*head))
	{
		return (1);
	}
	current = *head;
	while (current)
	{
		current = current->next;
		s++;
	}
	ptr = malloc(sizeof(int) * s);
	if (!ptr)
	{
		printf("failed to allocate");
		return(0);
	}
	current = *head;
	while (current)
	{
		ptr[i] = current->n;
		current = current->next;
		i++;
	}
	current = *head;
	s--;
	while (current)
	{
		if (current->n != ptr[s])
		{
			free(ptr);
			return (0);
		}
		current = current->next;
		s--;
	}
	free(ptr);
	return (1);
}
