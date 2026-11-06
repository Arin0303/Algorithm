import java.util.Set;
import java.util.LinkedHashSet;

class Solution {
    public String solution(String my_string) {
        Set<Character> set = new LinkedHashSet<>();
        
        for (int i=0; i<my_string.length(); i++){
            set.add(my_string.charAt(i));
        }

        String answer = "";
        
        for(char item : set) { // 향상된 for문
            answer += item;
        }
        return answer;
    }
}