# Home Credit 字段中文对照

这份文档根据 `HomeCredit_columns_description.csv` 整理，目标是帮助你在做 `application_train.csv` 和后续几张关联表时，能快速看懂字段含义。

## 先记 6 个常见前缀/后缀

- `SK_ID_*`：主键/编号，用于关联表
- `AMT_*`：金额类字段
- `CNT_*`：计数类字段
- `DAYS_*`：相对申请日的天数，通常是负数
- `FLAG_*`：是否、标记类字段，常见取值 `1/0`
- `NAME_*` / `CODE_*`：类别型字段，表示类型、名称、编码

## 先记 3 个很常见的统计后缀

- `_AVG`：平均值
- `_MODE`：众数或最常见值
- `_MEDI`：中位数

## 1. `application_{train|test}.csv`

### 1.1 主键与目标变量

- `SK_ID_CURR`：当前贷款申请 ID
- `TARGET`：目标变量，`1` 表示客户有还款困难，`0` 表示其他情况

### 1.2 当前申请的基本信息

- `NAME_CONTRACT_TYPE`：贷款合同类型，现金贷或循环贷
- `CODE_GENDER`：客户性别
- `FLAG_OWN_CAR`：是否有车
- `FLAG_OWN_REALTY`：是否有房产
- `CNT_CHILDREN`：子女人数
- `AMT_INCOME_TOTAL`：客户总收入
- `AMT_CREDIT`：本次贷款金额
- `AMT_ANNUITY`：本次贷款年金/每期应还金额
- `AMT_GOODS_PRICE`：商品价格，常见于消费贷
- `NAME_TYPE_SUITE`：申请贷款时陪同人员类型
- `NAME_INCOME_TYPE`：收入类型
- `NAME_EDUCATION_TYPE`：最高学历
- `NAME_FAMILY_STATUS`：婚姻/家庭状态
- `NAME_HOUSING_TYPE`：住房情况

### 1.3 地区、年龄、工作与稳定性

- `REGION_POPULATION_RELATIVE`：客户所在地区的人口相对指标，值越大通常表示地区人口越多
- `DAYS_BIRTH`：申请时年龄对应的天数，通常为负数
- `DAYS_EMPLOYED`：当前工作开始距申请日多少天，通常为负数
- `DAYS_REGISTRATION`：最近一次变更登记信息距申请日多少天
- `DAYS_ID_PUBLISH`：最近一次更新身份证件距申请日多少天
- `OWN_CAR_AGE`：车辆车龄

### 1.4 联系方式与身份信息

- `FLAG_MOBIL`：是否提供手机号
- `FLAG_EMP_PHONE`：是否提供工作电话
- `FLAG_WORK_PHONE`：是否提供家庭电话/工作相关电话
- `FLAG_CONT_MOBILE`：手机号是否可联系
- `FLAG_PHONE`：是否提供家庭电话
- `FLAG_EMAIL`：是否提供邮箱
- `OCCUPATION_TYPE`：职业类型
- `CNT_FAM_MEMBERS`：家庭成员人数

### 1.5 区域评级与申请时间

- `REGION_RATING_CLIENT`：客户所在地区评级
- `REGION_RATING_CLIENT_W_CITY`：考虑城市后的地区评级
- `WEEKDAY_APPR_PROCESS_START`：申请发生在星期几
- `HOUR_APPR_PROCESS_START`：申请发生的大致小时

### 1.6 地址/工作地是否一致

- `REG_REGION_NOT_LIVE_REGION`：户籍地区与居住地区是否不同
- `REG_REGION_NOT_WORK_REGION`：户籍地区与工作地区是否不同
- `LIVE_REGION_NOT_WORK_REGION`：居住地区与工作地区是否不同
- `REG_CITY_NOT_LIVE_CITY`：户籍城市与居住城市是否不同
- `REG_CITY_NOT_WORK_CITY`：户籍城市与工作城市是否不同
- `LIVE_CITY_NOT_WORK_CITY`：居住城市与工作城市是否不同

### 1.7 工作单位与外部风险评分

- `ORGANIZATION_TYPE`：工作单位类型
- `EXT_SOURCE_1`：外部数据源评分 1，已标准化
- `EXT_SOURCE_2`：外部数据源评分 2，已标准化
- `EXT_SOURCE_3`：外部数据源评分 3，已标准化

### 1.8 房屋/建筑信息字段的统一理解

这组字段很多，但可以按“前缀 + 后缀”来记。它们都表示客户住房或楼宇信息，且多数已经标准化。

