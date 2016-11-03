#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

template <typename T>
class MyClass {
private:
  T i;

public:
  static int j;
  MyClass(T t) {
    i = t;
  }
  void print(const string& tag) {
    cout << "---" << tag << "---" << endl;
    cout << "[int i]" << &i << " " << i << endl;
    cout << "[static int j]" << &j << " " << j << endl;
  }
  void setj(int t) {
    j = t;
  }
};

template<typename T> int MyClass<T>::j = 0;

class MyClass1 {
private:
  int i;
public:
  static int j;
  void print(const string& tag) {
    cout << "---" << tag << "---" << endl;
    cout << "[T i]"<< &i << " " << i << endl;
    cout << "[static int j]" << &j << " " << j << endl;
  }
  void setj(int t) {
    j = t;
  }

};

int MyClass1::j = 0;

/*
 * since c++17
class MyClass2 {
private:
  inline static int j = 1;
};
*/


int main() {
  MyClass<int> mc1(1);
  MyClass<string> mc2("2");
  MyClass<int> mc3(3);
  mc1.setj(1);
  mc2.setj(2);
  mc3.setj(3);
  mc1.print("mc1");
  mc2.print("mc2");
  mc3.print("mc3");

  MyClass1 mc11;
  MyClass1 mc22;
  mc11.setj(11);
  mc22.setj(22);
  mc11.print("mc11");
  mc22.print("mc22");

  cout << &MyClass<int>::j << endl;
  cout << &MyClass<string>::j << endl;
  cout << &MyClass1::j<< endl;

  cout << &decltype(mc1)::j << endl;
}

// g++ --std=c++11 test_template.cc
