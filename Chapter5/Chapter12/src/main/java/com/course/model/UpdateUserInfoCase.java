package com.course.model;

import lombok.Data;

@Data
public class UpdateUserInfoCase {
    private int id;
    private int userId;
    private String userName;
    private int sex;
    private int age;
    private int permission;
    private int isDelete;
    private String expected;

//    public String toString(){
//        return (
//                "{id:"+id+","+
//                "userId:"+userId+","+
//                "userName:"+userName+","+
//                "sex:"+sex+","+
//                "age:"+age+","+
//                "permission:"+permission+","+
//                "isDelete:"+isDelete+","+
//                "expectde:"+expected+"}"
//                );
//    }
}
