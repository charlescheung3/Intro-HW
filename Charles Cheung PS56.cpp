//Charles Cheung
//charles.cheung24@myhunter.cuny.edu
//May 5, 2020
//This C++ program draws triangles with stars based on a number the user inputs

#include <iostream>
using namespace std;

int main() 
{
  int i,j,size;
  cout << "Enter size: ";
  cin >> size;
  for (i = 1; i < size+1; i++)
  {
    for (j = 0; j < i; j++)
    {
        cout << "*";
    }
    cout << endl;
  }
    return 0; 
 }




