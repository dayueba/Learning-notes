# bug

## 无法连接MongoDB的在线免费服务

![1552545741278](C:\Users\xuan\AppData\Local\Temp\1552545741278.png)

把ip地址添加到白名单


## 第三方库 照着github上的文档写 结果错了 
原因是github上的文档和 下载的不是一个版本 以为下载的都是最新版本 所有搞错了


## flutter打包成Android apk以后 无法使用网络
```
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
```
添加到android/src/main/AndroidManifest.xml里
