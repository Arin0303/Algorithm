import java.util.Arrays;

class Solution {
    public int[] solution(int[] answers) {
        
        int[] p1 = {1,2,3,4,5};
        int[] p2 = {2,1,2,3,2,4,2,5};
        int[] p3 = {3,3,1,1,2,2,4,4,5,5};
        
        int[] scores = new int[3];
        
        // 각 점수 계산
        for (int i=0; i<answers.length; i++) {
            if (answers[i] == p1[i%5])  scores[0]++;
            if (answers[i] == p2[i%8])  scores[1]++;
            if (answers[i] == p3[i%10])  scores[2]++;
        }
        
        // 최고 점수 계산
        int max_num = Math.max(scores[0], Math.max(scores[1], scores[2]));

        
        int[] answer = new int[3];
        
        int count = 0;
        
        // 최고 점수를 받은 수포자 
        for (int i=0; i<3; i++) {
            if (max_num == scores[i]) {
                answer[count++] = i+1;
            }
        }
        
        return Arrays.copyOf(answer, count);
        
    }
}