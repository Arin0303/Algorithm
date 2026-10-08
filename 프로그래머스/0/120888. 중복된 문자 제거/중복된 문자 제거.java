class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        for(int i=0; i < my_string.length(); i++) {
            boolean is_present = false;
            // 존재 여부 확인 로직
            for(int j=0; j<answer.length(); j++) {
                
                // 이미 존재
                if (answer.charAt(j) == my_string.charAt(i)) {
                    is_present = true;
                    break;
                }
            }
            if (is_present == false) {
                answer += my_string.charAt(i);
            }
            
        }
        return answer;
    }
}