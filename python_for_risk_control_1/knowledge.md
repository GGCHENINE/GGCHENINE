### 一、基础语法与数据类型

- **变量与赋值**  
  - 用 `=` 给变量赋值：`a = 10`、`score = 80`  
  - 变量名要有意义，如 `total_amount`、`max_score`、`pass_count`。

- **基本数据类型**  
  - 整数 / 浮点数：分数、金额、步数等。  
  - 字符串：`"PASS"`、`"BLOCK"`、`"BLACKLIST"`。  
  - 布尔逻辑：`True/False` 来自比较表达式。

- **输入输出**  
  - `input()` 读取字符串，再用 `int()` 转成数字。  
  - `print()` 输出结果；推荐用 f-string：`print(f"user={uid} amount={amt}")`。

---

### 二、条件判断与规则表达

- **基本条件**  
  - 比较运算：`>=`、`>`、`<`、`<=`、`==`、`!=`。  
  - 逻辑运算：`and`、`or` 组合多个条件。

- **多分支结构**  
  - `if / elif / else`：只会执行其中一支，适合**互斥区间**（成绩分段、金额区间）。  
  - 多个 `if`：每个条件都会独立判断，适合**多条规则叠加**（风控打分）。

- **边界与顺序**  
  - 区间写法：`500 < amt <= 5000`。  
  - 先写“高优先级规则”（如黑名单），再写其他规则。

---

### 三、循环与统计模板

- **`for` 遍历列表**  
  - `for x in list:`：挨个拿到元素。  
  - 常见模式：累加、计数、更新最大/最小值。

- **`enumerate` 取索引和元素**  
  - `for i, event in enumerate(events):`  
  - 用 `i` 看前一个元素：`events[i-1]`，用来判断“新的一段开始”。

- **常用统计模板**  
  - 求和：先 `total = 0`，循环中 `total += x`。  
  - 计数：先 `count = 0`，满足条件时 `count += 1`。  
  - 最大值：先 `max_val = 初始值`，若 `x > max_val` 则更新。  
  - 平均值：`avg = total / len(list)`，可再 `round(avg, 2)`。

---

### 四、列表与字典（风控最常用的数据结构）

- **列表（有序）**  
  - 存一串数值或记录：`amounts = [...]`、`events = [...]`。  
  - 通过索引访问：`events[i]`。

- **字典（key→value 映射）**  
  - 单条记录：`{"user_id": "u1", "amount": 100, "tag": "NORMAL"}`。  
  - 访问字段：`uid = tx["user_id"]`，`amt = tx["amount"]`。

- **嵌套字典做“聚合统计”**  
  - 结构示例：  
    ```python
    stats = {
        "u1": {"total": 2100, "count": 2, "max": 2000},
        "u2": {"total": 2000, "count": 2, "max": 1200},
    }
    ```
  - 新 key 初始化：  
    ```python
    if uid not in stats:
        stats[uid] = {"total": 0, "count": 0, "max": 0}
    ```
  - 更新统计字段：  
    - `stats[uid]["total"] += amt`  
    - `stats[uid]["count"] += 1`  
    - `if amt > stats[uid]["max"]: stats[uid]["max"] = amt`

- **遍历聚合结果**  
  - `for uid, info in stats.items():`  
  - `info["count"]`、`info["total"]`、`info["max"]` 拆出来打印。

---

### 五、风控常见特征模板

- **规则打分（scorecard 思路）**  
  - 每笔从 `risk = 0` 开始。  
  - 每条规则满足就 `risk += 分数`：  
    - 金额区间、大额、卡边金额、异常金额、奇偶等。  
  - 用多个 `if` 做叠加，用 `if/elif` 做互斥区间。

- **拦截决策**  
  - 根据总风险分决定：  
    ```python
    if risk >= 阈值:
        result = "BLOCK"
    else:
        result = "PASS"
    ```

- **连续特征（streak/segment）**  
  - 当前连续长度：`streak`（遇到特定事件 +1，遇到其它事件清零）。  
  - 历史最大连续：`max_streak`。  
  - 段数：当“当前是 BLOCK 且前一个不是 BLOCK”时，`segments += 1`。

- **标签计数**  
  - 按 `tag` 计数：  
    ```python
    if tag == "NORMAL": stats[uid]["normal"] += 1
    if tag == "HIGH_RISK": stats[uid]["high"] += 1
    if tag == "BLACKLIST": stats[uid]["black"] += 1
    ```

- **用户风险画像（多维统计汇总）**  
  - 每个用户维度汇总：总笔数、总金额、最大单笔、高额次数、高风险标签次数、黑名单标签次数。  
  - 输出时用 f-string 清晰展示。

---