//Charles Cheung
//charles.cheung24@myhunter.cuny.edu
//May 5, 2020
//This C++ program asks the user for their age, and continue asking until the number entered positive (that is, greater than 0).

#include <iostream>
using namespace std;

int main()
{
	int age;
	cout << "Please enter age:";
	cin >> age;
    while (age < 0)
    {
    	cout<<"Entered a negative number.";
    	cout << "Please enter age:";
		cin >> age;
    }
    cout << "You entered your age as: " << age;
    return(0);
}