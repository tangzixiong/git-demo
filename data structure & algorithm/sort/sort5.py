## 堆和堆排序

# 原文链接：https://blog.csdn.net/u010712012/article/details/87207559


# 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树
# 的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

# 堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：

    # 大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
    # 小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；
    # 堆排序的平均时间复杂度为 Ο(nlogn)。

