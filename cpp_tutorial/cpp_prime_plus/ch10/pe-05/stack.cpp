#include "stack.h"

Stack::Stack()
	: top(0)
{
}

bool Stack::IsEmpty() const
{
	return top == 0;
}

bool Stack::IsFull() const
{
	return top == MAX;
}

bool Stack::push(const Item& item)
{
	if (IsFull())
	{
		return false;
	}

	items[top++] = item;
	return true;
}

bool Stack::pop(Item& item)
{
	if (IsEmpty())
	{
		return false;
	}

	item = items[--top];
	return true;
}