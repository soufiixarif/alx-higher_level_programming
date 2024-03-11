#include "lists.h"
int check_cycle(listint_t *list)
{
    listint_t *tmp;

    tmp = list;
    while (tmp)
    {
        tmp = tmp->next;
        if(tmp == NULL)
            return(0);
        else if(tmp == list)
            return(1);
    }
    return(0);
}