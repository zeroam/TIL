#include <iostream>

using namespace std;

int main()
{
    string phrase = "Nice to meet you";
    cout << "Giraffe Academy\n";
    cout << "Hello" << endl;
    cout << phrase.length() << endl;
    cout << phrase[0] << endl;
    phrase[0] = 'B';
    cout << phrase << endl;
    cout << phrase.find("meet", 0) << endl;
    cout << phrase.substr(8, 3) << endl;

    return 0;
}
