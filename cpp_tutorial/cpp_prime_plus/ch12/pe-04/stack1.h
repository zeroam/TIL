// stack1.h -- ���� ADT�� ���� Ŭ���� ����
#pragma once

typedef unsigned long Item;

class Stack
{
public:
	Stack(int n = MAX);		// n���� ���Ҹ� ���� ������ �����Ѵ�
	Stack(const Stack& st);
	~Stack();
	bool isempty() const;
	bool isfull() const;
	// push()�� ������ ���� �� ������ false��, �ƴϸ� true�� �����Ѵ�
	bool push(const Item& item);	// ���ÿ� �׸��� �߰��Ѵ�
	// pop()�� ������ ��� ������ flase��, �ƴϸ� true�� �����Ѵ�
	bool pop(Item& item);			// ����� �׸��� ���� item�� �ִ´�
	Stack& operator=(const Stack& st);

private:
	enum { MAX = 10 };
	Item* pitems;
	int size;
	int top;
};
