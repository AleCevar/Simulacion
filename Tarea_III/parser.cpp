#include <bits/stdc++.h>

using namespace std;

#define all(a) a.begin(),a.end()
#define nl cout << '\n'
#define vec vector
#define ll long long
#define pr pair
#define forr(a,b,c) for(ll (a) = (b); (a) < (c); (a)++)
#define forn(a,b) forr(a,0,b)
#define ce(a) cout << (a) << ' ';
#define cnl(a) cout << (a) << '\n'
#define sz(a) (ll)a.size()
#define pb push_back

const ll mod = 998244353;

void solve() {
  ll n,m; cin >> n >> m;
  vec<vec<float>> a(n,vec<float>(m));
  forn(i,n) forn(j,m) cin >> a[i][j];
  forn(j,m){
    forn(i,n) cnl(a[i][j]);
  }
}

int32_t main(){
  ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
  // ll t; cin >> t; while(t--)
  solve();
  return 0;
}