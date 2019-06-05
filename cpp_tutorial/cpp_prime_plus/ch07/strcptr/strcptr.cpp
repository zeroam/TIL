// strctfun.cpp -- ����ü �Ű������� �����ϴ� �����͸� ����ϴ� �Լ�
#include <iostream>
#include <cmath>

// ����ü ����
struct polar
{
	double distance;		// �������κ����� �Ÿ�
	double angle;			// ���������κ����� ����
};
struct rect
{
	double x;				// �������κ����� ����Ÿ�
	double y;				// �������κ����� �����Ÿ�
};

// �Լ� ����
polar rect_to_polar(const rect* pxy, polar* pda);
void show_polar(const polar* pda);

int main()
{
	using namespace std;
	rect rplace;
	polar pplace;

	cout << "x���� y���� �Է��Ͻʽÿ�: ";
	while (cin >> rplace.x >> rplace.y)
	{
		pplace = rect_to_polar(&rplace, &pplace);
		show_polar(&pplace);
		cout << "x���� y���� �Է��Ͻʽÿ� (�������� q�� �Է�): ";
	}
	cout << "���α׷��� �����մϴ�.\n";
	return 0;
}

// ���� �·Ḧ �� ��ǥ�� ��ȯ�Ѵ�
polar rect_to_polar(const rect* pxy, polar* pda)
{
	using namespace std;
	polar answer;

	answer.distance =
		sqrt(pxy->x * pxy->x + pxy->y * pxy->y);
	answer.angle = atan2(pxy->y, pxy->x);
	return answer;
}

// ���� ������ �� ������ ��ȯ�Ͽ� �� �·Ḧ ����Ѵ�
void show_polar(const polar* pda)
{
	using namespace std;
	const double Rad_to_deg = 57.29577951;

	cout << "�Ÿ� = " << pda->distance;
	cout << ", ���� = " << pda->angle * Rad_to_deg;
	cout << "��\n";
}
