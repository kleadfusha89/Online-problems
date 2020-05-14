#pragma once


class HashTable
{
private:
	static const int hashGroups = 10;
	list<pair<int, string>> table[hashGroups]; // List 1 -> index 0 ; list 2 -> index 1 .... etc etc...
public:
	bool isEmpty() const;
	int hashFunction(int key);
	void insertItem(int key, string value);
	void removeItem(int key);
	//string searchTable(int key);
	void printTable();

};