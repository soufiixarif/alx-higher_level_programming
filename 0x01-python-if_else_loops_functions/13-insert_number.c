#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node;
    listint_t *tmp;

    node = malloc(sizeof (listint_t));
    if(!node)
        return (NULL);
    node->n = number;
    node->next = NULL;
    if(!*head)
        *head = node;
    tmp = *head;
    if (node->n < (*head)->n)
        {
            node->next = tmp;
            *head = node;
            return(node);
        }
    while (tmp->next && tmp->next->n < number) 
    {
        tmp = tmp->next;
    }

    node->next = tmp->next;
    tmp->next = node;

    return node;
    return (NULL);
}