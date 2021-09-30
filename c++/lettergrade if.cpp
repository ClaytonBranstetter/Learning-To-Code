/* Created by Clayton Branstetter
This program takes user input and prints the letter grade
90-100 = A
80-89 = B
70-79 = C
60-69 = D
59 = F
*/

#include <iostream>
using namespace std;

int main() { 
  int x = 0;

  cout << "pls gib grade" << endl;
  cin >> x;

  if(x >= 100) {
      cout << "A";
  }
  else if (x >= 89) {
    cout << "B";
  }
  else if(x >= 79) {
    cout << "C";
  }
  else if(x >= 69){
    cout << "D";}
  else{
    cout << "F";
  }

  
}