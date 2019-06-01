# 计数排序

1. 得到数列元素最大值
2. 根据最大值确定统计数组长度 开辟空间
3. 遍历数组 填充统计数组
4. 遍历统计数组 输出结果

## 优化
- 数列的统计数组长度为 最大值-最小值+1 最小值作为偏移量

- 从统计数组第二个元素开始,每一个元素都加上前面所有元素之和<br>
让统计数组存储的元素值为等于相应整数的最终排序位置的序号.<br>
创建输出数组,长度和输入数列一致,然后从后向前遍历数列.<br>

```
    public static void countSort(int[] arr) {
        int max = arr[0];
        int min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min)
                min = arr[i];
            if (arr[i] > max)
                max = arr[i];
        }

        int length = max - min + 1;
        int[] countArr = new int[length];
        for (int i = 0; i < countArr.length; i++) {
            countArr[i] = 0;
        }
        for (int i = 0; i < arr.length; i++) {
            countArr[arr[i] -min]++;
        }

        for (int i = 1; i < countArr.length; i++) {
            countArr[i] += countArr[i-1];
        }
        
        int[] sortedArr = new int[arr.length];
        for (int i = arr.length-1; i >= 0; i--) {
            sortedArr[countArr[arr[i] -min] -1] = arr[i];
            countArr[arr[i] -min] --;
        }

        for (int i = 0; i < arr.length; i++) {
            arr[i] = sortedArr[i];
        }
    }
```

### 局限性
- 最大值和最小值差别过大时不适用
- 数列元素不是整数时也不适用