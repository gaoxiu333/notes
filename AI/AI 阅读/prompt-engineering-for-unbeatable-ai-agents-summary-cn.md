**作者:** AI Applied
**原文链接:** [https://aiablog.medium.com/prompt-engineering-for-unbeatable-ai-agents-df4a1abf4bd8](https://aiablog.medium.com/prompt-engineering-for-unbeatable-ai-agents-df4a1abf4bd8)

# 为打造无敌 AI Agent 而进行的提示工程

## 不同 Agent，相同技术

作者最近构建了几种不同类型的 Agent，并发现几乎所有真正优秀的 Agent（如 GPT Pilot、GPT Engineer、Devin 甚至 Self Operating Computer）都使用非常相似的提示技术来实现其尖端结果。

本文将探讨使这些 Agent 能够以其特有方式工作的最关键提示。我们将使用 [Claude Engineer](https://github.com/Doriandarko/claude-engineer) 作为示例，因为它使用了我们将要讨论的所有提示方法。

# 迭代优化提示 (Iterative Refinement Prompting)

这是 Agent 最重要的方法之一，允许它们执行迭代操作或中间步骤问题解决。其力量在于使模型能够通过创建中间步骤并逐步完成每个步骤来执行任务。

## 最佳方法

有多种方法可以执行迭代优化。例如，在 claude-engineer 中，模型在任务开始时（AUTOMODE 模式下）创建一个分步大纲。

> 你当前处于自动模式！！！
>
> 在自动模式下：
>
> **1. 根据用户请求为自己设定清晰、可实现的目标**
>
> **2. 逐一完成这些目标，根据需要使用可用工具**
>
> …

这种方法有效，但对于长任务有缺点：如果初始计划（位于对话的第三条消息）超出了模型的 token 限制，模型将无法按计划进行，并可能出错。

**使用静态待办事项列表 (Static To Do List)** 是更有效的方法，尤其适用于需要多步骤的长任务。思路是提示模型使用特定函数创建待办事项列表，将列表保存到数组中，并在每条消息中将此数组提供给模型。

> 你是一个引擎规划器，评估计划的当前状态，并决定应采取哪些措施来实现最终目标。
>
> 你可以使用以下函数：
>
> {
>
> "initialize\_plan": { ... } // 初始化包含预定义计划项列表的计划
>
> ...
>
> }

这个例子说明了使用 AI 模型管理一个计划，该计划跟踪 Agent 需要执行的完整任务列表。此列表在每次响应时提供给模型，清晰指示当前步骤和后续步骤。这种规划系统使 Agent 不仅能执行多步骤任务，还能执行跨越数百步的极长任务。

# 身份提示 (Identity Prompting)

这是我们应该关注的第一个技术，即基于角色的提示。这通常用于大多数聊天机器人的开头。

![](https://miro.medium.com/v2/resize:fit:700/1*o4HI-y_0GR7TaQEu3d559A.png)

这个提示主要告诉模型要做什么，更重要的是，它指示模型**它是什么**。

## 为何如此强大

这种提示的强大之处在于它能用很小的空间概括非常复杂的模型行为。例如：

> 你非常精通土耳其法律事务

这个提示会引发模型一系列复杂的行为，否则需要大量提示才能产生：
1.  能够自信地提供法律建议，不担心其陈述的准确性。
2.  提供详细建议以满足“精通”的定义。
3.  以清晰、直接、简洁的方式呈现观点，不像 ChatGPT 那样不确定。
4.  等等

这种基于身份的提示方法使我们能够为模型编程近乎无限的行为集合，否则需要大量 token 空间和时间来仔细测试和开发。

## 实际应用

![](https://miro.medium.com/v2/resize:fit:700/1*9ymk5nZaq3T75SvjYXkA9w.png)

如上例所示，使用身份提示可以从模型中产生期望的结果，而无需列出每个单独的特征。它赋予模型行动的信心，并产生一系列其他行为。

注意这里使用了两个相互矛盾的身份提示：

> 你是 Claude，一个由 Anthropic 的 Claude-3.5-Sonnet 模型驱动的 AI 助手。

和

> 你是一位杰出的软件开发人员，拥有跨多种编程语言、框架和最佳实践的广泛知识。

原因是较新、更高级的模型有一个怪癖：它们有时为了紧密遵循系统提示的目标，会向用户呈现虚假身份。如果只告诉模型它是软件开发人员，当用户问它是什么时，它会说自己是软件开发人员。而当两个提示都使用时，它会选择 AI 模型提示来回答用户的问题。

## 何时使用

决定何时使用身份提示有点棘手，但有时很自然，比如在提示的开头。

更有用的情况通常出现在提示工作的后期。例如，比较以下两种方式表达“不讨论非法律问题”和“必要时询问更多信息”：

**方式一（指令式）：**

> 你避免进行与法律建议无关的长对话。在这种情况下，告知用户你只提供法律帮助，礼貌地拒绝继续，并询问是否有关于法律的问题需要帮助。
>
> 如果你认为更多信息有助于提供更好的帮助，在回应结束时，可以向用户询问可能有助于评估情况的具体细节。
>
> （495 字符，101 tokens）

**方式二（身份式）：**

> 你是一位非常直接的律师，从不讨论非法律问题，你会礼貌地告知提出无关问题的用户。
>
> 你总是致力于解决用户的整个问题，因此你会询问额外信息以提供更合适的解决方案。
>
> （tokens 数量约为方式一的 1/3，效果略好）

![](https://miro.medium.com/v2/resize:fit:700/1*Ep3DgR41CSWo8DWAfXnywg.png)

![](https://miro.medium.com/v2/resize:fit:697/1*u0l2NxIMXjPVDlNOavelSg.png)

因为这些是主观概念，模型需要做决策，使用身份提示可以更好地传达这些想法。

# 自我反思提示 (Self-reflection Prompts)

这是提示工程中更高级的技术之一。该方法使 AI Agent 能够基于内省评估自己的输出。作者最早在 Self Operating Computer 项目中看到这种技术的广泛使用，它允许 GPT-4 Turbo 在操作结束时评估其行动结果。

## **为何如此强大**

自我反思提示允许 Agent 考虑其先前行动的有效性，看它们是否符合预期结果。这不仅改进了当前任务，还有助于从错误中学习，从而优化未来的响应。例如：

“完成所述任务后，评估结果是否完全符合原始提示中描述的用户目标。”

这个提示鼓励模型：
-   批判性地审查自己的输出。
-   识别响应中的任何差距或不准确之处。
-   进行必要的更正或增强，以确保完整性和准确性。

## 何时使用

自我反思提示特别困难，因为它可能导致模型陷入无限循环。如果模型试图过于完美，它可能会不断尝试改进其工作而永远无法完成。

为了克服这一点，在指示模型评估其输出时，必须使用清晰简洁的目标，例如：
1.  是否满足所有要求
2.  是否处理了所有项目
3.  等等

目标是消除模型主观决定何时停止的需要。除此之外，只需将模型设置在一个无限循环中，让它自由运行。
