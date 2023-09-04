#include "lists.h"
/**
 * check_cycle - check cycle
 * @list: lists
 * Return: int
*/
int check_cycle(listint_t *list);
{
listint_t *sabik;
listint_t *lahik;

sabik = list;
lahik = sabik;
while (sabik && sabik->next)
{
lahik = lahik->next;
sabik = sabik->next->next;
if (sabik == lahik)
{
return (1);
}
}
return (0);
}
