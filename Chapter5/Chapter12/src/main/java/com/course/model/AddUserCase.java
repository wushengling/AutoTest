package com.course.model;

import lombok.Data;

@Data
public class AddUserCase {
    private int id;
    private String userName;
    private String password;
    private int sex;
    private int age;
    private int permission;
    private int isDelete;
    private String expected;
//    public String toString(){
//        return (
//                "{id:"+id+","+
//                "userName:"+userName+","+
//                "password:"+password+","+
//                "age:"+age+","+
//                "sex:"+sex+","+
//                "permission:"+permission+","+
//                "isDelete:"+isDelete+","+
//                "expected"+expected+"}"
//                );
//    }
}
