// switch.cpp -- switch ����
#include <iostream>
using namespace std;
void showmenu();		// �Լ� ������
void report();
void comfort();
int main()
{
	showmenu();
	int choice;
	cin >> choice;
	while (choice != 5)
	{
		switch (choice)
		{
		case 1:
			cout << "\a\n";
			break;
		case 2:
			report();
			break;
		case 3:
			cout << "������� ���� ȸ�翡 ��̽��ϴ�.\n";
			break;
		case 4:
			comfort();
			break;
		default:
			cout << "�װ��� ������ �� �����ϴ�.\n";
		}
		showmenu();
		cin >> choice;
	}
	cout << "���α׷��� �����մϴ�.\n";
	return 0;
}

void showmenu()
{
	cout << "1, 2, 3, 4, 5 ���߿��� �ϳ��� �����Ͻʽÿ�:\n"
		"1) �����            2) ����\n"
		"3) �˸�����          4) �ݷ���\n"
		"5) ����\n";
}

void report()
{
	cout << "�̹� �б�� �濵 ������ ���� �����ϴ�.\n"
		"�Ǹŷ��� 120% �þ��, ����� 35% �پ����ϴ�.\n";
}

void comfort()
{
	cout << "������� ����� ���� �ְ��� CEO��� �����ϰ� �ֽ��ϴ�.\n"
		"�̻�ȸ�� ����� ���� �ְ��� CEO��� �����ϰ� �ֽ��ϴ�.\n";
}