### MySQL

##### 1. group by

列名经过group by之后，该列名就会被逐一列举出来，单独算一行，列名牵扯聚合函数一般不会group by。

##### 2. cast(column_name as decimal(10,3))

##### 3. limit 3只显示前三行，不足就全显示

##### 4. '值' time对时间非日期格式化，去重是有整行一样才会去重，所以取那几列来去重

##### 5. select可以在列名中参与计算

```mysql
        select
            sum(c) sales_total,
            sum(c) / (
                select
                    count(*)
                from
                    e
            )
        from
            a
```

