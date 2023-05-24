#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main(void)
{
    string str1 = "hello", str2 = "ll", needle = "";

    // if (str1.find(str2)) cout << "True" << endl;
    cout << str1.find(str2) << endl;
    cout << needle.length() << endl;

    for(int i=0;i<=6;i++)
    {
        cout << i << endl;
        i += 1;
    }

    return 0;
}