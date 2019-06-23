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
	long arrive;			// 고객이 큐에 도착한 시간
	int processtime;		// 고객의 거래를 처리하는 시간
};

typedef Customer Item;

class Queue
{
	// 클래스 사용 범위의 정의들
	// Node는 이 클래스에 지역적인, 내포된 구조체 정의이다
	struct Node { Item item; Node* next; };
	enum { Q_SIZE = 10 };

public:
	Queue(int qs = Q_SIZE);		// qs 한계를 가진 큐를 생성한다
	~Queue();
	bool isempty() const;
	bool isfull() const;
	int queuecount() const;
	bool enqueue(const Item& item);	// 항목을 꼬리에 추가한다
	bool dequeue(Item& item);		// 머리에서 항목을 삭제한다

private:
	Node* front;				// Queue의 머리를 지시하는 포인터
	Node* rear;					// Queue의 꼬리를 지시하는 포인터
	int items;					// Queue에 있는 현재 항목 수
	const int qsize;			// Queue에 넣을 수 있는 최대 항목 수
	// public 복사를 방지하는 선점 정의
	Queue(const Queue& q) : qsize(0) {}
	Queue& operator=(const Queue& q) { return *this; }
};