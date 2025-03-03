
import com.dht.junittestdemo.Radix;
import org.junit.Test;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author admin
 */
public class RadixTester {
    @Test
    public void testException1() {
        Assertions.assertThrows(ArithmeticException.class, () -> {
            new Radix(-1);
        });
    }
    
    @Test
    public void testException2() {
        Assertions.assertThrows(ArithmeticException.class, () -> {
            Radix r = new Radix(100);
            r.ConvertDecimalToAnother(1);
        });
    }
    
    @ParameterizedTest
    @CsvFileSource(resources = "test.csv", numLinesToSkip = 1)
    public void testData(int number, int radix, String expected) {
        Radix r = new Radix(number);
        String actual = r.ConvertDecimalToAnother(radix);
        
        Assertions.assertEquals(expected, actual);
    }
}
