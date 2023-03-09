package org.example;

public class StringUtils {
    public boolean isPalindrome(String str) {
        if (str == null || str.isEmpty()) {
            return false;
        }
        int i = 0, j = str.length() - 1;
        while (i < j) {
            if (str.charAt(i) != str.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    public String reverseString(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        StringBuilder sb = new StringBuilder(str);
        return sb.reverse().toString();
    }

    public String capitalizeFirstLetter(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        char firstChar = str.charAt(0);
        if (Character.isUpperCase(firstChar)) {
            return str;
        } else {
            StringBuilder sb = new StringBuilder(str);
            sb.setCharAt(0, Character.toUpperCase(firstChar));
            return sb.toString();
        }
    }

    public String[] splitString(String str, String separator) {
        if (str == null || str.isEmpty()) {
            return new String[0];
        }
        if (separator == null || separator.isEmpty()) {
            throw new IllegalArgumentException("Separator cannot be null or empty");
        }
        return str.split(separator);
    }
}
