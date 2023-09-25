#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle- checks whether a linked list has a cycle
 * @list: the first node in the linked list
 * Return: 0 if no cycle in list and 1 if there's a cycle
 */

int check_cycle(listint_t *list)
{
	int i = 0;
	int first_node_n = list->n;
	listint_s second_node = list->next;

	while (list->n != NULL)
	{
		if (i != 0 && list->n == first_node_n && list->next == second_node)
		{
			return (1);
		}
		i++;
	}
	return (0);
}
