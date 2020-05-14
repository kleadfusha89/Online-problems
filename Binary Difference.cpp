#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

string findBinary(int num)
{
	int remainder = 0;
	string binaryValue = "";
	while(num > 0)
	{
		remainder = num % 2;
		num = num / 2;
		binaryValue += to_string(remainder);
	}
	return binaryValue;

}


int binaryDifference(string x, string y)
{
	int changes = 0;
	int smaller;
	int difference = x.length() - y.length();
	difference = abs(difference);

	if (x.length() > y.length())
		smaller = y.length();
	else
		smaller = x.length();
	
	for (int i = 0; i < smaller; i++)
	{
		if (x[i] != y[i])
		{
			changes++;
		}
	}
	changes += difference;
	
	return changes;


}

int main()
{
	int x = 5;
	int y = 9;
	

	string xBinary = findBinary(x);
	string yBinary = findBinary(y);
	cout << x << " : " << xBinary << endl;
	cout << y << " : " << yBinary << endl;

	cout << binaryDifference(xBinary, yBinary) << endl;


	system("PAUSE");
   
	
}
