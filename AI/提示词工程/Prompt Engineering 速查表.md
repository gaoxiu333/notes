### **一、提示工程基础**

TODO: 结合claude的excel表再来一次，填充一些重点

- **提示（Prompt）**：你提供给模型的输入文字
- **输出（Output）**：模型根据你的提示返回的响应
- **上下文（Context）**：影响输出质量的额外信息（例如角色设定、示例）

### **二、构建更好提示的技巧**

#### **明确具体**

- 错误示例：写一封邮件
- 正确示例：写一封 100 字以内、语气友善的销售邮件，推销 X 产品给 Y 群体

#### **加入角色**

- "你是位资深 UX 设计师，请评估以下界面并提出改进建议。"

#### **设定格式**

- "请以表格形式返回"
- "输出格式为 JSON，包括字段：标题、摘要、评分"

#### **引导输出结构**

- "请将回答分为三部分：1）问题重述；2）分析过程；3）结论"

#### **明确语言风格**

- "用简洁、轻松的语气写一个 LinkedIn 帖子"
- "用学术语言撰写一段论文引言"
- // 三岁的孩子一样

### **三、进阶策略**

#### **Few-shot 提示**

提供一到多个示例来引导模型风格与格式

```
输入：用户说"谢谢你"  
输出：系统回复"很高兴帮到您！"  
输入：用户说"请再详细一点"  
输出：
```

#### **Chain-of-Thought（思维链）提示**

鼓励模型分步推理

- "请逐步推理，最后再给出答案。"
- "请说明你是如何得出结论的。"

#### **自我反思（Self-critique）**

- "请评估你上面的回答是否存在逻辑问题，并修正。"

#### **提示迭代**

不断尝试多个变体，优化提示语：

- "将提示语改写成更简洁专业的版本"
- "这个提示语是否存在歧义？请重写"

### **四、常见用途模板**

| **类型**   | **示例提示语**                                         |
| ---------- | ------------------------------------------------------ |
| 头脑风暴   | "列出关于[主题]的 10 个创意点子"                       |
| 学术写作   | "用学术语气写一段关于[主题]的 300 字说明"              |
| 文本总结   | "请将以下文字压缩为 100 字以内的摘要"                  |
| 代码生成   | "用 Python 写一个读取 CSV 文件并统计平均值的脚本"      |
| 翻译       | "将以下内容从英文翻译为繁体中文"                       |
| 数据格式化 | "将以下信息整理成 JSON 格式，字段包括标题、作者、时间" |
| 风格改写   | "将这段话改写成更适合社交媒体的语气"                   |

### **五、常用框架技巧**

#### **AIDA 框架（用于营销）**

- Attention：吸引注意
- Interest：激起兴趣
- Desire：引发欲望
- Action：促使行动

#### **PAS 框架**

- Problem：提出问题
- Agitate：激化问题
- Solution：给出解决方案

### **六、工具 & 资源推荐（英文）**

- [Prompt Engineering Guide](https://www.promptingguide.ai/introduction/basics)
- [LangChain](https://python.langchain.com/docs/use_cases/question_answering/)
- [LlamaIndex](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html)
- [Awesome Prompts](https://github.com/f/awesome-chatgpt-prompts)
- [向量数据库列表](https://www.datacamp.com/blog/the-top-5-vector-databases)

### **参考资源**
-  [Anthropic 创建测试用例](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool#creating-test-cases) - 更好的例子，让AI生成例子
