#include "07.h"
#include <iostream>

void num7::program()
{
	using namespace std;

	int num;

	cout << "몇 대의 차를 목록으로 관리하시겠습니까? ";
	cin >> num;
	
	// 동적으로 구조체 배열 생성
	car* cars = new car[num];
	//car** cars = new car*[num];

	for (int i = 0; i < num; i++)
	{
		cout << "자동차 #" << i + 1 << ":\n";
		cout << "제작업체 : ";
		cin >> cars[i].company;
		//cin >> cars[i]->company;
		cout << "제작년도 : ";
		cin >> cars[i].year;
	}

	cout << "현재 귀하가 보유하고 있는 자동차 목록은 다음과 같습니다." << endl;
	for (int i = 0; i < num; i++)
	{
		cout << cars[i].year << "년형 " << cars[i].company << endl;
	}
}
