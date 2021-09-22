/* Created by Clayton Branstetter
This program is to calculate change back to the customer
Cash Register
*/

#include <iostream> // header file

using namespace std; // preprocessor directive

int main() { // main function
// variable declaration
float checkAmount, amountPaid, change;
int dollar, quarter, dime, nickel, penny;
int p_change;

// prompt user for checkAmount
cout << "pls gib checkAmount" << endl;
// take in checkAmount
cin >> checkAmount;
// prompt user for amount amountPaid
cout << "pls gib amountPaid" << endl;
// take in the amountPaid
cin >> amountPaid;
// convert into positive change
change = (checkAmount - amountPaid) * -1;
p_change = change * 100;
// calculations
dollar = p_change / 100;
p_change -= (dollar * 100);

quarter = p_change / 25;
p_change -= (quarter * 25);

dime = p_change / 10;
p_change -= (dime * 10);

nickel = p_change / 5;
p_change -= (nickel * 5);

penny = p_change;
// display output
cout << "The change is $" << change << endl;
cout << dollar << "dollar bills" << endl;
cout << quarter << "quarter(s)" << endl;
cout << dime << "dime(s)" << endl;
cout << nickel << "nickel(s)" << endl;
cout << penny << "penny(s)" << endl;
}
