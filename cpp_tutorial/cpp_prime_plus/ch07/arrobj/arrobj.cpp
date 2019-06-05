// arrobj.cpp -- C++11�� array ��ü�� ���� ���
#include <iostream>
#include <array>
#include <string>
// ��� (constant) ������

const int Seasons = 4;
const std::array<std::string, Seasons> Sname =
	{ "Spring", "Summer", "Fall", "Winter" };

// array ��ü�� �����ϴ� ���
void fill(std::array<double, Seasons>* pa);
// �������� �ʰ� ��ü�� ����ϴ� ���
void show(std::array<double, Seasons> da);

int main()
{
	std::array<double, Seasons> expenses;
	fill(&expenses);
	show(expenses);
	return 0;
}

void fill(std::array<double, Seasons>* pa)
{
	using namespace std;
	for (int i = 0; i < Seasons; i++)
	{
		cout << Sname[i] << "�� �ҿ�Ǵ� ���: ";
		cin >> (*pa)[i];
	}
}

void show(std::array<double, Seasons> da)
{
	using namespace std;
	double total = 0.0;
	cout << "\n������ ���\n";
	for (int i = 0; i < Seasons; i++)
	{
		cout << Sname[i] << " : $" << da[i] << endl;
		total += da[i];
	}
	cout << "�� ��� : $" << total << endl;
}