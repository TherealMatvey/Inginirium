#include <iostream>
using namespace std;


//float root()
//{
//	cout << "print a number" << endl;
//	int b;
//	cin >> b;
//	float a = 0;
//	for (float i = 100000000; a * a < b; i /= 10)
//	{
//		while (a * a <= b)
//		{
//			a = a + i;
//		};
//		a -= i;
//	}
//	return a;
//}


void main()
{
	/*cout << root() << endl;*/
	cout << "print a number" << endl;
	int b;
	cin >> b;
	float a = 0;
	for (float i = 1000; a * a < b; i /= 10)
	{
		while (a * a <= b)
		{
			a = a + i;
			cout << a << endl;
		};
		a -= i;
		/*if ((a - i) * (a - i) >= b)
		{
			a -= i;
		}
		cout << a << endl;*/
	}

}

