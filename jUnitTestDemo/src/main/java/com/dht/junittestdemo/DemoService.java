/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.dht.junittestdemo;

import java.time.Duration;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author admin
 */
public class DemoService {
    public static boolean isNt(int n) {
        
//        try {
            if (n < 0)
                throw new ArithmeticException();
            
//            Thread.sleep(Duration.ofSeconds(2));
            if (n < 2)
                return false;
            for (int i = 2; i < Math.sqrt(n); i++)
                if (n % 2 == 0)
                    return false;
            return true;
//        } catch (InterruptedException ex) {
//            Logger.getLogger(DemoService.class.getName()).log(Level.SEVERE, null, ex);
//        }
//        
//        return false;
    }
}
