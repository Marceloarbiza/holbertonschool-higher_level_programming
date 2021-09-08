#include "lists.h"
/**
 * check_cycle - turtle-hare
 * @list: list
 * Return: int
 */
int check_cycle(listint_t *list)
{
    listint_t *tu = list, *ha = list;

    if (!list)
        return (0);

    while (tu && ha && ha->next)
    {
        tu = tu ->next;
        ha = ha->next->next;
        if (tu == ha)
            return (1);
    }
    return (0);
}
