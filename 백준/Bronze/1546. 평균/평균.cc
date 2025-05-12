#include <iostream>
#include <vector>
#include <iomanip>// setprecision 사용을 위해 필요
#include <algorithm>
using namespace std;


int main(void) {
    int n;
    cin >> n;

    vector<double> score(n);

    double sum = 0;
    double average;
    double max_score;


    for (int i = 0; i < score.size(); i++) {
        cin >> score[i];
    }

    // 최댓값 구하기

    max_score = *max_element(score.begin(), score.end());

    
    // 점수 재계산
    for (int i = 0; i < score.size(); i++) {
        score[i] = (score[i] / max_score) * 100; 
        sum += score[i];
    }



    average = sum / n;
    cout << fixed << setprecision(15) <<average << '\n';

    return 0;
}
