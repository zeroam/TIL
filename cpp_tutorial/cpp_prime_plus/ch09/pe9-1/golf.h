#pragma once

const int Len = 40;
struct golf
{
	char fullname[Len];
	int handicap;
};

// 비대화식 버전:
// 이 함수는 ㅐ개변수로 전달된 값들을 사용하여
// golf 구조체를 제공된 이름과 핸디캡으로 설정한다
void setgolf(golf& g, const char* name, int hc);

// 대화식 버전:
// 이 함수는 사용자에게 이름과 핸디캡을 묻는다
// g의 멤버들으 입력된 값으로 설정한다
// 이름이 입력되면 1을 리턴하고, 이름이 빈 문자열이면 0을 리턴한다
int setgolf(golf& g);

// 이 함수는 handicap을 새로운 값으로 설정한다
void handicap(golf& g, int hc);

// 이 함수는 golf 구조체의 내용을 출력한다
void showgolf(const golf& g);
