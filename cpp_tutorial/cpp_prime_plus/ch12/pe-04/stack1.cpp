#include "stack1.h"

Stack::Stack(int n)
	: top(0)
	, size(n)
{
	if (size <= 0)
	{
		size = MAX;
	}

	pitems = new Item[size];
}

Stack::Stack(const Stack& other)
	: top(other.top)
	, size(other.size)
{
	pitems = new Item[size];
	for (int i = 0; i < size; i++)
	{
		pitems[i] = other.pitems[i];
	}
}

Stack::~Stack()
{
	delete[] pitems;
}

bool Stack::isempty() const
{
	return top == 0;
}

bool Stack::isfull() const
{
	return top == size;
}

bool Stack::push(const Item& item)
{
	if (top >= size)
	{
		return false;
	}
	
	pitems[top++] = item;
	return true;
}

bool Stack::pop(Item& item)
{
	if (top <= 0)
	{
		return false;
	}
	item = pitems[--top];
	return true;
}

Stack& Stack::operator=(const Stack& rhs)
{
	if (this == &rhs)
	{
		return *this;
	}

	delete[] pitems;

	size = rhs.size;
	top = rhs.top;
	
	pitems = new Item[size];
	for (int i = 0; i < size; i++)
	{
		pitems[i] = rhs.pitems[i];
	}

	return *this;
}