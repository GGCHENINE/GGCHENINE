### `record.py` 中 18 个练习题目汇总（含题目内容）

#### 1）exercise1  
**内容**：  
- 定义函数 `exercise1()`，打印 `"Hello, World!"`。  
**练习点**：最基本的函数与输出。

---

#### 2）exercise2  
**内容**：  
- 定义 `a=10`、`b=20`，打印两数之和：`a+b=` 及结果。  
**练习点**：变量、加法、`print`。

---

#### 3）exercise3  
**内容**：  
- 设定 `score = 80`，用 `if/else` 判断并打印 “及格” 或 “不及格”（虽然逻辑有点反直觉，但本质是练条件分支）。  
**练习点**：单分支判断。

---

#### 4）exercise4  
**内容**：  
- 使用 `input()` 读入一个成绩（转为 `int`），根据区间输出：  
  - `>=90`：优秀  
  - `>=80` 且 `<90`：良好  
  - `>=60` 且 `<80`：及格  
  - `<60`：不及格  
**练习点**：`input`、类型转换、多分支区间判断。

---

#### 5）exercise5  
**内容**：  
- 输入语文、数学两门成绩。  
- 根据两科是否 ≥60，输出四种组合（两科都及格 / 一科及格 / 都不及格）。  
- 再计算并打印两门的总分和平均分。  
**练习点**：多个条件与 `and` 组合、总分和平均值。

---

#### 6）exercise6  
**内容**：  
- 有一周每天的消费列表：`[50,80,120,30,0,200,60]`。  
- 计算一周总消费，判断是否 `>500`（“消费偏高”或“正常”），再算一周平均消费。  
**练习点**：遍历列表求和、简单规则判断、平均值。

---

#### 7）exercise7  
**内容**：  
- 有分数列表：`[88, 92, 75, 63, 99, 81]`。  
- 在一次遍历中计算：最高分、最低分、总分、平均分，并打印。  
**练习点**：最大值 / 最小值 / 总和 / 平均值模板。

---

#### 8）exercise8  
**内容**：  
- 有步数列表：`[3200, 8100, 5200, 0, 4500, 12000, 6800]`。  
- 计算最大步数、最小步数、总步数、平均步数。  
**练习点**：与 7 类似，复习统计模板。

---

#### 9）exercise9  
**内容**：  
- 有成绩列表：`[88, 45, 62, 90, 58, 73, 0, 100]`。  
- 统计 `>=60` 的人数（及格）和 `<60` 的人数（不及格），并打印。  
**练习点**：两个计数器在循环中分别累加。

---

#### 10）exercise10 —— 风控入门：交易规则打分与拦截  
**内容**：  
- 金额列表：`[12, 880, 55, 3000, 120, 499, 500, 501, 0, -20, 9999]`。  
- 每笔从 `risk = 0` 开始，根据规则加分：  
  - A：`amt <= 0` → `+100`  
  - B：`amt > 5000` → `+60`  
  - C：`500 < amt <= 5000` → `+30`  
  - D：`amt` 在 `{499, 500, 501}` 中 → `+20`  
  - E：`amt` 为偶数 → `+5`  
- 若该笔 `risk >= 60` → 标记为 `BLOCK`，否则 `PASS`。  
- 对每笔打印：`amt=<金额> risk=<风险分> <PASS/BLOCK>`。  
- 最后汇总打印：  
  - `PASS=<数量>`  
  - `BLOCK=<数量>`  
  - `max_risk=<最大风险分>`  
  - `avg_risk=<平均风险分>`（保留 2 位小数）。  
**练习点**：多规则叠加 vs 互斥、每笔单独计算、总和/最大值/平均值统计。

---

#### 11）exercise11 —— 连续失败次数与最长连续失败  
**内容**：  
- 事件序列：  
  `events = ["PASS","PASS","BLOCK","BLOCK","BLOCK","PASS","BLOCK","PASS","PASS","BLOCK","BLOCK"]`  
- 遍历时维护：  
  - `streak`：当前连续 `BLOCK` 的长度（遇到 PASS 归零）。  
  - `max_block_streak`：历史最长的连续 `BLOCK` 长度。  
  - `block_segments`：`BLOCK` 段数（每次从非 BLOCK 切换到 BLOCK 计一段）。  
  - `pass_count` / `block_count`：总 PASS / BLOCK 次数。  
- 每一步打印：`i=<索引> event=<当前值> streak=<当前连续BLOCK长度>`。  
- 最终打印：  
  - `PASS=<数量>`  
  - `BLOCK=<数量>`  
  - `block_segments=<BLOCK 段数>`  
  - `max_block_streak=<最长连续 BLOCK 次数>`  
**练习点**：  
- 连续计数（streak 模板）。  
- 利用“当前 + 上一条”判断新段开始。  
- `enumerate` 同时获取索引和元素。

---

#### 12）exercise12 —— 逻辑练习：背单词统计  
**内容**：  
- 每天背单词数量：`[10, 15, 0, 20, 25, 30, 5, 5, 40]`。  
- 统计并打印：  
  - 背单词天数（>0 的天数）。  
  - 没背单词天数（==0 的天数）。  
  - 单日最多背单词数。  
  - 平均每天背单词数量（保留 2 位小数）。  
