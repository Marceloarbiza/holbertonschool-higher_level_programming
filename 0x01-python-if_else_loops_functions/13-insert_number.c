#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
* insert_nodeint_at_index - add node index
* @head: listint_t
* @n: int
* @idx: int
* Return: listint_t
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *h = NULL, *new = NULL;

    if (head == NULL)
        return (NULL);

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);

    h = *head;
    new->n = number;
    new->next = NULL;

    if (!h || new->n < h->n)
    {
        new->next = *head;
        *head = new;
        return (new);
    }

    while (h)
    {
        if (!h || new->n < h->next->n)
        {
            new->next = h->next;
            h->next = new;
            return (h);
        }
        h = h->next;
    }
    free(new);
    return (NULL);
}
