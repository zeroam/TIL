// stack.h -- ���� ADT�� ���� Ŭ���� ����
#pragma once

typedef unsigned long Item;

class Stack
{
public:
	Stack();
	bool isempty() const;
	bool isfull() const;
	// push()�� ������ ���� �� ������ false��, �ƴϸ� true�� �����Ѵ�
	bool push(const Item& item);	// ���ÿ� �׸��� �߰��Ѵ�
	// pop()�� ������ ��� ������ false��, �ƴϸ� true�� �����Ѵ�
	bool pop(Item& item);			// ����� �׸��� ���� item�� �ִ´�

private:
	enum {MAX = 10};
	Item items[MAX];
	int top;
};
