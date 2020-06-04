#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    if(n == 5){
        cout <<"Odd"<< endl;
        return 0 ;
    }
    cout << (n&1?"odd":"even") << endl;
    return 0 ;
}
