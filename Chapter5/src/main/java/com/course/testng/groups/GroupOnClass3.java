package com.course.testng.groups;

import org.testng.annotations.Test;

@Test(groups = "teacher")
public class GroupOnClass3 {

    public void teacher1(){
        System.out.println("groupOnClass3中的teacher1111运行");
    }

    public void teacher2(){
        System.out.println("groupOnClass3中的teacher2222运行");
    }
}