#### 常见前缀

- `APARTMENTS`：公寓面积
- `BASEMENTAREA`：地下室面积
- `YEARS_BEGINEXPLUATATION`：房屋投入使用年份相关信息
- `YEARS_BUILD`：建造年份相关信息
- `COMMONAREA`：公共区域面积
- `ELEVATORS`：电梯相关信息
- `ENTRANCES`：入口数量相关信息
- `FLOORSMAX`：最高楼层相关信息
- `FLOORSMIN`：最低楼层相关信息
- `LANDAREA`：土地面积
- `LIVINGAPARTMENTS`：居住用公寓数量/面积相关信息
- `LIVINGAREA`：居住面积
- `NONLIVINGAPARTMENTS`：非居住公寓相关信息
- `NONLIVINGAREA`：非居住面积

#### 这 14 个前缀都分别有三种后缀

- `_AVG`：平均值版本
- `_MODE`：众数版本
- `_MEDI`：中位数版本

也就是说，下面这些字段可以统一按这个规则理解：

- `APARTMENTS_AVG` / `APARTMENTS_MODE` / `APARTMENTS_MEDI`
- `BASEMENTAREA_AVG` / `BASEMENTAREA_MODE` / `BASEMENTAREA_MEDI`
- `YEARS_BEGINEXPLUATATION_AVG` / `YEARS_BEGINEXPLUATATION_MODE` / `YEARS_BEGINEXPLUATATION_MEDI`
- `YEARS_BUILD_AVG` / `YEARS_BUILD_MODE` / `YEARS_BUILD_MEDI`
- `COMMONAREA_AVG` / `COMMONAREA_MODE` / `COMMONAREA_MEDI`
- `ELEVATORS_AVG` / `ELEVATORS_MODE` / `ELEVATORS_MEDI`
- `ENTRANCES_AVG` / `ENTRANCES_MODE` / `ENTRANCES_MEDI`
- `FLOORSMAX_AVG` / `FLOORSMAX_MODE` / `FLOORSMAX_MEDI`
- `FLOORSMIN_AVG` / `FLOORSMIN_MODE` / `FLOORSMIN_MEDI`
- `LANDAREA_AVG` / `LANDAREA_MODE` / `LANDAREA_MEDI`
- `LIVINGAPARTMENTS_AVG` / `LIVINGAPARTMENTS_MODE` / `LIVINGAPARTMENTS_MEDI`
- `LIVINGAREA_AVG` / `LIVINGAREA_MODE` / `LIVINGAREA_MEDI`
- `NONLIVINGAPARTMENTS_AVG` / `NONLIVINGAPARTMENTS_MODE` / `NONLIVINGAPARTMENTS_MEDI`
- `NONLIVINGAREA_AVG` / `NONLIVINGAREA_MODE` / `NONLIVINGAREA_MEDI`

#### 其他住房相关字段

- `FONDKAPREMONT_MODE`：房屋维修基金相关信息
- `HOUSETYPE_MODE`：房屋类型
- `TOTALAREA_MODE`：总面积相关信息
- `WALLSMATERIAL_MODE`：墙体材料
- `EMERGENCYSTATE_MODE`：紧急状态相关信息

### 1.9 社交圈风险、手机变更、证件提交

- `OBS_30_CNT_SOCIAL_CIRCLE`：客户社交圈中 30 天逾期相关观察数量
- `DEF_30_CNT_SOCIAL_CIRCLE`：客户社交圈中 30 天逾期违约数量
- `OBS_60_CNT_SOCIAL_CIRCLE`：客户社交圈中 60 天逾期相关观察数量
- `DEF_60_CNT_SOCIAL_CIRCLE`：客户社交圈中 60 天逾期违约数量
- `DAYS_LAST_PHONE_CHANGE`：最近一次换手机号距申请日多少天

### 1.10 证件提交标记

下面这组都表示“是否提交某类文件”：

- `FLAG_DOCUMENT_2` 到 `FLAG_DOCUMENT_21`

可以统一理解为：提交文档 2 到文档 21 的标记变量。

### 1.11 征信查询次数

- `AMT_REQ_CREDIT_BUREAU_HOUR`：申请前 1 小时内征信查询次数
- `AMT_REQ_CREDIT_BUREAU_DAY`：申请前 1 天内征信查询次数
- `AMT_REQ_CREDIT_BUREAU_WEEK`：申请前 1 周内征信查询次数
- `AMT_REQ_CREDIT_BUREAU_MON`：申请前 1 月内征信查询次数
- `AMT_REQ_CREDIT_BUREAU_QRT`：申请前 3 个月内征信查询次数
- `AMT_REQ_CREDIT_BUREAU_YEAR`：申请前 1 年内征信查询次数

