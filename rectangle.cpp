/* Created By Clayton Branstetter
This Program takes the users input and calculates the perimeter and the area
*/
#include <iostream> // header file

using namespace std; // preprocessor directive

int main() {
    // declaring values needed
    int length, width, perimeter, area;

    // prompting user for length
    cout << "pls gib length\n";
    cin >> length;
    // prompting user for width
    cout << "pls gib width\n";
    cin >> width;

    // first find perimeter with the given values
    // perimeter = 2(l+w)
    perimeter = 2 * length + 2 * width;
    // second find area with the given values
    // area = l*w
    area = length * width;

    // now, output the values
    // gives blank space between given width and stats
    cout << "\n";
    // outputs stats ... \n creates a new line 
    // so that length isnt printed on same line
    cout << "stats\n";
    // outputs the length ... endl creates new line
    cout << "length = " << length << endl;
    // outputs the width
    cout << "width = " << width << endl;
    // outputs the perimeter
    cout << "perimeter = " << perimeter << endl;
    // outputs the area ... 
    //endl; or \n isnt needed because this is final line
    cout << "area = " << area;
}