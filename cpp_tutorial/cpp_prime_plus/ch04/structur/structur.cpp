// structur.cpp -- ������ ����ü
#include <iostream>

struct inflatable
{
	char name[20];
	float volume;
	double price;
};

int main()
{
	using namespace std;
	inflatable guest =
	{
		"Glorious Gloria",	// name ��
		1.88,				// volume ��
		29.99				// price ��
	};	// guest�� inflatable���� ����ü �����̴�.

	inflatable pal =
	{
		"Audacious Arthur",
		3.12,
		32.99
	};

	cout << "���� �Ǹ��ϰ� �ִ� ����ǳ����\n" << guest.name;
	cout << "�� " << pal.name << "�Դϴ�.\n";
	cout << "�� ��ǰ�� $";
	cout << guest.price + pal.price << "�� �帮�ڽ��ϴ�!\n";

	return 0;
}