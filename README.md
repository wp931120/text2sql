# 大模型prompt engineering 教程
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
prompt = """
        现在你是一个数据分析师,SQL大神,请根据用户提供的表的信息，以及用户的需求，写出效率最高的SQL,
        表信息如下：
            表名：students;
            字段：id,name,age,location
        用户需求:统计一下姓名年龄大于23,姓名包含andy且在beijing,的的学生个数。
        并且要求输出的SQL以#开头,以#结尾，样例如下：
                #SELECT * FROM table#
                #SELECT COUNT(*) FROM table#
        注意不需要分析过程，直接给出SQL语句
       """
inputttext ="""<human>:
     {}
<aibot>:
""".format(prompt)
  
  最终结果：
  ![image](https://github.com/wp931120/text2sql/assets/28627216/4b8395c7-93f9-4b85-b6cd-06b80ae9187e)
