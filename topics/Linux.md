

### Linux

#### 文件目录

##### 1. ls 列出当前目录内容可以指定

![](../picturs/0022.png)

-l 详细信息；

-a 全部文件包括隐藏文件；

-h 人可识别大小。

##### 2. cd 切换目录

![](../picturs/23.png)

##### 3. pwd 打印当前工作目录

![](../picturs/24.png)

##### 4. mkdir 创建目录

![](../picturs/25.png)

-p 递归创建目录；只能创建目录，mkdir dir1单层目录。

##### 5. rm 删除文件或者目录

![](../picturs/26.png)

-r 递归；

-f 强制且不显示删除过程信息。

##### 6. cp 复制指定目录到指定目录

![](../picturs/27.png)

-r 递归；

-i 覆盖前提示。

##### 7. mv 移动或者重命名

![](../picturs/28.png)

##### 8. touch 创建单个或者多个空文件或者更改文件的时间戳

![](../picturs/29.png)

##### 9. cat 显示文件全部内容

![](../picturs/30.png)

-n 显示行号。

##### 10. less 适合大文件查看和匹配

- /keyword 匹配关键字；

  ![](../picturs/36.png)


- page up 上一页； page down下一页；g首行；G尾行；q退出。

##### 11. head显示靠首行的行

-n 控制显示几行。

![](../picturs/37.png)


##### 12. tail显示靠行尾的行

-n 控制显示行数；

-f 实时显示（常用）；

![](../picturs/38.png)


-F 跟踪滚动日志。

##### 13. whoami 查看当前用户

![](../picturs/39.png)

##### 14. su 切换用户

![](../picturs/40.png)


##### 15. 查看全部用户

冒号前的第一列全是用户

![](../picturs/41.png)

##### 16. groups 查看当前的组

groups 直接查看当前用户的组

![](../picturs/42.png)

groups 用户名：查看特定用户名的组

![](../picturs/43.png)

##### 17. id 查看当前目录用户更详细的信息

![](../picturs/44.png)




#### 权限管理

##### 1. chmod

\+ 赋予权限r w x；

\- 回收权限r w x；

![](../picturs/45.png)

只针对当前用户

4 = r; 2 = w ; 1 = x;

-R 递归赋予或者回收权限；

![](../picturs/46.png)


都会没有执行的权限，以前有现在不会有。

##### 2. chown 改用户或者组，可以同时

-R 递归更改。

![](../picturs/47.png)




#### 进程管理

##### 1. ps 进程快照

-aux：可以不带-，一样的效果；a，tty下的全部进程；u，以面向用户的格式；x，显示没有控制终端的进程（守护进程或者后台进程）

![](../picturs/48.png)

该组合参数常用于查看进程状态，资源使用状况，排查性能问题。

-ef：e，显示所有进程（似-A）；f，完整格式显示

![](../picturs/49.png)

该组合参数常用于查看父子进程。

--sort=-列名：-，代表降序；列名，忽略大小写。

![](../picturs/50.png)

##### 2. top 动态查看进程资源

按键p按照cpu降序，c显示完整指令，m按照内存降序，t按执行照时间降序

![](../picturs/51.png)

##### 3. kill 杀死进程

-9 强制杀死；-15 温和杀死，不一定杀死；

kill -9 pid



#### 网络命令

##### 1. ping 测试网络连通性

-c 指定发送次数（发几个包）

![](../picturs/52.png)

##### 2.  ifconfig 查看配置网络结构（ip addr [show]）

![](../picturs/53.png)

##### 3. netstat(network statistics) 

netstat 显示网络连接、路由表和接口统计等信息。

-t 显示tcp；-u 显示UDP；-l 显示正在监听；-n 数字形式显示 ip 和 port

![](../picturs/54.png)

-c 实时刷新；-p显示进程；-a显示全部进程

##### 4. curl 发送http请求

-o 指定请求返回输出路径；-X 指定请求方式；

![](../picturs/55.png)



#### 压缩打包

##### 1. tar 打包解包

-z .tar.gz类型；-c 创建；-v 显示过程；-f 指定要打包成的文件名；-x 解压

![](../picturs/56.png)

![](../picturs/57.png)

##### 2. gzip 压缩解压.gz文件

-d 解压，仅适用于单个大文件。

gzip file.txt 或者 file.tar 

gzip -d file.txt.gz 或者 file.tar.gz



#### 文本处理（重中之重）

##### 1. grep 搜索文本

