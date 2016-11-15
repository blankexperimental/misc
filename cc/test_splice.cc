#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

using std::list;
using std::cout;
using std::endl;

template <typename T>
class print{
public:
    void
    operator()(const T& iter) const
    {
        cout<<iter;
        return ;
    }
};

int
listTest(void)
{
    list<int> list1;
    list<int> list2;
    list1.push_back(1);
    list1.push_back(2);
    list1.push_back(3);
    list2.push_back(4);
    list2.push_back(8);
    list2.push_back(9);
    list2.push_back(6);
    list1.splice(list1.end(),
                list2,
                ++list2.begin(), list2.end());       //list1 = list1 + [list2++, list2.end), list2 = list2.begin();
    //list1.sort();
    std::for_each(list1.begin(), list1.end(), print<int>());
    std::cout<<endl;
    std::for_each(list2.begin(), list2.end(), print<int>());
    std::cout<<endl;

    auto start = list1.begin();
    auto end = list1.begin();
    cout << *start << " "<< *end << endl;

    std::advance(start, 2);
    std::advance(end, 3);
    
    cout << *start << " "<< *end << endl;
    list1.splice(list1.begin(), list1, start, end);
    std::for_each(list1.begin(), list1.end(), print<int>());
    cout << endl;  
    return 0;
}

int
main()
{
    listTest();
    return 0;
}
