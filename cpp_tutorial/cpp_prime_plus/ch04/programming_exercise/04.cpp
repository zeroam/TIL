#include "04.h"
#include <iostream>
#include <string>

void exercise::number4()
{
	using namespace std;

	string first_name;
	string last_name;
	string full_name;

	cout << "퍼스트 네임 (이름)을 입력하시오: ";
	getline(cin, first_name);
	cout << "라스트 네임 (성)을 입력하시오: ";
	getline(cin, last_name);

	full_name = last_name + ", " + first_name;
	cout << "하나의 문자열로 만들면: " << full_name << endl;
}