// static.cpp -- ���� ���� ���� ����ϱ�
#include <iostream>
#include <string>
// ���
const int ArSize = 10;

// �Լ� ����
void strcount(std::string str);

int main()
{
	using namespace std;
	std::string input;

	cout << "�������� �� ���� �Է��Ͻʽÿ�:\n";
	getline(std::cin, input);
	while (input != "")
	{
		strcount(input);
		cout << "���� ���� �Է��Ͻʽÿ�(�������� �� ���� �Է�):\n";
		getline(std::cin, input);
	}
	cout << "���α׷��� �����մϴ�.\n";
	return 0;
}

void strcount(std::string str)
{
	using namespace std;
	static int total = 0;		// ���� ���� ����
	int count = 0;				// �ڵ� ���� ����

	cout << "\"" << str << "\"���� ";
	count = str.length();
	total += count;
	cout << count << "���� ���ڰ� �ֽ��ϴ�.\n";
	cout << "���ݱ��� �� " << total << "���� ���ڸ� �Է��ϼ̽��ϴ�.\n";
}