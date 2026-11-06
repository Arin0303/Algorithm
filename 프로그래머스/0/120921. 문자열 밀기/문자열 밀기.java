class Solution {
    public int solution(String A, String B) {
        int answer = -1;
        for (int i=0; i<A.length(); i++) {
            if (A.equals(B)) {
                answer = i;
                break;
            }
            
            
            // 마지막 문자
            String last = A.substring(A.length() - 1);
            
            // 나머지 문자열
            String rest = A.substring(0, A.length() - 1);
            
            A = last + rest;
                        
        }
        return answer;
    }
}