**练习点**：分条件计数、最大值、平均值。

---

#### 13）exercise13 —— 近 7 天消费总额 & 超阈值天数  
**内容**：  
- 消费金额列表：`[120, 0, 300, 80, 500, 1000, 30, 60, 700, 0, 50, 400]`。  
- 统计并打印：  
  - `total_amount`：总消费金额。  
  - `high_days`：消费金额 `>= 500` 的天数。  
  - `max_amount`：单日最大消费。  
  - `avg_amount`：平均每天消费金额（所有天数上平均，保留 2 位小数）。  
**练习点**：条件计数 + 最大值 + 平均值。

---

#### 14）exercise14 —— 黑名单 + 大额风控规则（引入字典）  
**内容**：  
- 交易列表（每笔有用户和金额）：  
  ```python
  transactions = [
      {"user_id": "u1", "amount": 100},
      {"user_id": "u2", "amount": 800},
      {"user_id": "u3", "amount": 5000},
      {"user_id": "u1", "amount": 2000},
      {"user_id": "u4", "amount": 50},
      {"user_id": "u2", "amount": 1200},
  ]
  blacklist = ["u2", "u5"]
  ```  
- 对每笔交易打标签：  
  - 若 `user_id` 在黑名单 → `tag="BLACKLIST"`  
  - 否则若 `amount >= 2000` → `tag="HIGH_AMOUNT"`  
  - 否则 → `tag="NORMAL"`  
- 每笔打印：`user=<uid> amount=<amt> tag=<tag>`。  
- 最后汇总打印：  
  - `BLACKLIST=<数量>`  
  - `HIGH_AMOUNT=<数量>`  
  - `NORMAL=<数量>`  
**练习点**：  
- 遍历“字典列表”。  
- 黑名单优先级高于大额。  
- 用计数器统计各标签数量。

---

#### 15）exercise15 —— 按用户统计风险特征（字典聚合）  
**内容**：  
- 同样的交易列表（有 `user_id` 和 `amount`）。  
- 按用户统计：  
  - `total`：每个用户总金额。  
  - `count`：每个用户交易笔数。  
  - `max`：每个用户最大单笔金额。  
- 每个用户打印一行：  
  `user=<uid> total=<total> count=<count> max=<max>`。  
**练习点**：  
- `stats = {user_id: {"total":..., "count":..., "max":...}}` 结构。  
- `if uid not in stats:` 初始化，然后在 `stats[uid][...]` 上累加/更新。

---

#### 16）exercise16 —— 按“省份 + 风险标签”统计  
**内容**：  
- 交易列表增加 `province` 和 `tag`：  
  ```python
  {"user_id": "u1", "province": "BJ", "tag": "NORMAL"}, ...
  ```  
- 按省份统计：  
  - `count`：该省交易总笔数。  
  - `black_count`：`tag == "BLACKLIST"` 的笔数。  
  - `high_count`：`tag == "HIGH_RISK"` 的笔数。  
- 每个省打印一行：  
  `province=<省份> count=<总笔数> black=<黑名单笔数> high=<高风险笔数>`。  
**练习点**：  
- 以 `province` 为 key 做聚合：`stats[prov] = {"count":..., "black_count":..., "high_count":...}`。  
- 在一趟遍历中维护多种计数。

---

#### 17）exercise17 —— 按“用户 + 风险标签”做二维统计  
**内容**：  
- 交易列表有 `user_id` 和 `tag`：`NORMAL / HIGH_RISK / BLACKLIST`。  
- 按用户统计：  
  - `count`：总交易笔数。  
  - `normal`：`tag == "NORMAL"` 的笔数。  
  - `high`：`tag == "HIGH_RISK"` 的笔数。  
  - `black`：`tag == "BLACKLIST"` 的笔数。  
- 每个用户打印一行：  
  `user=<uid> count=<count> normal=<normal> high=<high> black=<black>`。  
**练习点**：  
- 同一 key（用户）下的多个标签计数。  
- 使用 `stats[uid]` 的多字段结构。

---

#### 18）exercise18 —— 综合小项目：用户风险画像  
**内容**：  
- 交易列表包含 `user_id`、`amount`、`tag`。  
- 按用户构建“风险画像”，统计：  
  - `count`：总交易笔数。  
  - `total`：总金额。  
  - `max`：最大单笔金额。  
  - `high_count`：`amount >= 2000` 的笔数。  
  - `high_tag_count`：`tag == "HIGH_RISK"` 的笔数。  
  - `black_tag_count`：`tag == "BLACKLIST"` 的笔数。  
- 每个用户打印一行：  
  `user=<uid> count=<count> total=<total> max=<max> high_count=<高额次数> high_tag=<高风险标签次数> black_tag=<黑名单标签次数>`。  
**练习点**：  
- 把前面所有统计技巧综合起来，做用户层面的风险特征聚合。  
