package com.course.controller;

import com.course.model.User;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;


@RestController
@Api(value = "v1",description = "这是我第一个版本的demo")
@RequestMapping("v1")
public class Demo {

    //首先获取一个执行sql语句的对象
    @Autowired
    private SqlSessionTemplate template;

    @RequestMapping(value = "/getUserList",method = RequestMethod.GET)
        @ApiOperation(value = "可以获取到用户数",httpMethod = "GET")
        public int getUserCount(){
            return  template.selectOne("getUserCount");
        }

        @RequestMapping(value = "/addUser",method = RequestMethod.POST)
        @ApiOperation(value = "新增用户",httpMethod = "POST")
        public int addUser(@RequestBody User user){
            int result =  template.insert("addUser",user);
            return result;
        }

        @RequestMapping(value = "/updateUser",method = RequestMethod.POST)
        @ApiOperation(value = "更新",httpMethod = "POST")
        public int updateUser(@RequestBody User user){
            return template.update("updateUser",user);
        }

        @RequestMapping(value = "/deleteUser",method = RequestMethod.DELETE)
        @ApiOperation(value = "删除",httpMethod = "DELETE")
        public int delUser(@RequestParam int id){
            return template.delete("deleteUser",id);
        }

        @RequestMapping(value = "/test",method = RequestMethod.GET)
        @ApiOperation(value = "查询id为1,name",httpMethod = "GET")
        public String test(){
            return template.selectOne("test");
        }
}
