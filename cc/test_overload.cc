#include <iostream>

using namespace std;

void foo(int i) {
  cout << "foo-int:" << i << endl;
}

void foo(const string& i) {
  cout << "foo-string:" << i << endl;
}

int main() {
  foo(1);
  foo("string");
}
