#include "lists.h"
/**
 * is_palindrome- checks whether a singly linked list is a palindrome
 * @head: pointer to head element in asingly linked list
 * Return: 1 if is palindrome and 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *head_ptr;
	listint_t *tail_ptr;
	int head_counter = 0;
	int tail_counter = 0;

	head_ptr = *head;
	tail_ptr = *head;

	while(tail_ptr->next != NULL)
	{
		tail_counter++;
		tail_ptr = tail_ptr->next;
	}
	for(head_counter)
}
