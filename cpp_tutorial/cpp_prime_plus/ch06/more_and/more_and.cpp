// more_and.cpp -- ���� ������
#include <iostream>
const char* qualify[4] =
{
	"������ �޸���",
	"�𷡻��� ����",
	"��ġ �߸�",
	"�θ޶� ������"
};
int main()
{
	using namespace std;
	int age;
	cout << "���̸� �Է��Ͻʽÿ�: ";
	cin >> age;
	int index;

	if (age > 17 && age < 35)
		index = 0;
	else if (age >= 35 && age < 50)
		index = 1;
	else if (age >= 50 && age < 65)
		index = 2;
	else
		index = 3;

	cout << "����� " << qualify[index] << "�� ������ �� �ֽ��ϴ�.\n";
	return 0;
}