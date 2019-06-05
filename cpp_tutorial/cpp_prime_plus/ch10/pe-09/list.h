#pragma once

class List
{
public:
	List();
	~List();

	bool Append();
	bool Delete();
	bool IsFull();
	bool IsEmpty();
	bool Show();

private:
	enum { MAX = 10 };
	void* mItems[MAX];
	int mSize;
};