// stack1.h -- 스택 ADT를 위한 클래스 선언
#pragma once

typedef unsigned long Item;

class Stack
{
public:
	Stack(int n = MAX);		// n개의 원소를 가진 스택을 생성한다
	Stack(const Stack& st);
	~Stack();
	bool isempty() const;
	bool isfull() const;
	// push()는 스택이 가득 차 있으면 false를, 아니면 true를 리턴한다
	bool push(const Item& item);	// 스택에 항목을 추가한다
	// pop()은 스택이 비어 있으면 flase를, 아니면 true를 리턴한다
	bool pop(Item& item);			// 꼭대기 항목을 꺼내 item에 넣는다
	Stack& operator=(const Stack& st);

private:
	enum { MAX = 10 };
	Item* pitems;
	int size;
	int top;
};
