#include<iostream>
#include<typeinfo>

using namespace std;

class Coo {
public:
  void PrintType() {
    // return typeid(*this);
    cout << typeid(*this).name() << endl;
    cout << typeid(*this).hash_code() << endl;

    cout << typeid(this).name() << endl;
    cout << typeid(this).hash_code() << endl;
  }
};

int main() {
  Coo coo;
  cout << typeid(coo).name() << endl;
  coo.PrintType();
 
  hash<string> hash_string;
  cout << "size_of(size_t):" << sizeof(size_t) << endl;
  cout << "hash:" << hash_string("coo") << endl;

  // compile error: /usr/include/c++/4.9/typeinfo:178:5: error: 'std::type_info::type_info(const std::type_info&)' is private
  // type_info coo_type2 = typeid(coo);
  // cout << coo_type2.name << endl;
}

//  g++ -std=c++14 test_reflection.cc
