#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<string>

using namespace std;

int foo(int i) {
  return i;
}

double foo(double d) {
  return d;
}

template<typename T>
auto getnu(T t)->decltype(foo(t)) {
  return foo(t);
}

int main() {
  int input[] = {1,2,5,8,10,4,3,6,9,7};
  cout << sizeof(input)/sizeof(int) << endl;
  
  for(auto x: input) {
    cout << x << " ";
  }
  cout << endl;
  
  cout << "------------------" << endl;
  int next = 1;
  priority_queue<int, vector<int>, greater<int> > pq;
  for(auto x: input) {
    if(x == next) {
      cout << next << " ";
      next++;
      if(pq.size() == 0) {
        cout << endl;
        continue;
      }
      while(next == pq.top()) {
        cout << next << " ";
        next++;
        pq.pop();
      }
      cout << endl;
    } else {
      pq.push(x);
    }
  }

  cout << "------------------" << endl;
  map<int, string> mp;
  mp.clear();
  mp.insert(make_pair(3, "a3"));
  mp.insert(make_pair(2, "a2"));
  // for in map return pair object, not iterator
  for(auto &i: mp) {
    cout << i.first << " " << i.second << endl;
  }
  
  cout << "------------------" << endl;
  // cout << decltype(mp) << endl;
  decltype(mp) mp1;
  mp1.insert(make_pair(1, "a1"));
  for(auto &i: mp1) {
    cout << i.first << " " << i.second << endl;
  }
  decltype((mp1)) mp2 = mp1;
  
  for(auto &i: mp2) {
    cout << i.first << " " << i.second << endl;
  }
  cout << "------------------" << endl;
  
}
