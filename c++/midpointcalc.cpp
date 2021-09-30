/* Created by Clayton Branstetter
When given the x and y coordinates of two points on a line, 
the program calculates and displays the slope and the midpoint
of that line
**MIDPOINT CALC**
*/

#include <iostream>

using namespace std;

int main() {
    // variable declaration
    float x1, y1, x2, y2, slope, midpointX, midpointY;
    // user variable input of coordinates
    cout << "Please enter the x coordinate of the first point on a line: ";
    cin >> x1;
    cout << "Please enter the y coordinate of the first point on a line: ";
    cin >> y1;
    cout << "Please enter the x coordinate of the second point on the line: ";
    cin >> x2;
    cout << "Please enter the y coordinate of the second point on the line: ";
    cin >> y2;
    // user input feedback
    cout << "The first point's coordinate is: (" << x1 << "," << y1 << ")" << endl;
    cout << "The second point's coordinate is:(" << x2 << "," << y2 << ")" << endl;
    // slope and midpoint calculation
    slope = (y2 - y1) / (x2 - x1);
    midpointX = (x1 + x2) / 2;
    midpointY = (y1 + y2) / 2;
    // program slope and midpoint output
    cout << "The slope of the line is:" << slope << endl;
    cout << "The midpoint is: (" << midpointX << "," << midpointY << ")" << endl;
}