//Charles Cheung
//charles.cheung24@myhunter.cuny.edu
//May 5, 2020
//This C++ program asks the user for the month of the year (as a number), and prints the season

#include <iostream>
using namespace std;

int main()
{
	int month;
	cout << "Enter month (as a number):";
	cin >> month;
	if (month < 3 or month > 11)
	{
		cout << "Happy Winter";
	}
	else if (month >3 and month < 7)
	{
		cout << "Happy Spring";
	}
	else if (month >7 and month < 9)
	{
		cout << "Happy Summer";
	} 
	else 
	{
		cout << "Happy Fall";
	}
	return(0);
}