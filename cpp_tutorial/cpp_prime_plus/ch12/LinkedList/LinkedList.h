#pragma once
#include <iostream>
#include "Node.h"

class LinkedList
{
	enum { LIMIT = 10 };

public:
	LinkedList();
	~LinkedList();

	bool IsEmpty() const;
	bool IsFull() const;
	size_t Size() const;
	bool Append(Item item);
	bool Insert(size_t index, Item item);
	bool Remove(size_t index);
	
	friend std::ostream& operator<<(std::ostream& os, const LinkedList& rhs);

private:
	size_t mSize;
	size_t mCapacity;
	Node* mFront;
	Node* mRear;

	LinkedList(const LinkedList& other);
	LinkedList& operator=(const LinkedList& rhs);
};
