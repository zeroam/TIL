// enum.cpp -- enum(����ü) ���
#include <iostream>
// 0���� 6���� �����ϴ� �̸��� �ִ� ����� �����
enum {red, orange, yellow, green, blue, violet, indigo};

int main()
{
	using namespace std;
	cout << "�÷� �ڵ�(0,1,2,3,4,5,6)�� �Է��Ͻʽÿ�: ";
	int code;
	cin >> code;
	while (code >= red && code <= indigo)
	{
		switch (code)
		{
		case red:
			cout << "�Լ��� �Ӿ����ϴ�.\n";
			break;
		case orange:
			cout << "�Ӹ�ī���� �ֻ��̾����ϴ�.\n";
			break;
		case yellow:
			cout << "�Ź��� ������̾����ϴ�.\n";
			break;
		case green:
			cout << "������ �ʷϻ��̾����ϴ�.\n";
			break;
		case blue:
			cout << "�����ʹ� �Ķ����̾����ϴ�.\n";
			break;
		case violet:
			cout << "���� ������̾����ϴ�.\n";
			break;
		case indigo:
			cout << "������� �ʺ��̾����ϴ�.\n";
			break;
		}
		cout << "�÷� �ڵ�(0,1,2,3,4,5,6)�� �Է��Ͻʽÿ�: ";
		cin >> code;
	}
	cout << "���α׷��� �����մϴ�.\n";
	return 0;
}