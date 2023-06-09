# text2sql 大模型prompt engineering 教程
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
