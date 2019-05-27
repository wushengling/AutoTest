package com.course.testng.parameter;

import org.testng.annotations.Parameters;
import org.testng.annotations.Test;

/**
 * 参数化测试 通过xml文件
 */
public class ParameterTest {
    @Test
    @Parameters({"name","age"})
    public void parameterTest1(String name,int age){
        System.out.println("name = "+ name +"; age = "+ age);
    }
}
