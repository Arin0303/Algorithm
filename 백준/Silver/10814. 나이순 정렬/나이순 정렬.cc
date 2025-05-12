#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Member {
    int age;
    string name;
    int order;
};

bool compare(Member a, Member b) {
    if (a.age == b.age) return a.order < b.order;
    return a.age < b.age;
}

int main() {
    int n;
    cin >> n;
    vector<Member> members(n);
    for (int i = 0; i < n; i++) {
        cin >> members[i].age >> members[i].name;
        members[i].order = i;
    }
    sort(members.begin(), members.end(), compare);
    for (auto &m : members) {
        cout << m.age << ' ' << m.name << '\n';
    }
    return 0;
}
