// strctfun.cpp -- 구조체 매개변수를 지시하는 포인터를 사용하는 함수
#include <iostream>
#include <cmath>

// 구조체 선언
struct polar
{
	double distance;		// 원점으로부터의 거리
	double angle;			// 수평축으로부터의 각도
};
struct rect
{
	double x;				// 원점으로부터의 수평거리
	double y;				// 원점으로부터의 수직거리
};

// 함수 원형
polar rect_to_polar(const rect* pxy, polar* pda);
void show_polar(const polar* pda);

int main()
{
	using namespace std;
	rect rplace;
	polar pplace;

	cout << "x값과 y값을 입력하십시오: ";
	while (cin >> rplace.x >> rplace.y)
	{
		pplace = rect_to_polar(&rplace, &pplace);
		show_polar(&pplace);
		cout << "x값과 y값을 입력하십시오 (끝내려면 q를 입력): ";
	}
	cout << "프로그램을 종료합니다.\n";
	return 0;
}

// 직각 좌료를 극 좌표로 변환한다
polar rect_to_polar(const rect* pxy, polar* pda)
{
	using namespace std;
	polar answer;

	answer.distance =
		sqrt(pxy->x * pxy->x + pxy->y * pxy->y);
	answer.angle = atan2(pxy->y, pxy->x);
	return answer;
}

// 라디안 단위를 도 단위로 변환하여 극 좌료를 출력한다
void show_polar(const polar* pda)
{
	using namespace std;
	const double Rad_to_deg = 57.29577951;

	cout << "거리 = " << pda->distance;
	cout << ", 각도 = " << pda->angle * Rad_to_deg;
	cout << "도\n";
}
