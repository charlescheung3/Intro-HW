//Charles Cheung
//charles.cheung24@myhunter.cuny.edu
//May 5, 2020
//This C++ program asks the user for the starting amount, and prints out the yearly balance of a savings account, assuming 10% interest, until the amount has doubled.

#include <iostream>
using namespace std;

int main()
{
	float startMoney;
	cout << "Please enter the starting amount:";
	cin >> startMoney;
	int y = 1;
	float nowMoney = startMoney;
	while (nowMoney < 2 * startMoney)
	{ 
		nowMoney = nowMoney * 1.1;
		cout<< "Year " << y <<" "<< nowMoney << endl;
		y++;
	}
	return 0;
}