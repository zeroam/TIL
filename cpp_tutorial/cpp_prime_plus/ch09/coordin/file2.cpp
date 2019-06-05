// file2.cpp -- file1.cpp���� ȣ��Ǵ� �Լ��� ��� �ִ�
#include <iostream>
#include <cmath>
#include "coordin.h"

// ���� ��ǥ�� �� ��ǥ�� ��ȯ�Ѵ�
polar rect_to_polar(rect xypos)
{
	using namespace std;
	polar answer;

	answer.distance =
		sqrt(xypos.x * xypos.x + xypos.y * xypos.y);
	answer.angle = std::atan2(xypos.y, xypos.x);
	return answer;			// polar�� ����ü�� �����Ѵ�
}

// ���� ������ �� ������ ��ȯ�Ͽ� �� ��ǥ�� ����Ѵ�
void show_polar(polar dapos)
{
	using namespace std;
	const double Rad_to_deg = 57.29577951;
	
	cout << "�Ÿ� = " << dapos.distance;
	cout << ", ���� = " << dapos.angle * Rad_to_deg;
	cout << "��\n";
}