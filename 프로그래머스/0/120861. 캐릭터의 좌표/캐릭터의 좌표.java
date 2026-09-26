class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {0,0};
        
        int width = board[0] / 2;
        int height = board[1] / 2;
    
        for(int i=0; i<keyinput.length; i++) {
        
            switch(keyinput[i]) {
                case "up":
                    if((answer[1] + 1) > height) {
                        break;
                    }
                    answer[1] += 1;
                    break;
                    
                case "down":
                    if((answer[1]-1) < -height) {
                        break;
                    }
                    answer[1] += -1;
                    break;
                    
                case "left":
                    if((answer[0] - 1) < -width) {
                        break;
                    }
                    answer[0] += -1;
                    break;
                    
                default:
                    if((answer[0] + 1) > width) {
                        break;
                    }
                    answer[0] += 1;
                    break;
                    
            }
        }
        
        return answer;
    }
}