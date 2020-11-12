import java.util.Calendar;
class Solution {
    public String solution(int a, int b) {
        Calendar today = Calendar.getInstance();
        today.set(2016,a-1,b);
        String []WEEK  = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
        String answer = WEEK[(int)(today.get(Calendar.DAY_OF_WEEK))-1];
        return answer;
    }
}
