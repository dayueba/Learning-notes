# 一些和数据结构关系不大的题目

## 求出最大公约数
1. 辗转相除法
    ```
    // 最大公约数为a除以b的余数c和b之间的最大公约数
    public int getGreatestCommonDivisorV2(int a, int b) {
        int big = a > b ? a : b;
        int small = a < b ? a : b;
        if(big % small ==0 )
            return small;
        return getGreatestCommonDivisorV2(big%small, small);
    }
    ```

2. 更相减损术
    ```
    // 最大公约数为a-b的差值c和较小数b的最大公约数
    public int getGreatestCommonDivisorV2(int a, int b) {
        if (a == b)
            return a;
        int big = a > b ? a : b;
        int small = a < b ? a : b;
        return getGreatestCommonDivisorV2(big - small, small);
    }
    ```
3. 相结合
    1. 当a和b都为偶数
        
        gcd(a>>1, b>>1)<<1
    2. 当a为偶数, b为奇数

        gcd(a>>1, b)
    3. 当a为奇数, b为偶数

        gcd(a, b>>1)
    4. 都为奇数

        gcd(b, a-b)


## 判断一个数是否为2的整数次幂
如果一个整数是2的整数次幂, 当它转化为二进制时, 只有最高位为1, 其他位都是0

如果把这个数减一, 则所有位都为1

判断按位相与的结果是否为0即可

```
public boolean isPowerOf2(int num){
    return (num & (num-1)) == 0;
}
```

## 寻找全排列的下一个数
1. 从后向前查看逆序区域, 找到逆序区域的边界
2. 让逆序边界的前一位和逆序区域中大于它的最小的数字交换位置
3. 把原来的逆序区转换为顺序区

## 删去k个数字后的最小值
从左到右比较 如果左边的数字大于右边的数字 则删除

借助栈 

## 大整数相加 
可以利用数组 倒序存储 按位相加
可以9位数存在一个数组里