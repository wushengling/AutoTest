package com.course.model;

import lombok.Data;

@Data
public class GetUserListCase {
    private int id;
    private String userName;
    private int age;
    private int sex;
    private String expected;

//    public String toString(){
//        return (
//                "{id:"+id+","+
//                "userName:"+userName+","+
//                "age:"+age+","+
//                "sex:"+sex+","+
//                "expected:"+expected+"}"
//                );
//    }
}
