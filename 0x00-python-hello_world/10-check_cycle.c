#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp;
	listint_t *ptr;

	tmp = list;
	ptr = list;
	if (!list)
		return (0);
	while (tmp)
	{
		tmp = tmp->next;
		if (tmp == NULL)
			return (0);
		else if (tmp == ptr)
			return (1);
	}
	return (0);
}
