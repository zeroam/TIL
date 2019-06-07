// stack.h -- 스택 ADT를 위한 클래스 정의
#pragma once

typedef unsigned long Item;

class Stack
{
public:
	Stack();
	bool isempty() const;
	bool isfull() const;
	// push()는 스택이 가득 차 있으면 false를, 아니면 true를 리턴한다
	bool push(const Item& item);	// 스택에 항목을 추가한다
	// pop()은 스택이 비어 있으면 false를, 아니면 true를 리턴한다
	bool pop(Item& item);			// 꼭대기 항목을 꺼내 item에 넣는다

private:
	enum {MAX = 10};
	Item items[MAX];
	int top;
};
