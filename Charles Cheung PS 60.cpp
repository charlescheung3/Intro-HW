//Charles Cheung
//charles.cheung24@myhunter.cuny.edu
//May 5, 2020
//This C++ program asks the user for a whole number between -31 and 31 and prints out the number in "two's complement" notation, using an algorithm

#include <iostream>
using namespace std;

int main()
{
	int n;
	cout << "Enter a number:";
	cin >> n;
	while (n < -31 or n > 31)
	{
		cout << "Enter a number:";
		cin >> n;
	}
	float x;
	if (n < 0)
	{
		cout<< 1;
		x = 32 + n;
	}
	else if (n >= 0)
	{
		cout<< 0;
		x = n;
	}
	float b = 16;
	while (b > 0.5)
	{
		if (x >= b)
		{
			cout<< 1;
		}
		else
		{
			cout<< 0; 
		}
		x = (float)((int)x % (int)b);
		b = b/2;
	}
	cout<< endl;
	return 0;
}