#include<vector>
#include<iostream>

using namespace std;

vector<int> get() {
  vector<int> vec;
  vec.push_back(1);
  cout << vec.size() << endl;
  return vec;
}

int main() {
  cout << get().size() << endl;
}