## 2. `bureau.csv`

这张表表示客户在外部征信机构中的历史贷款记录。

- `SK_ID_CURR`：当前客户 ID
- `SK_BUREAU_ID`：征信历史贷款记录 ID
- `CREDIT_ACTIVE`：征信贷款当前状态
- `CREDIT_CURRENCY`：征信贷款币种
- `DAYS_CREDIT`：这笔征信贷款距当前申请日多少天
- `CREDIT_DAY_OVERDUE`：当前逾期天数
- `DAYS_CREDIT_ENDDATE`：征信贷款距离结束还有多少天
- `DAYS_ENDDATE_FACT`：征信贷款实际结束距当前申请日多少天
- `AMT_CREDIT_MAX_OVERDUE`：历史最大逾期金额
- `CNT_CREDIT_PROLONG`：贷款展期次数
- `AMT_CREDIT_SUM`：当前贷款总额
- `AMT_CREDIT_SUM_DEBT`：当前剩余债务
- `AMT_CREDIT_SUM_LIMIT`：信用卡类授信额度
- `AMT_CREDIT_SUM_OVERDUE`：当前逾期金额
- `CREDIT_TYPE`：征信贷款类型
- `DAYS_CREDIT_UPDATE`：最近一次征信信息更新距当前申请日多少天
- `AMT_ANNUITY`：该笔征信贷款的年金/期供

## 3. `bureau_balance.csv`

这张表是 `bureau.csv` 的按月状态明细。

- `SK_BUREAU_ID`：征信贷款记录 ID，可关联 `bureau.csv`
- `MONTHS_BALANCE`：相对申请日的月份，`-1` 常表示最近一个月
- `STATUS`：该月贷款状态

`STATUS` 常见理解：

- `C`：已关闭
- `X`：状态未知
- `0`：无逾期
- `1`：逾期 1-30 天
- `2`：逾期 31-60 天
- `3`：逾期 61-90 天
- `4`：逾期 91-120 天
- `5`：逾期 120 天以上或核销/转卖

## 4. `POS_CASH_balance.csv`

这张表记录客户之前 POS 贷/现金贷的月度余额。

- `SK_ID_PREV`：历史贷款 ID
- `SK_ID_CURR`：当前客户 ID
- `MONTHS_BALANCE`：相对申请日的月份
- `CNT_INSTALMENT`：历史贷款总期数
- `CNT_INSTALMENT_FUTURE`：剩余未还期数
- `NAME_CONTRACT_STATUS`：该月合同状态
- `SK_DPD`：该月逾期天数
- `SK_DPD_DEF`：考虑容忍规则后的逾期天数

## 5. `credit_card_balance.csv`

这张表记录客户历史信用卡账户的月度信息。

- `SK_ID_PREV`：历史信用卡账户 ID
- `SK_ID_CURR`：当前客户 ID
- `MONTHS_BALANCE`：相对申请日的月份
- `AMT_BALANCE`：当月余额
- `AMT_CREDIT_LIMIT_ACTUAL`：信用额度
- `AMT_DRAWINGS_ATM_CURRENT`：ATM 取现金额
- `AMT_DRAWINGS_CURRENT`：当月总支取/消费金额
- `AMT_DRAWINGS_OTHER_CURRENT`：其他支取金额
- `AMT_DRAWINGS_POS_CURRENT`：刷卡消费金额
- `AMT_INST_MIN_REGULARITY`：当月最低应还款额
- `AMT_PAYMENT_CURRENT`：当月已还金额
- `AMT_PAYMENT_TOTAL_CURRENT`：当月总还款额
- `AMT_RECEIVABLE_PRINCIPAL`：应收本金
- `AMT_RECIVABLE`：应收金额
- `AMT_TOTAL_RECEIVABLE`：应收总额
- `CNT_DRAWINGS_ATM_CURRENT`：ATM 取现次数
- `CNT_DRAWINGS_CURRENT`：总支取次数
- `CNT_DRAWINGS_OTHER_CURRENT`：其他支取次数
- `CNT_DRAWINGS_POS_CURRENT`：消费次数
- `CNT_INSTALMENT_MATURE_CUM`：已完成分期累计次数
- `NAME_CONTRACT_STATUS`：合同状态
- `SK_DPD`：当月逾期天数
- `SK_DPD_DEF`：考虑容忍规则后的逾期天数

