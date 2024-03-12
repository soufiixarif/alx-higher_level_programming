#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node;
    listint_t *tmp;
    listint_t *ptr;

    node = malloc(sizeof (listint_t));
    if(!node)
        return (NULL);
    node->n = number;
    node->next = NULL;
    if(!*head)
        *head = node;
    tmp = *head;
    ptr = *head;
    while (tmp)
    {
        if (node->n < tmp->n)
        {
            ptr->next = node;
            node->next = tmp;
            return(node);
        }
        ptr = tmp;
        tmp = tmp->next;
    }
    return (NULL);
}