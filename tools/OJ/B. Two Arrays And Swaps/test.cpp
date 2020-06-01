#include<bits/stdc++.h>
using namespace std;

void solve() {

        long long int n, k ;
            cin >> n >> k;
                vector < long long int > a(n) , b(n) ;
                    for(auto &x : a){
                                cin >> x;
                                    }
                        for(auto &x : b){
                                    cin >> x;
                                        }

                            sort(a.begin(),a.end() );
                                sort( b.begin(),b.end(), greater<long long int> ()) ;

                                    for(int i = 0 ; i < k ; i++){
                                                if(a[i] < b[i]){
                                                                swap(a[i],b[i]) ;
                                                                        }
                                                    }
                                        long long int ans = 0 ;
                                            for(auto x : a){
                                                        ans += x;
                                                            }
                                                cout << ans << endl ;
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
