import org.example.StringUtils;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class StringUtilsTest {
    private StringUtils stringUtils;

    @Before
    public void setUp() {
        stringUtils = new StringUtils();
    }

    @After
    public void tearDown() {
        stringUtils = null;
    }

    @Test
    public void testIsPalindromeForPalindrome() {
        assertTrue(stringUtils.isPalindrome("madam"));
    }

    @Test
    public void testIsPalindromeForNonPalindrome() {
        assertFalse(stringUtils.isPalindrome("hello"));
    }

    @Test
    public void testIsPalindromeForEmptyString() {
        assertFalse(stringUtils.isPalindrome(""));
    }

    @Test
    public void testIsPalindromeForNull() {
        assertFalse(stringUtils.isPalindrome(null));
    }

    @Test
    public void testReverseString() {
        assertEquals("olleh", stringUtils.reverseString("hello"));
    }

    @Test
    public void testReverseStringForEmptyString() {
        assertEquals("", stringUtils.reverseString(""));
    }

    @Test
    public void testReverseStringForNull() {
        assertNull(stringUtils.reverseString(null));
    }

    @Test
    public void testCapitalizeFirstLetter() {
        assertEquals("Hello", stringUtils.capitalizeFirstLetter("hello"));
    }

    @Test
    public void testCapitalizeFirstLetterForAlreadyCapitalized() {
        assertEquals("Hello", stringUtils.capitalizeFirstLetter("Hello"));
    }

    @Test
    public void testCapitalizeFirstLetterForEmptyString() {
        assertEquals("", stringUtils.capitalizeFirstLetter(""));
    }

    @Test
    public void testCapitalizeFirstLetterForNull() {
        assertNull(stringUtils.capitalizeFirstLetter(null));
    }

    @Test
    public void testSplitString() {
        String[] expected = {"hello", "world"};
        assertArrayEquals(expected, stringUtils.splitString("hello,world", ","));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testSplitStringWithNullSeparator() {
        stringUtils.splitString("hello,world", null);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testSplitStringWithEmptySeparator() {
        stringUtils.splitString("hello,world", "");
    }
}
