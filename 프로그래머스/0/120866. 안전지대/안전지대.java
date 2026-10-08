

class Solution {
    public int solution(int[][] board) {       
        int n = board[0].length;
        int[][] result = new int[n][n]; 
        
        for(int y = 0; y < n; y++) { 
            for(int x = 0; x < n; x++) {
                if (board[y][x] == 1) {
                    
                    // 위험 구역
                    for (int dy=-1; dy<=1; dy++) {
                        for (int dx=-1; dx<=1; dx++) {
                            int nx = x + dx;
                            int ny = y + dy;
                            
                            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                                result[ny][nx] = 1;
                            }
                        }
                    }
                }
            }
        }
        int answer = 0;
        
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if (result[i][j] == 0) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}