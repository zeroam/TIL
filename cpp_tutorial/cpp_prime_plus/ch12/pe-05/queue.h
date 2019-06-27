// queue.h -- ť�� ���� �������̽�
#pragma once

// �� ť�� Customer �׸���� �����ϰ� �ȴ�
class Customer
{
public:
	Customer() { arrive = processtime = 0; }
	void set(long when);
	long when() const { return arrive; }
	int ptime() const { return processtime; }

private:
	long arrive;
	int processtime;
};

typedef Customer Item;

class Queue
{
public:
	Queue(int qs = Q_SIZE);
	~Queue();
	bool isempty() const;
	bool isfull() const;
	int queuecount() const;
	bool enqueue(const Item& item);
	bool dequeue(Item& item);

private:
	// Ŭ���� ��� ������ ���ǵ�
	// Node�� �� Ŭ������ ��������, ������ ����ü �����̴�
	struct Node { Item item; Node* next; };
	enum { Q_SIZE = 10 };

	// private Ŭ���� �����
	Node* front;
	Node* rear;
	int items;
	const int qsize;

	// public ���縦 �����ϴ� ���� ����
	Queue(const Queue& q) : qsize(0) { }
	Queue& operator=(const Queue& q) { return *this; }
};
