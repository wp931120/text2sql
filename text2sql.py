import torch
from transformers import BitsAndBytesConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel

###加载子牙大模型并进行量化
model_id = "./Ziya-LLaMA-13B/"
# model_id = "ClueAI/ChatYuan-large-v2"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
    # load_in_8bit=True
)
device_map = {"": 1}
model_4bit = AutoModelForCausalLM.from_pretrained(model_id, device_map=device_map, quantization_config=bnb_config)
device = "cuda:1"
tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=False)

### 进行prompt工程,激发LLM的SQL能力，将LLM转换成SLQ boy
from transformers import GenerationConfig
import re


def text2sql(llm, tokenizer, tabledesc, sqltext):
    """
      tabledesc:        表名：students;
                        字段：id,name,age,location
      sqltext :  "统计一下姓名年龄大于23,姓名包含andy且在beijing,的的学生个数"
    """

    prompt = """
            现在你是一个数据分析师,SQL大神,请根据用户提供的表的信息，以及用户的需求，写出效率最高的SQL,
            并且要求输出的SQL以#开头,以#结尾，样例如下：
                #SELECT * FROM table#
                #SELECT COUNT(*) FROM table#
            表信息如下：
              {}
            用户需求:{}。
           """.format(tabledesc, sqltext)
    inputttext = """<human>:
         {}
    <aibot>:
    """.format(prompt)

    inputs = tokenizer(inputttext, return_tensors="pt").to(device)
    generation_config = GenerationConfig(
        temperature=0.1,
        top_p=0.85,
        do_sample=True,
        repetition_penalty=1,
        eos_token_id=2,
        bos_token_id=1,
        pad_token_id=0,
        max_new_tokens=1024,  # max_length=max_new_tokens+input_sequence

    )
    generate_ids = llm.generate(**inputs, generation_config=generation_config)
    output = tokenizer.decode(generate_ids[0][1:-1])[len(inputttext):]
    output = re.search("(?<=#)(.*?)(?=#)", output)
    return output.group()


### 使用text2sql方法
text2sql(model_4bit,
         tokenizer,
         """
         表名：students;
         字段：id,name,age,location
         """,
         "姓名年龄小于11，其姓名包含belle的学生有多少个"
         )