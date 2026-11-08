import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char chars = s.charAt(i);
            if (chars == '(') {
                stack.push(')');
            } else if (chars == '{') {
                stack.push('}');
            } else if (chars == '[') {
                stack.push(']');
            } else if (stack.isEmpty() || stack.pop() != chars) {
                return false;
            }
        }
        return stack.isEmpty();
    }
}