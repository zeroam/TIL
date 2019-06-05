#pragma once

struct customer
{
	char fullname[35];
	double payment;
};

typedef customer Item;

class Stack
{
public:
	Stack();

	bool IsEmpty() const;
	bool IsFull() const;
	bool push(const Item& item);
	bool pop(Item& item);

private:
	enum { MAX = 10 };
	Item items[MAX];
	int top;
};
