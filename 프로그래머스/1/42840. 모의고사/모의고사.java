import java.util.Arrays;

class Solution {
    public int[] solution(int[] answers) {
        int[][] submit_ans = {
            {1,2,3,4,5},
            {2,1,2,3,2,4,2,5},
            {3,3,1,1,2,2,4,4,5,5}
        }; 
        int[] score = {0,0,0};
    
        for (int i=0; i<answers.length; i++) {
            for (int j=0; j<3; j++) {
                if (answers[i] == submit_ans[j][i%(submit_ans[j].length)])   score[j] += 1;
            }
        }
        // 최고 점수 계산
        int max_score = Math.max(score[0], Math.max(score[1], score[2]));
        // 최고 점수 인원 수와 해당 수포자 계산
        int[] answer = new int[3];
        int count = 0;
            
        for (int i=0; i<3; i++) {
            if (max_score == score[i]) {
                answer[count++] = i+1;
            }
        }  
        return Arrays.copyOf(answer, count);
    }
}