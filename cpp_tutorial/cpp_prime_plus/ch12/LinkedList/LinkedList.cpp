#include "LinkedList.h"

LinkedList::LinkedList()
	: mSize(0)
	, mCapacity(LIMIT)
	, mFront(nullptr)
	, mRear(nullptr)
{
}

LinkedList::~LinkedList()
{
	Node* temp;
	while (mFront != nullptr)
	{
		temp = mFront;
		mFront = mFront->next;
		delete temp;
	}
}

bool LinkedList::IsEmpty() const
{
	return mSize == 0;
}

bool LinkedList::IsFull() const
{
	return mSize == mCapacity;
}

size_t LinkedList::Size() const
{
	return mSize;
}

bool LinkedList::Append(Item item)
{
	// 꽉 찼으면
	if (IsFull())
	{
		return false;
	}

	Node* add = new Node;
	add->item = item;
	add->next = nullptr;
	// 아무것도 없으면
	if (mFront == nullptr)
	{
		mFront = add;
	}
	else
	{
		mRear->next = add;
	}
	mRear = add;
	mSize++;

	return true;
}

bool LinkedList::Insert(size_t index, Item item)
{
	if (IsFull())
	{
		return false;
	}

	if (index >= mSize || mSize == 0)
	{
		return false;
	}

	Node* add = new Node;
	add->item = item;

	if (index == 0)
	{
		add->next = mFront;
		mFront = add;
	}
	else
	{
		Node* before = mFront;
		Node* after = mFront->next;

		before->next = add;
		add->next = after;
	}
	mSize++;

	return true;
}

bool LinkedList::Remove(size_t index)
{
	if (IsEmpty())
	{
		return false;
	}

	
	if (index == 0)
	{
		Node* temp;
		temp = mFront;
		mFront = mFront->next;
		delete temp;
	}
	else 
	{
		Node* before = mFront;
		Node* cur = mFront->next;
		Node* after = cur->next;

		for (size_t i = 1; i < index; i++)
		{
			before = cur;
			cur = after;
			after = cur->next;
		}

		before->next = after;
		delete cur;
	}
	
	mSize--;
	if (mSize == 0)
	{
		mRear = nullptr;
	}

	return true;
}

std::ostream& operator<<(std::ostream& os, const LinkedList& rhs)
{
	Node* temp = rhs.mFront;

	os << "( " << temp->item;
	for (size_t i = 1; i < rhs.mSize; i++)
	{
		temp = temp->next;
		os << ", " << temp->item;
	}
	os << " )";

	return os;
}