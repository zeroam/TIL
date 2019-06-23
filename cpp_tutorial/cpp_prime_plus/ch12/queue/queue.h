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
	long arrive;			// ���� ť�� ������ �ð�
	int processtime;		// ���� �ŷ��� ó���ϴ� �ð�
};

typedef Customer Item;

class Queue
{
	// Ŭ���� ��� ������ ���ǵ�
	// Node�� �� Ŭ������ ��������, ������ ����ü �����̴�
	struct Node { Item item; Node* next; };
	enum { Q_SIZE = 10 };

public:
	Queue(int qs = Q_SIZE);		// qs �Ѱ踦 ���� ť�� �����Ѵ�
	~Queue();
	bool isempty() const;
	bool isfull() const;
	int queuecount() const;
	bool enqueue(const Item& item);	// �׸��� ������ �߰��Ѵ�
	bool dequeue(Item& item);		// �Ӹ����� �׸��� �����Ѵ�

private:
	Node* front;				// Queue�� �Ӹ��� �����ϴ� ������
	Node* rear;					// Queue�� ������ �����ϴ� ������
	int items;					// Queue�� �ִ� ���� �׸� ��
	const int qsize;			// Queue�� ���� �� �ִ� �ִ� �׸� ��
	// public ���縦 �����ϴ� ���� ����
	Queue(const Queue& q) : qsize(0) {}
	Queue& operator=(const Queue& q) { return *this; }
};