-i 忽略关键字大小写；-n 显示搜索出来的关键字所在行；-w 精确单词匹配；-v 显示非关键字的所在行的内容；

-r 递归搜索目录；-c 统计匹配的行数；-l 批量查找那些文件包含此关键字；-L 批量查找那些文件不含此关键字；

-m (max) 控制匹配次数；--color 高亮显示关键字；

-A (after) 显示关键字的后几行；-B (before) 显示关键字的前几行；-C (content) 显示关键字的前后各几行；

-P 扩展使用正则表达式；-o (only-matching) 只输出匹配的部分，而不是整行

- ###### task01

统计日志中总共有多少个 `TEST_PASSED` 和 `TEST_FAILED`（不区分大小写）

![](../picturs/58.png)

- task02

找出所有包含 `ERROR` 的行，并显示行号

![](../picturs/59.png)

- ###### task03

反向匹配：找出所有**不包含** `INFO` 的行（只看错误、警告和调试信息）

![](../picturs/60.png)

- ###### task04

递归搜索：假设 logs 目录下有多个子目录，搜索所有文件中包含 `NullPointerException` 的文件（只显示文件名，不显示内容）

![](../picturs/61.png)

- ###### task05

查找 `SQLException` 相关的错误，并显示**后 3 行**（看完整堆栈）

![](../picturs/62.png)

- ###### task06

查找所有 `TEST_FAILED` 的行，并显示**前 1 行**（看是什么测试用例失败了）

![](../picturs/63.png)

- ###### task07

使用 `-o` 参数提取所有 `OrderID=xxx` 的值（只要 OrderID 后面的编号，如 ORD20240221001）

![](../picturs/64.png)

- ###### task08

提取所有 IP 地址（使用正则，提示：数字.数字.数字.数字 格式）

![](../picturs/65.png)

-P 更像re的功能

- ###### task09

精确匹配单词：查找 `error` 但不要匹配到 `SQLException` 或 `TEST_FAILED` 中的 error 部分（用 `-w`）

![](../picturs/66.png)

- ###### task10

统计每种日志级别（ERROR/WARN/INFO）各出现多少次（结合 `sort | uniq -c`）

![](../picturs/67.png)

单独的uniq是去重；wc -l file.txt 统计行数。

- ###### task11

找出所有响应时间超过 1000ms 的接口（提示：查找 `Duration:` 后面大于 1000 的数字，需要正则）

![](../picturs/68.png)

上面可以等于1000

![](../picturs/69.png)

- ###### task12

统计失败率 - 计算 `Failed` 数量占 `Total` 的比例（从最后一行提取数字计算）

![](../picturs/70.png)

直接使用 | 书写两个完整的表达式；NR就是所有行从1开始，NR==1表示第一行；NF 列数。

- ###### task13

写一个脚本命令：如果日志中存在 `CRITICAL` 或 `FATAL`，则输出 "紧急告警"，否则输出 "系统正常"（使用 `-q` 参数）

```shell
#!/bin/bash

num=$(grep -qiP "critical|fatal" test02.txt && echo 1 || echo 0)
echo $num
if [ $num -eq 1 ]; then
        echo "紧急告警"
else
        echo "系统正常"
fi
# if grep -qiP "critical|fatal" test02.txt; then
#	pass
# fi
```

- ###### task14

批量处理：查找所有 `Duration: xxxms` 并提取数字，计算平均响应时间（结合 `awk`）

```shell
#!/bin/bash

value=$(grep -iPo "Duration:\s\K\d+" test02.txt --color)
# echo $value 125 2500
echo $value | awk '{sum=0;for(i=1;i<=NF;i++) sum+=$i} END{print sum/NF}'
# NF 列数；$NF 最后一个值；$NF-1倒数第二个值。
```

##### 2. awk 强大的文本处理工具，按列处理



#### Linux 易错点

##### 1.-P perl比-E更实用，\s可以匹配多个空格

##### 2.$var_name；$(命令表达式)；$((算数表达式)) 是有结果的；[ $((exp1)) -eq 0 ] 算数判断，[ != ] 字符串判断，[[  $((exp1)) -eq 0 && $((exp2)) -eq 1 ]] 

##### 3. $0 : 表示文件；$1 : 表示第一列；$$ : 表示当前脚本进程ID；$? : 表示上一个命令的退出状态（0:success 1:fail）；$! : 最后一个后台运行的进程号；${#car_name[@]} : 长度；${var_name[@]} : 个数。

​	