				/*Saurav Paul*/
#include<bits/stdc++.h>
using namespace std;


#define bug()				  debug() <<
#define sim template < class c
#define ris return * this
#define dor > debug & operator <<
#define eni(x) sim > typename \
enable_if<sizeof dud<c>(0) x 1, debug&>::type operator<<(c i) {
sim > struct rge { c b, e; };
sim > rge<c> range(c i, c j) { return rge<c>{i, j}; }
sim > auto dud(c* x) -> decltype(cerr << *x, 0);
sim > char dud(...);
struct debug {
#ifdef PAUL
~debug() { cerr << endl; }
eni(!=) cerr << boolalpha << i; ris; }
eni(==) ris << range(begin(i), end(i)); }
sim, class b dor(pair < b, c > d) {
  ris << "(" << d.first << ", " << d.second << ")";
}
sim dor(rge<c> d) {
  *this << "[";
  for (auto it = d.b; it != d.e; ++it)
    *this << ", " + 2 * (it == d.b) << *it;
  ris << "]";
}
#else
sim dor(const c&) { ris; }
#endif
};
#define dbg(...) " [" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "] "

#ifdef ONLINE_JUDGE
#define cerr if (false) cerr
#endif

long long int cal(long long int n){
    long long int mx = 0 , mn = 9 ;
    if(n == 0) return 0 ;
    while(n){
        mx = max(mx,n%10) ;
        mn = min(mn,n%10) ;
        n /= 10 ;
    }
    return mx*mn ;
}
bool is_zero(long long int n){
    
    while(n){
        if(n%10 == 0){
            return true ;
        }
        n /= 10 ;
    }

    return false ;
}


int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int testcase;
    cin >> testcase;
    for (int t = 1; t <= testcase; t++){
    long long int n , k ;
    cin >> n >> k;
    long long int last = 0 ;
    long long int st = n ;
    for(int i = 0 ; i < k-1 ; i++){
        st = st + cal(st) ;
        if(is_zero(st)){
            
            break ;
        }
    }
    cout << st << endl ;
    }

    return 0;
}