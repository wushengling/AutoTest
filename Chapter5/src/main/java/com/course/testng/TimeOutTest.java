package com.course.testng;

import org.testng.annotations.Test;

/**
 * 超时测试
 */
public class TimeOutTest {

    @Test(timeOut = 3000)//单位为毫秒值
    public void testSuccess() throws InterruptedException {
        Thread.sleep(2000);
        System.out.println("aaa");
    }

    @Test(timeOut = 2000)//单位为毫秒值
    public void testFailed() throws InterruptedException {
        Thread.sleep(3000);
        System.out.println("bbb");
    }
}
