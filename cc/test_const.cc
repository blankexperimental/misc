/*
test const
*/

#include <iostream>

using namespace std;

class A {
private:
  int i_;

public:
  A() {
    this->i_ = 1;
  }

  int get() const {
    return this->i_;
  }

  void set(int i) {
    this->i_ = i;
  }
};

int main() {
  cout << "--------------------------" << endl;
  A *const p1 = new A;  // must new object at this time
  p1->set(2);
  cout << p1->get() << endl;
  // error, because p1 is const
  // p1++
  delete p1;

  cout << "--------------------------" << endl;
  const A* p2;
  p2 = new A;
  // test_const.cc:36:12: error: passing 'const A' as 'this' argument of 'void A::set(int)' discards qualifiers [-fpermissive]
  // p2->set(2);
  cout << p2 << endl;
  cout << p2->get() << endl;
  p2++;
  cout << p2 << endl;
  p2--;
  delete p2;

  cout << "--------------------------" << endl;
  const A *const p3 = new A;
  cout << p3->get() << endl;
  delete p3;

  return 0;
}
