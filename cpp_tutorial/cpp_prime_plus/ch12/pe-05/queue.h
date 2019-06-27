// queue.h -- 큐를 위한 인터페이스
#pragma once

// 이 큐는 Customer 항목들을 포함하게 된다
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
	// 클래스 사용 범위의 정의들
	// Node는 이 클래스에 지역적인, 내포된 구조체 정의이다
	struct Node { Item item; Node* next; };
	enum { Q_SIZE = 10 };

	// private 클래스 멤버들
	Node* front;
	Node* rear;
	int items;
	const int qsize;

	// public 복사를 방지하는 선점 정의
	Queue(const Queue& q) : qsize(0) { }
	Queue& operator=(const Queue& q) { return *this; }
};