## 6. `previous_application.csv`

这张表记录客户在 Home Credit 的历史申请。

- `SK_ID_PREV`：历史申请 ID
- `SK_ID_CURR`：当前客户 ID
- `NAME_CONTRACT_TYPE`：历史申请合同类型
- `AMT_ANNUITY`：历史申请年金/期供
- `AMT_APPLICATION`：历史申请金额
- `AMT_CREDIT`：历史申请最终获批贷款金额
- `AMT_DOWN_PAYMENT`：首付款金额
- `AMT_GOODS_PRICE`：申请对应商品价格
- `WEEKDAY_APPR_PROCESS_START`：历史申请发生在星期几
- `HOUR_APPR_PROCESS_START`：历史申请发生的大致小时
- `FLAG_LAST_APPL_PER_CONTRACT`：是否为该合同最后一次申请
- `NFLAG_LAST_APPL_IN_DAY`：是否为当日最后一次申请
- `NFLAG_MICRO_CASH`：是否为小额现金贷
- `RATE_DOWN_PAYMENT`：首付比例，已标准化
- `RATE_INTEREST_PRIMARY`：主利率，已标准化
- `RATE_INTEREST_PRIVILEGED`：优惠利率，已标准化
- `NAME_CASH_LOAN_PURPOSE`：现金贷用途
- `NAME_CONTRACT_STATUS`：历史申请状态，是否批准/取消/拒绝
- `DAYS_DECISION`：历史申请审批决定距当前申请日多少天
- `NAME_PAYMENT_TYPE`：还款方式
- `CODE_REJECT_REASON`：历史申请被拒原因
- `NAME_TYPE_SUITE`：申请时陪同人员类型
- `NAME_CLIENT_TYPE`：新客户还是老客户
- `NAME_GOODS_CATEGORY`：申请商品类别
- `NAME_PORTFOLIO`：产品组合/业务线
- `NAME_PRODUCT_TYPE`：产品类型
- `CHANNEL_TYPE`：获客渠道
- `SELLERPLACE_AREA`：销售地点区域
- `NAME_SELLER_INDUSTRY`：卖方行业
- `CNT_PAYMENT`：历史贷款期数
- `NAME_YIELD_GROUP`：收益率分组
- `PRODUCT_COMBINATION`：产品组合明细
- `DAYS_FIRST_DRAWING`：首次放款距当前申请日多少天
- `DAYS_FIRST_DUE`：首次应还款日距当前申请日多少天
- `DAYS_LAST_DUE_1ST_VERSION`：初始约定最后还款日距当前申请日多少天
- `DAYS_LAST_DUE`：最后还款日距当前申请日多少天
- `DAYS_TERMINATION`：预计终止日距当前申请日多少天
- `NFLAG_INSURED_ON_APPROVAL`：审批时是否附带保险

## 7. `installments_payments.csv`

这张表记录历史分期还款明细。

- `SK_ID_PREV`：历史贷款 ID
- `SK_ID_CURR`：当前客户 ID
- `NUM_INSTALMENT_VERSION`：分期计划版本
- `NUM_INSTALMENT_NUMBER`：第几期分期
- `DAYS_INSTALMENT`：应还款日期距当前申请日多少天
- `DAYS_ENTRY_PAYMENT`：实际付款日期距当前申请日多少天
- `AMT_INSTALMENT`：应还金额
- `AMT_PAYMENT`：实际支付金额

## 8. 初学者最值得先盯住的字段

如果你当前只做 `application_train.csv` 的基础 EDA，最值得优先理解的是这几个：

- `TARGET`：是否违约
- `AMT_INCOME_TOTAL`：收入
- `AMT_CREDIT`：贷款金额
- `AMT_ANNUITY`：每期还款额
- `AMT_GOODS_PRICE`：商品价格
- `DAYS_BIRTH`：年龄
- `DAYS_EMPLOYED`：工作时长
- `EXT_SOURCE_1` / `EXT_SOURCE_2` / `EXT_SOURCE_3`：外部风险评分

## 9. 使用建议

- 看 `DAYS_*` 字段时，先记住它们大多是“相对申请日”的负数
- 看 `FLAG_*` 字段时，通常按 `1=是, 0=否` 理解
- 看 `AMT_*` 字段时，优先思考“收入、贷款、还款压力”之间的关系
- 看 `EXT_SOURCE_*` 时，可以把它们先理解为外部风险评分
- 房屋相关字段很多，不建议一开始逐个死记，更适合按前缀和后缀理解
