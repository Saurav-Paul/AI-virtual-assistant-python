                /*Saurav Paul*/
#include<bits/stdc++.h>
using namespace std;

void solve() {

        string s;
            cin >> s;

                int a , b, c ;
                    a = b = c = -1 ;
                        int mn = INT_MAX ;
                            bool ok = false ;
                                for(int i = 0 ; i < s.size() ; i++){
                                            if(s[i] == '1') a = i ;
                                                    else if(s[i] == '2') b = i ;
                                                            else if(s[i] == '3') c = i ;
                                                                    else assert(false) ;

                                                                            if(a != -1 && b != -1 && c != -1){
                                                                                            mn = min( mn , max({a,b,c}) - min({a,b,c})+1)  ;
                                                                                                        ok = true ;            
                                                                                                                }
                                                                                }
                                    if(!ok) mn = 0 ;
                                        cout << mn << endl ;
}

int main(){

        ios_base::sync_with_stdio(false);
            cin.tie(0);

                int testcase;
                    cin >> testcase;
                        for (int t = 1; t <= testcase; t++){
                                    solve();
                                        }    

                            return 0;
}
