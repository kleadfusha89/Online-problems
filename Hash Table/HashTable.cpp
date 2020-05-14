#include "pch.h"
#include <iostream>
#include <list>
#include <cstring>
#include <string>
#include "HashTable.h"


using namespace std;

bool HashTable::isEmpty() const
{
	int sum{};
	for (int i{}; i < hashGroups; i++)
	{
		sum += table[i].size();
	}

	if (!sum)
	{
		return true;
	}

	return false;
}

int HashTable::hashFunction(int key)
{
	return key % hashGroups;
}

void HashTable::insertItem(int key, string value)
{
	int hashValue = hashFunction(key);
	auto& cell = table[hashValue];
	auto bItr = begin(cell);
	bool keyExists = false;
	for (; bItr != end(cell); bItr++)
	{
		if (bItr->first == key)
		{
			keyExists = true;
			bItr->second = value;
			cout << "[WARNING] Key exists. Vaule replaced." << endl;
			break;
		}
	}

	if (!keyExists)
	{
		cell.emplace_back(key, value);
	}
	return;

}


void HashTable::removeItem(int key)
{
	int hashValue = hashFunction(key);
	auto& cell = table[hashValue];
	auto bItr = begin(cell);
	bool keyExists = false;
	for (; bItr != end(cell); bItr++)
	{
		if (bItr->first == key)
		{
			keyExists = true;
			bItr = cell.erase(bItr);
			cout << "[Info] Pair removed." << endl;
			break;
		}
	}

	if (!keyExists)
	{
		cout << "[WARNING] Key not found! Pair not removed." << endl;
	}

	return;
}

void HashTable::printTable()
{
	for (int i{}; i < hashGroups; i++)
	{
		if (table[i].size() == 0) continue;

		auto bItr = table[i].begin();

		for (; bItr != table[i].end(); bItr++)
			cout << "Key: " << bItr->first << "  Value: " << bItr->second << endl;
	}
}