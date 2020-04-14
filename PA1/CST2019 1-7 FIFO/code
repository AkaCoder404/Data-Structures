#include <iostream>
using namespace std;

int memory = 0;
int access = 0;
int N = 0; //Buffer Size
int M = 0; //Fetched

void parse(string* buffer, char temp)
{
    if(memory == N) memory = 0; 
    //cout << temp << " : ";
    if ((*buffer).size() == N && (*buffer).find(temp) == string::npos)
    {
        (*buffer)[memory] = temp;
        memory++;  
        access++;
    } 
    else if ((*buffer).find(temp) == string::npos)
    {
        (*buffer).insert((*buffer).size(), 1, temp);
        access++;
    }
    cout << memory << " : ";
    cout << *buffer << endl;
    // cout << endl;
}

int main()
{
    cin >> N >> M;
    string buffer[1000];
    
    for(int i = 0; i < M; i++)
    {
        char temp;
        cin >> temp;
        parse(buffer, temp);
    }  
    cout << access;
}
