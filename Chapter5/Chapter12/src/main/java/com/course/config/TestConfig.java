package com.course.config;

import org.apache.http.client.CookieStore;
import org.apache.http.impl.client.DefaultHttpClient;

public class TestConfig {
    public static String loginUrl;
    public static String updateUserInfoUrl;
    public static String getUserListUrl;
    public static String getUserInfoUrl;
    public static String addUserUrl;
    //声明http客户端
    public static DefaultHttpClient httpClient;
    //用来存储cookies信息的变量
    public static CookieStore store;

}
