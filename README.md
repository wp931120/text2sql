# 大模型prompt engineering 教程
博客地址：https://zhuanlan.zhihu.com/p/635799364

prompt的组成包四个元素：

+ Instruction（指令，必须）
+ Context（上下文信息，可选）
+ Input Data（需要处理的数据，可选）
+ Output Indicator（要输出的类型或格式，可选）

一个面向复杂任务的prompt的一般都包含Instruction，Context，Input Data，Output Indicator。

所以面向大语言模型的开发应用过程就是如下公式：
**LMM(Instruction + Context + Input Data + Output Indicator)  = Output**

prompt engineering 就是写好这四块东西Instruction，Context，Input Data，Output Indicator
让模型的输出Output越准越好。

# text2sql  prompt
```
> prompt = """
>         现在你是一个数据分析师,SQL大神,请根据用户提供的表的信息，以及用户的需求，写出效率最高的SQL,
>         表信息如下：
>             表名：students;
>             字段：id,name,age,location
>         用户需求:统计一下姓名年龄大于23,姓名包含andy且在beijing,的的学生个数。
>         并且要求输出的SQL以#开头,以#结尾，样例如下：
>                 #SELECT * FROM table#
>                 #SELECT COUNT(*) FROM table#
>         注意不需要分析过程，直接给出SQL语句
>        """
> inputttext ="""<human>:
>      {}
> <aibot>:
> """.format(prompt)
```
  
  输出结果：  #SELECT COUNT(*) FROM students WHERE age > 23 AND name LIKE '%andy%' AND location = 'beijing'#
  ![image](https://github.com/wp931120/text2sql/assets/28627216/9e43aba9-fefc-4fc8-8537-8b7082424348)

# 大模型text2sql 微调教程
LLM大模型：https://huggingface.co/baichuan-inc/Baichuan-13B-Chat
训练数据：https://huggingface.co/datasets/Clinton/Text-to-sql-v1
```
数据格式如下：
"""Below are sql tables schemas paired with instruction that describes a task. Using valid SQLite, write a response that appropriately completes the request for the provided tables. ### Instruction: provide the number of patients whose diagnoses icd9 code is 60000? ### Input: CREATE TABLE procedures (\n    subject_id text,\n    hadm_id text,\n    icd9_code text,\n    short_title text,\n    long_title text\n)\n\nCREATE TABLE prescriptions (\n    subject_id text,\n    hadm_id text,\n    icustay_id text,\n    drug_type text,\n    drug text,\n    formulary_drug_cd text,\n    route text,\n    drug_dose text\n)\n\nCREATE TABLE demographic (\n    subject_id text,\n    hadm_id text,\n    name text,\n    marital_status text,\n    age text,\n    dob text,\n    gender text,\n    language text,\n    religion text,\n    admission_type text,\n    days_stay text,\n    insurance text,\n    ethnicity text,\n    expire_flag text,\n    admission_location text,\n    discharge_location text,\n    diagnosis text,\n    dod text,\n    dob_year text,\n    dod_year text,\n    admittime text,\n    dischtime text,\n    admityear text\n)\n\nCREATE TABLE lab (\n    subject_id text,\n    hadm_id text,\n    itemid text,\n    charttime text,\n    flag text,\n    value_unit text,\n    label text,\n    fluid text\n)\n\nCREATE TABLE diagnoses (\n    subject_id text,\n    hadm_id text,\n    icd9_code text,\n    short_title text,\n    long_title text\n) ### Response:"""
```

训练代码：text2sqlBaichuan13B.py
训练效果：
![image](https://github.com/wp931120/text2sql/assets/28627216/4aef1e11-36ab-4617-ac02-c74f52bbd222)
![image](https://github.com/wp931120/text2sql/assets/28627216/521910a9-9147-4bcf-9610-27a42b9ce7e8)

