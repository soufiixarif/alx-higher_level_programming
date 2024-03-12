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
    if (!head)
        return(NULL);
    if(!*head)
    {
        *head = node;
        return (NULL);
    }
    else if (node->n < (*head)->n)
        {
            node->next = *head;
            *head = node;
            return(node);
        }
    tmp = *head;
    while (tmp->next && tmp->next->n < number) 
    {
        tmp = tmp->next;
    }

    node->next = tmp->next;
    tmp->next = node;

    return node;
    return (NULL);
}