package com.course.testng.parameter;

import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import java.lang.reflect.Method;

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

    //通过不同的方法名,传不同的参数
    @Test(dataProvider = "methodData")
    public void test1(String name ,int age){
        System.out.println("test1111方法"+"name = "+ name +"; age = "+ age);
    }

    @Test(dataProvider = "methodData")
    public void test2(String name ,int age){
        System.out.println("test2222方法"+"name = "+ name +"; age = "+ age);
    }

    @DataProvider(name = "methodData")
    public Object[] [] methodDataTest(Method method){
        Object[][] result = null;
        if (method.getName().equals("test1")){
            result = new Object[][]{
                    {"不高兴",18},
                    {"不知道",17},
                    {"不晓得",100}
            };
        }else if (method.getName().equals("test2")){
            result = new Object[][]{
                    {"高兴",18},
                    {"知道",17},
                    {"晓得",100}
            };
        }
        return result;
    }

}
