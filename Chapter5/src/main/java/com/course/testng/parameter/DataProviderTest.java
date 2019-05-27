package com.course.testng.parameter;

import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

/**
 * 参数化测试,通过DataProviderTest参数化
 */
public class DataProviderTest {

    @Test(dataProvider = "data")
    public void testDataProvider(String name,int age){
        System.out.println("name = "+ name +"; age = "+ age);
    }
    @DataProvider(name = "data")
    public Object [][] providerData(){
        Object[][] o = new Object[][]{
                {"不高兴",18},
                {"不知道",17},
                {"不晓得",100}
        };
        return o;
    }
}
