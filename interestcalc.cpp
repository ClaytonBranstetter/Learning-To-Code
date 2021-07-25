/* Created by Clayton Branstetter
Interest Calc
*/

#include <iostream> // header file
#include <cmath> // header file for pow
using namespace std; // preprocessor directive

int main() { // main function
// variable declaration
double A; // result available
double X; // initial deposit
double R; //interest rate
double N; // number of years to calculate

// user variable input
cout << "Enter the Initial Deposit" << endl;
cin >> X; 
cout << "Enter the number of years" << endl;
cin >> N;
cout << "Enter the interest rate" << endl;
cin >> R;

// calculations
  // for reference pow(3.0, 4.0) - 3 to the 4th power
A=X*(pow(1.0+(R/100),N));

//displays final calculations for user
cout << "The amount available if" << X
<< " is deposited for " << N
<< " years at " << R
<< " interest rate is " << A << endl;
}