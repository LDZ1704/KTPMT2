
import com.dht.junittestdemo.DemoService;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;
import org.junit.jupiter.params.provider.ValueSource;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author admin
 */
public class Test2 {

    @ParameterizedTest
    @ValueSource(ints = {4, 6, 144, 156})
    public void testListOfEvenNumbers(int n) {
        boolean actualOutput = DemoService.isNt(n);

        Assertions.assertFalse(actualOutput);
    }
    
    @ParameterizedTest
    @CsvFileSource(resources = "data.csv", numLinesToSkip = 1)
    public void test(int n, boolean expected) {
        Assertions.assertEquals(expected, DemoService.isNt(n));
    }
}
