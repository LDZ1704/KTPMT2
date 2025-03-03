
import com.dht.junittestdemo.DemoService;
import java.time.Duration;
//import junit.framework.Assert;
import org.junit.Test;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author admin
 */
public class MyTest {
    @BeforeAll
    public static void setUpClass() {
        System.out.println("BEFORE ALL");
    }
    @AfterAll
    public static void tearDownClass() {
        System.out.println("AFTER ALL");
    }
    
    @BeforeEach
    public void setUp() {
        System.out.println("BEFORE EACH");
    }
    
    @AfterEach
    public void tearDown() {
        System.out.println("BEFORE EACH");
    }
    
    @Test
    @DisplayName("....")
    @Tag("critical")
    public void testEvenNumber() {
        int input = 2;
        boolean expectedOutput = true;
        boolean actualOutput = DemoService.isNt(input);
        
//        Assert.assertEquals();
        Assertions.assertEquals(expectedOutput, actualOutput);
    }
    
    @Test
    public void testWrongEvenNumber() {
        int input = 4;
        boolean expectedOutput = false;
        boolean actualOutput = DemoService.isNt(input);
        
        Assertions.assertEquals(expectedOutput, actualOutput);
    }
    
    @Test
    public void testOddNumber() {
        int input = 11;
        boolean expectedOutput = true;
        boolean actualOutput = DemoService.isNt(input);
        
        Assertions.assertEquals(expectedOutput, actualOutput);
    }
    
    @Test
    public void testTimeout() {
        Assertions.assertTimeoutPreemptively(Duration.ofSeconds(1), () -> {
            DemoService.isNt(9999);
        });
    }
    
    @Test
    public void testEx() {
        Assertions.assertThrows(ArithmeticException.class, () -> {
            DemoService.isNt(-11);
        });
    }
    
    
}
