// num_test.cpp -- for ������ ���� �˻翡 ��ġ�� ���� ����Ѵ�
#include <iostream>

int main()
{
	using namespace std;

	cout << "ī��Ʈ ���۰��� �Է��Ͻʽÿ�: ";
	int limit;
	cin >> limit;
	int i;
	for (i = limit; i; i--)			// i�� 0�� �Ǹ� ����
		cout << "i = " << i << "\n";
	cout << "i = " << i << "�̹Ƿ� ������ �����մϴ�.\n";
	
	return 0;
}