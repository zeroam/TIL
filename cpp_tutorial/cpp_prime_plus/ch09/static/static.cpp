// static.cpp -- ���� ���� ���� ����ϱ�
#include <iostream>
// ���
const int ArSize = 10;

// �Լ� ����
void strcount(const char* str);

int main()
{
	using namespace std;
	char input[ArSize];
	char next;

	cout << "�������� �� ���� �Է��Ͻʽÿ�:\n";
	cin.get(input, ArSize);
	while (cin)
	{
		cin.get(next);
		while (next != '\n')	// �Է� ���ڿ��� �迭�� ũ�⸦ �ʰ��Ѵ�
			cin.get(next);		// �������� �����Ѵ�
		strcount(input);
		cout << "���� ���� �Է��Ͻʽÿ�(�������� �� ���� �Է�):\n";
		cin.get(input, ArSize);
	}
	cout << "���α׷��� �����մϴ�.\n";
	return 0;
}

void strcount(const char* str)
{
	using namespace std;
	static int total = 0;		// ���� ���� ����
	int count = 0;				// �ڵ� ���� ����

	cout << "\"" << str << "\"���� ";
	while (*str++)
		count++;
	total += count;
	cout << count << "���� ���ڰ� �ֽ��ϴ�.\n";
	cout << "���ݱ��� �� " << total << "���� ���ڸ� �Է��ϼ̽��ϴ�.\n";
}