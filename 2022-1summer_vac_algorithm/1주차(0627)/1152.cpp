// Example program
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s;
    int count = 0;
    
    getline(cin,s);
    
    // 입력된 문자열의 길이만큼 반복
    // 현재 위치의 값이 공백이 아닌 상태(문자를 가지고 있음) 이며 다음 위치에서의 값이 공백이거나 null(끝)인 경우 count를 추가
    for(int i=0; i<s.length(); i++){
        if(s[i] != ' ' && (s[i+1] == ' ' || s[i+1] == '\0')){
            count++;
        }
    }
    cout << count;
    return 0;
}
