#include "string2.h"

using namespace std;

int main()
{
	String s1(" and I am a C++ student.");
	String s2 = "���� �̸��� �Է��Ͻʽÿ�: ";
	String s3;
	cout << s2;					// �����ε��� << ������
	cin >> s3;					// �����ε��� >> ������
	s2 = "My name is " + s3;	// �����ε��� =, + ������
	cout << s2 << ".\n";
	s2 = s2 + s1;
	s2.stringup();				// ���ڿ��� �빮�ڷ� ��ȯ�Ѵ�
	cout << "���� ���ڿ�����\n" << s2 << "\n���� 'A'�� "
		<< s2.has('A') << "�� ��� �ֽ��ϴ�.\n";
	s1 = "red";					// String(const char*)��
								// String& operator(const String&)�� ����Ѵ�
	String rgb[3] = { String(s1), String("green"), String("blue") };

	cout << "���� ������� �̸��� �ϳ��� �Է��Ͻʽÿ�: ";
	String ans;
	bool success = false;
	while (cin >> ans)
	{
		ans.stringlow();		// ���ڿ��� �ҹ��ڷ� ��ȯ�Ѵ�
		for (int i = 0; i < 3; i++)
		{
			if (ans == rgb[i])
			{
				cout << "�¾ҽ��ϴ�!\n";
				success = true;
				break;
			}
		}
		if (success)
		{
			break;
		}
		else
		{
			cout << "�ٽ� �Է��Ͻʽÿ�: ";
		}
	}
	cout << "���α׷��� �����մϴ�.\n";

	return 0;
}