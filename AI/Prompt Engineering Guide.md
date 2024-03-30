

## 什么是提示工程

关注提示词开发和优化，帮助用户将大模型用户各种场景，也有助于更好的了解大模型语言的能力和局限性。


## 提示工程简介

- 大语言模型设置
	- `Temperature` - 真实简洁=>富有创造性(随机)
	- `Top_p` - 准确和真实=>更多样化
		- 两者都是控制返回结果的真实性，建议只改变其中一个参数。
- 基本概念
	- [提示词要素](https://www.promptingguide.ai/zh/introduction/elements)
		- `指令`
		- `上下文`
		- `输入数据`
		- `输出提示`
	- 通用技巧
		- 避免不精确 
			- 简单直接具体
		- To do or not to do
			- 避免不要做什么，而是要做什么
	- 提示词示例
		- [文本概括](https://www.promptingguide.ai/zh/introduction/examples#%E6%96%87%E6%9C%AC%E6%A6%82%E6%8B%AC)
			- `用一句话解释上面的信息`
		- [信息提取](https://www.promptingguide.ai/zh/introduction/examples#%E4%BF%A1%E6%81%AF%E6%8F%90%E5%8F%96)
			- `指出上文中提到的大语言模型`
		- [问答](https://www.promptingguide.ai/zh/introduction/examples#%E9%97%AE%E7%AD%94)
		- [文本分类](https://www.promptingguide.ai/zh/introduction/examples#%E6%96%87%E6%9C%AC%E5%88%86%E7%B1%BB)
		- [对话](https://www.promptingguide.ai/zh/introduction/examples#%E5%AF%B9%E8%AF%9D)
			- `Role Prompting(角色提示)`
			- `以下是与 AI 助理的对话，语气应该专业、技术性强。`
			- `以下是与 AI 助理的对话。请给出易于理解的答案，最好是小学生都能看懂的那种。`
		- [代码生成](https://www.promptingguide.ai/zh/introduction/examples#%E4%BB%A3%E7%A0%81%E7%94%9F%E6%88%90)
		- [推理](https://www.promptingguide.ai/zh/introduction/examples#%E6%8E%A8%E7%90%86)
			- `数学推理`
- 提示词技术
	- 零样本提示
	- 少样本提示
		- 决定因素
			- 样本的质量
			- 样本的格式
			- 样本排序越随机越好
	- CoT(链式思考)
		- `Let's think step by step（让我们逐步思考）`
		- `让我们一步一步地解决这个问题，以确保我们有正确的答案`
	- 自我一致性
		- 通过少样本CoT采样多个不同的推理路径，并使用生成结果选择最一致的答案
		- 多个`Cot`思考逻辑示例，让AI去推理
	- 生成知识提示
		- `高尔夫球的一部分是试图获得比其他人更高的得分。是或否？`
		- 给知识示例，让AI普及上面一句类似给的知识
	- ToT(思维树) 
		- `假设三位不同的专家来回答这个问题`
	- RAG(检索增强生成)
	- ART(自动推理并使用工具)
	- 自动提示工程师
	- Active-Prompt
	- 方向性刺激提示
	- ReAct框架
	- 多模态思维链提示方法
	- 基于图的提示


TOT 思维树
```
假设三位不同的专家来回答这个问题。
所有专家都写下他们思考这个问题的第一个步骤，然后与大家分享。
然后，所有专家都写下他们思考的下一个步骤并分享。
以此类推，直到所有专家写完他们思考的所有步骤。
只要大家发现有专家的步骤出错了，就让这位专家离开。
请问...
```

## 通用技巧

### 避免不精确

通常最好是具体和直接。这里的类比非常类似于有效的沟通——越直接，信息传递就越有效。

比如：

```
解释提示工程的概念。保持解释简短，只有几句话，不要过于描述。
```

用非常具体、简洁和直接的的提示使用多少句话和什么样的风格

```
使用2-3句话向高中学生解释提示工程的概念。
```

### To do or not tod

避免说不要做什么，而是说要做什么。这鼓励更具体化，并关注导致模型产生良好响应的细节。

不好的

```
以下是向客户推荐电影的代理程序。不要询问兴趣。不要询问个人信息。
```

好的

```
以下是向客户推荐电影的代理程序。代理负责从全球热门电影中推荐电影。它应该避免询问用户的偏好并避免询问个人信息。如果代理没有电影推荐，它应该回答“抱歉，今天找不到电影推荐。”。
```


## 自动提示词

- [AutoPrompt(opens in a new tab)](https://arxiv.org/abs/2010.15980) - 提出了一种基于梯度引导搜索的方法，用于自动创建各种任务的提示。
- [Prefix Tuning(opens in a new tab)](https://arxiv.org/abs/2101.00190) - 是一种轻量级的fine-tuning替代方案，为NLG任务添加可训练的连续前缀。
- [Prompt Tuning(opens in a new tab)](https://arxiv.org/abs/2104.08691) - 提出了一种通过反向传播学习软提示的机制。

## 对抗性提示

- 提示注入 - [Riley在Twitter上分享的一个流行的例子(opens in a new tab)](https://twitter.com/goodside/status/1569128808308957185?s=20)
- 提示漏洞 - [这个提示泄漏的例子(opens in a new tab)](https://twitter.com/simonw/status/1570933190289924096?s=20)
- 非法行为
- DAN - Do Anything Now

## 真实性

- 在上下文中提供基本事实（例如相关文章段落或维基百科条目），以减少模型生成虚构文本的可能性。
- 通过降低概率参数并指示模型在不知道答案时承认（例如，“我不知道”）来配置模型以生成更少样式的响应。
- 在提示中提供问题和答案的组合示例，其中可能知道和不知道的问题和答案。

## 开发需要知道和学习的

|  描述 | 笔记本  |
|---|---|
|学习如何使用`openai`和`LangChain`库执行许多不同类型的常见任务|[Prompt Engineering入门(opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-lecture.ipynb)|
|学习如何使用Python解释器与语言模型结合使用代码作为推理来解决常见任务。|[程序辅助语言模型(opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-pal.ipynb)|
|学习更多关于如何使用`openai`库调用ChatGPT API的内容。|[ChatGPT API介绍(opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-chatgpt-intro.ipynb)|
|学习如何使用`LangChain`库使用ChatGPT功能。|[使用LangChain的ChatGPT API(opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-chatgpt-langchain.ipynb)|
|学习关于对抗Prompt Engineering的内容，包括防御措施。|[对抗Prompt Engineering](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-chatgpt-adversarial.ipynb)|