#include <iostream>
#include <random>
using namespace std;

template <class T, class U>
T* find(T* a, U* b)
{
	return (a > b ? a : b);
};

int main()
{
	int a = 123, b = 456;
	cout << *find(&a, &b);
};