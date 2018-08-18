public class Solution {
    public boolean match(char[] str, char[] pattern)
    {
        if(str == null || pattern == null){
            return false;
        }
        int strIndex = 0;
        int patternIndex = 0;
        return matchCore(str, strIndex, pattern, patternIndex);
    }
    
    public boolean matchCore(char[] str, int strIndex, char[] pattern, int patternIndex){
        // str到尾，pattern到尾，匹配成功
        if(strIndex == str.length && patternIndex == pattern.length){
            return true;
        }
        // pattern到尾，str还没结束，匹配失败
        if(patternIndex == pattern.length && strIndex != str.length){
            return false;
        }
        // 如果第二个是"*"，在考虑第一位是否匹配，匹配：0个，1个或多个；不匹配：pattern移两位
        if(patternIndex + 1 < pattern.length && pattern[patternIndex + 1] == '*'){
            if((strIndex != str.length && str[strIndex] == pattern[patternIndex]) || (pattern[patternIndex] == '.' && strIndex != str.length)){
                return matchCore(str, strIndex, pattern, patternIndex + 2) || // 匹配0个字符
                matchCore(str, strIndex + 1, pattern, patternIndex + 2) || // 匹配1个字符
                matchCore(str, strIndex + 1, pattern, patternIndex); // 匹配多个字符
            }
            else{
                return matchCore(str, strIndex, pattern, patternIndex + 2); // 匹配0个字符
            }
        }
        // 第二个不是"*", 且第一位匹配，则str和pattern均移一位。
        if((strIndex != str.length && str[strIndex] == pattern[patternIndex]) || (pattern[patternIndex] == '.' && strIndex != str.length)){
            return matchCore(str, strIndex + 1, pattern, patternIndex + 1);
        }
        // 什么都没匹配，返回false
        return false;
    }
}