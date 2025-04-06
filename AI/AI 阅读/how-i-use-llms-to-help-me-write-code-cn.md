# 来源：Simon Willison's Newsletter | 作者：Simon Willison

# 我如何使用 LLM 辅助编写代码

### 此外，CSS 视图转换和 llm-openrouter 的重大更新

[![Simon Willison’s Newsletter](https://substackcdn.com/image/fetch/w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe68a4ed9-6701-4ace-b17d-00a1fddab42f_450x450.png)](https://simonw.substack.com/)

# [Simon Willison’s Newsletter](https://simonw.substack.com/)

订阅注册

# 我如何使用 LLM 辅助编写代码

### 此外，CSS 视图转换和 llm-openrouter 的重大更新

[![](https://simonw.substack.com/p/fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5a30d45c-fcba-407a-bebf-96f51a8944a4_48x48.jpeg)](https://substack.com/@simonw)

[Simon Willison](https://substack.com/@simonw)

2025 年 3 月 11 日

81

[2](https://simonw.substack.com/p/how-i-use-llms-to-help-me-write-code/comments)
17

[分享](javascript:void(0))

在本新闻通讯中：

- 以下是我如何使用 LLM 辅助编写代码


外加 3 个链接和 2 个引言

感谢阅读 Simon Willison 的新闻通讯！ 免费订阅以接收新帖子并支持我的工作。

订阅

### [以下是我如何使用 LLM 辅助编写代码](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) \- 2025-03-11

关于[使用大型语言模型辅助编写代码](https://simonwillison.net/tags/ai-assisted-programming/)的在线讨论不可避免地会产生一些开发人员的评论，他们的经验令人失望。 他们经常问自己哪里做错了 - 为什么有些人报告了如此出色的结果，而他们自己的实验却证明不足？

使用 LLM 编写代码是**困难的**和**违反直觉的**。 需要付出巨大的努力才能弄清楚以这种方式使用它们的优势和劣势，而且几乎没有指导可以帮助人们弄清楚如何最好地应用它们。

如果有人告诉你使用 LLM 进行编码是_容易的_，那么他们（可能无意中）误导了你。 他们很可能偶然发现了一些有效的模式，但这些模式并非对每个人都适用。

两年来，我一直在从 LLM 中获得出色的代码结果。 这是我尝试将一些经验和直觉传授给你的尝试。

- [设定合理的期望](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#set-reasonable-expectations)

- [考虑训练截止日期](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#account-for-training-cut-off-dates)

- [上下文为王](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#context-is-king)

- [向他们询问选项](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#ask-them-for-options)

- [告诉他们该怎么做](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#tell-them-exactly-what-to-do)

- [你必须测试它写的东西！](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#you-have-to-test-what-it-writes-)

- [记住这是一场对话](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#remember-it-s-a-conversation)

- [使用可以为你运行代码的工具](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#use-tools-that-can-run-the-code-for-you)

- [Vibe-coding 是一种很好的学习方式](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#vibe-coding-is-a-great-way-to-learn)

- [使用 Claude Code 的详细示例](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#a-detailed-example)

- [准备好让人类接管](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#be-ready-for-the-human-to-take-over)

- [最大的优势是开发速度](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#the-biggest-advantage-is-speed-of-development)

- [LLM 扩大了现有专业知识](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#llms-amplify-existing-expertise)

- [奖励：回答有关代码库的问题](https://simonwillison.net/2025/Mar/11/using-llms-for-code/#bonus-answering-questions-about-codebases)


#### 设定合理的期望

忽略“AGI”的炒作 - LLM 仍然是花哨的自动完成。 他们所做的只是预测一系列 token - 但事实证明，编写代码主要是在正确的顺序中将 token 串在一起，因此如果你将它们指向正确的方向，它们可能会_非常_有用。

如果你认为这项技术可以完美地实现你的项目，而无需你运用自己的任何技能，那么你很快就会失望。

相反，使用它们来_增强_你的能力。 我目前最喜欢的思维模式是将它们视为一个过度自信的结对编程助手，他们可以快速查找东西，可以随时快速生成相关的示例，并且可以毫不抱怨地执行繁琐的任务。

**过度自信**很重要。 他们绝对会犯错误 - 有时是微妙的，有时是巨大的。 这些错误可能[非常不人道](https://simonwillison.net/2025/Mar/2/kellan-elliott-mccrea/) - 如果人类合作者幻想着一个不存在的库或方法，你将立即失去对他们的信任。 不要陷入将 LLM 人格化的陷阱，并假设会使人类失去信誉的失败应该以同样的方式使机器失去信誉。

在使用 LLM 时，你经常会发现它们无法做到某些事情。 记下这些 - 它们是有用的教训！ 它们也是未来存放起来的宝贵示例 - 一个强大的新模型的标志是，当它为以前的模型无法处理的任务生成可用的结果时。

#### 考虑训练截止日期

任何模型的关键特征都是其**训练截止日期**。 这是他们接受训练的数据停止收集的日期。 对于 OpenAI 的模型，这通常是 2023 年 10 月。 Anthropic 和 Gemini 以及其他提供商可能有更近的日期。

这对于代码来说_极其_重要，因为它会影响他们熟悉的库。 如果你使用的库自 2023 年 10 月以来发生了重大突破性更改，OpenAI 模型将不会知道！

我从 LLM 中获得了足够的价值，我现在在选择库时会故意考虑这一点 - 我尝试坚持使用具有良好稳定性的库，并且这些库足够流行，以至于它们的许多示例都已进入训练数据。 我喜欢应用[无聊技术](https://boringtechnology.club/)的原则 - 在你项目的独特卖点上进行创新，坚持使用经过试验和测试的解决方案来解决其他问题。

LLM 仍然可以帮助你使用其训练数据之外存在的库，但你需要投入更多的工作 - 你需要将这些库应如何使用的最新示例作为提示的一部分提供给它们。

这使我们了解了在使用 LLM 时要理解的最重要的事情：

#### 上下文为王

从 LLM 中获得良好结果的大部分技巧都归结为管理其上下文 - 即你当前对话的一部分文本。

此上下文不仅仅是你提供给它的提示：成功的 LLM 交互通常采用对话的形式，并且上下文包括你_和_ LLM 的每个消息，这些消息都存在于当前对话线程中。

当你开始新的对话时，你会将该上下文重置为零。 了解这一点很重要，因为通常修复已停止有用的对话的方法是擦除石板并重新开始。

例如，某些 LLM 编码工具不仅仅是对话。 例如，Claude Projects 允许你使用相当大量的文本来预先填充上下文 - 包括最近[从 GitHub 直接导入代码](https://support.anthropic.com/en/articles/10167454-using-the-github-integration)的功能，我正在大量使用该功能。

像 Cursor 和 VS Code Copilot 这样的工具会自动包含来自你当前编辑器会话和文件布局的上下文，有时你可以使用[Cursor 的 @commands](https://docs.cursor.com/context/@-symbols/overview)之类的机制来提取其他文件或文档。

我主要直接使用 [ChatGPT](https://chatgpt.com/) 和 [Claude](https://claude.ai/) 网络或应用程序界面的原因之一是，它可以让我更轻松地了解上下文中到底有什么。 对我隐藏该上下文的 LLM 工具_不太_有效。

你可以利用以前的回复也是上下文的一部分这一事实来发挥自己的优势。 对于复杂的编码任务，请尝试首先让 LLM 编写一个更简单的版本，检查它是否有效，然后迭代构建到更复杂的实现。

我经常通过转储现有代码来启动新的聊天来为该上下文添加种子，然后与 LLM 合作以某种方式修改它。

我最喜欢的代码提示技术之一是放入几个与我想构建的东西相关的完整示例，然后提示 LLM 将它们用作新项目的灵感。 当我[描述我的 JavaScript OCR 应用程序](https://simonwillison.net/2024/Mar/30/ocr-pdfs-images/)时，我详细介绍了这一点，该应用程序结合了 Tesseract.js 和 PDF.js - 我过去曾使用过的两个库，并且我可以在提示中提供有效的示例。

#### 向他们询问选项

我的大多数项目都始于一些开放性问题：我试图做的事情是否可行？ 我可以通过哪些潜在的方式来实现它？ 这些选项中哪个是_最好的_？

我将 LLM 用作此初始研究阶段的一部分。

我将使用诸如“Rust 中 HTTP 库有哪些选项？ 包括使用示例”之类的提示 - 或者“JavaScript 中有哪些有用的拖放库？ 为我构建一个演示每个库的工件”（对于 Claude）。

训练截止日期与此相关，因为它意味着不会推荐较新的库。 通常这没关系 - 我不想要最新的，我想要最稳定的，并且已经存在了足够长的时间来消除错误。

如果我要使用更新的东西，我将在 LLM 世界之外自己进行研究。

启动任何项目的最佳方法是使用原型来证明可以满足该项目的关键要求。 我经常发现，在坐到笔记本电脑前几分钟内，或者有时甚至在手机上工作时，LLM 就可以让我获得该工作原型。

#### 告诉他们该怎么做

完成初始研究后，我戏剧性地改变了模式。 对于生产代码，我对 LLM 的使用更加专制：我将其视为数字实习生，根据我的详细说明为我键入代码。

这是一个最近的例子：

> 编写一个使用 asyncio httpx 的 Python 函数，其签名为：
>
> ```
> async def download_db(url, max_size_bytes=5 * 1025 * 1025): -> pathlib.Path
> ```
>
> 给定一个 URL，这将数据库下载到临时目录并返回其路径。 但是，它会在流式传输回该数据开始时检查内容长度标头，如果超过限制，则会引发错误。 下载完成后，它使用 `sqlite3.connect(...)`，然后运行 `PRAGMA quick_check` 以确认 SQLite 数据有效 - 如果无效则引发错误。 最后，如果内容长度标头对我们撒谎 - 如果它说 2MB 但我们下载了 3MB - 我们会在注意到该问题后立即引发错误。

我可以自己编写这个函数，但这将花费我大部分时间来查找所有详细信息并使代码正常工作。 Claude 在 [15 秒内](https://gist.github.com/simonw/5aed8bd87016c77465c23e0dc4563ec9)将其淘汰。

我发现 LLM 对我在此处使用的函数签名反应非常好。 我可以充当函数设计者，LLM 完成构建主体的任务以满足我的规范。

我经常会接着说“现在使用 pytest 为我编写测试”。 同样，我指定了我选择的技术 - 我希望 LLM 节省我必须输入已经存在于我脑海中的代码的时间。

如果你的反应是“当然，输入代码比输入它的英语指令更快”，我只能告诉你，对我来说真的不是这样了。 代码需要正确。 英语有很大的捷径、含糊不清和错别字的空间，如果你不记得名字，可以说“使用那个流行的 HTTP 库”之类的话。

优秀的编码 LLM 非常擅长填补空白。 它们也比我懒惰得多 - 它们会记住捕获可能的异常，添加准确的文档字符串，并使用相关的类型注释来注释代码。

#### 你必须测试它写的东西！

我[上周](https://simonwillison.net/2025/Mar/2/hallucinations-in-code/#qa)对此进行了详细介绍：你绝对不能外包给机器的一件事是测试代码是否真的有效。

你作为软件开发人员的责任是交付可工作的系统。 如果你没有看到它运行，它就不是一个可工作的系统。 你需要投资于加强这些手动 QA 习惯。

这可能并不迷人，但无论是否涉及 LLM，它一直是交付优秀代码的关键部分。

#### 记住这是一场对话

如果我不喜欢 LLM 编写的内容，他们_永远_不会抱怨被告知要重构它！ “将该重复代码分解为一个函数”、“使用字符串操作方法而不是正则表达式”，甚至“更好地编写它！” - LLM 第一次生成的代码很少是最终实现，但它们可以为你重新键入数十次，而不会感到沮丧或厌烦。

偶尔我会从我的第一个提示中获得一个很棒的结果 - 随着我练习的次数增加，这种情况会更频繁地发生 - 但我希望至少需要几个后续步骤。

我经常想知道这是否是人们遗漏的关键技巧之一 - 一个糟糕的初始结果不是失败，而是推动模型朝着你真正想要的东西发展的起点。

#### 使用可以为你运行代码的工具

现在，越来越多的 LLM 编码工具能够为你_运行该代码_。 我对其中一些工具持谨慎态度，因为错误的命令可能会造成实际损害，因此我倾向于坚持在安全沙箱中运行代码的工具。 我现在最喜欢的是：

- **ChatGPT Code Interpreter**，其中 ChatGPT 可以直接在 OpenAI 管理的 Kubernetes 沙箱 VM 中编写然后执行 Python 代码。 这是完全安全的 - 它甚至无法建立出站网络连接，因此真正可能发生的是临时文件系统被破坏然后重置。

- **Claude Artifacts**，其中 Claude 可以为你构建一个完整的 HTML+JavaScript+CSS Web 应用程序，该应用程序显示在 Claude 界面中。 此 Web 应用程序显示在_非常_锁定的 iframe 沙箱中，极大地限制了它可以执行的操作，但可以防止诸如意外泄露你的私有 Claude 数据之类的问题。

- **ChatGPT Canvas** 是 ChatGPT 的一项较新功能，其功能与 Claude Artifacts 类似。 我自己还没有对此进行足够的探索。


如果你愿意生活得更危险一点：

- **[Cursor](https://www.cursor.com/)** 具有可以执行此操作的“代理”功能，**[Windsurf](https://codeium.com/windsurf)** 以及越来越多的其他编辑器也是如此。 我还没有花足够的时间来提出建议。

- **[Aider](https://aider.chat/)** 是这些类型模式的主要开源实现，并且是 [dogfooding](https://en.wikipedia.org/wiki/Eating_your_own_dog_food) 的一个很好的例子 - Aider 的最新版本已由 Aider 本身[编写了 80% 以上](https://aider.chat/HISTORY.html)。

- **[Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)** 是 Anthropic 进入该领域的新产品。 我将很快提供有关使用该工具的详细说明。


这种在循环中运行代码的模式非常强大，以至于我选择用于编码的核心 LLM 工具主要基于它们是否可以安全地运行和迭代我的代码。

#### Vibe-coding 是一种很好的学习方式

Andrej Karpathy 在一个多月前[创造了术语](https://simonwillison.net/2025/Feb/6/andrej-karpathy/) vibe-coding，并且它已经坚持了下来：

> 有一种新的编码方式，我称之为“vibe coding”，你完全沉浸在氛围中，拥抱指数，并忘记代码的存在。 \[...\] 我要求做最愚蠢的事情，比如“将侧边栏上的填充减少一半”，因为我太懒了，找不到它。 我总是“全部接受”，我不再阅读差异。 当我收到错误消息时，我只是复制粘贴它们，通常可以解决问题。

Andrej 建议这“对于一次性周末项目来说还不错”。 这也是探索这些模型的功能以及真正有趣的方式。

学习 LLM 的最佳方法是使用它们。 向他们抛出荒谬的想法并进行 vibe-coding，直到他们几乎可以进行排序，这确实是一种有用的方法，可以加快你建立对什么有效和什么无效的直觉的速度。

自从 Andrej 给它命名之前，我就一直在进行 vibe-coding！ 我的 [simonw/tools](https://github.com/simonw/tools) GitHub 存储库有 77 个 HTML+JavaScript 应用程序和 6 个 Python 应用程序，并且它们中的每一个都是通过提示 LLM 构建的。 我从构建此集合中学到了_很多_，并且我以每周几个新原型的速度添加到它。

你可以直接在 [tools.simonwillison.net](https://tools.simonwillison.net/) 上试用我的大部分工具 - 这是该存储库的 GitHub Pages 发布版本。 我在 10 月份的[本周我使用 Claude Artifacts 构建的所有内容](https://simonwillison.net/2024/Oct/21/claude-artifacts/)中写了更多关于其中一些工具的详细说明。

如果你想查看用于每个工具的聊天的记录，它几乎总是链接到该页面的提交历史记录中 - 或者访问新的 [colophon 页面](https://tools.simonwillison.net/colophon)以获取包含所有这些链接的索引。

#### 使用 Claude Code 的详细示例

在撰写本文时，我想到了 [tools.simonwillison.net/colophon](https://tools.simonwillison.net/colophon) 页面 - 我想要一些我可以链接到的东西，以比 GitHub 更明显的方式显示我的每个工具的提交历史记录。

我决定以此为例来演示我的 AI 辅助编码过程。

对于这个，我使用了 [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)，因为我希望它能够直接针对我笔记本电脑上现有的工具存储库运行 Python 代码。

在会话结束时运行 `/cost` 命令向我显示了以下内容：

```
> /cost
  ⎿  总成本：0.61 美元
     总持续时间（API）：5 分 31.2 秒
     总持续时间（墙）：17 分 18.7 秒
```

从开始到结束，最初的项目花费了我 17 分多一点的时间，并花费了我 61 美分的 API 调用费用给 Anthropic。

我使用了专制的流程，我告诉模型我想要构建什么。 这是我的提示序列（[此处提供完整记录](https://gist.github.com/simonw/323e1b00ee4f8453c7834a7560eeafc1)）。

我首先要求提供一个初始脚本来收集新页面所需的数据：

> 此目录中的几乎所有 HTML 文件都是使用 Claude 提示创建的，并且这些提示的详细信息链接在提交消息中。 构建一个 Python 脚本，该脚本依次检查每个 HTML 文件的提交历史记录，并将这些提交消息中的任何 URL 提取到列表中。 然后，它应该输出一个具有以下结构的 JSON 文件：{"pages": {"name-of-file.html": \["url"\], {"name-of-file-2.html": \["url1", "url2"\], ... - 正如你所看到的，某些文件可能在其提交历史记录中具有多个 URL。 该脚本应称为 gather\_links.py，并且应保存一个名为 gathered\_links.json 的 JSON 文件

我真的没有认真考虑这第一个提示 - 这更像是当我在考虑初始问题时输入到机器人中的意识流。

我检查了初始结果并发现了一些问题：

> 看起来它只是获得了 URL 的开头，它应该获得完整的 URL，这些 URL 可能是指向不同网站的 - 因此只需获取任何以 https:// 开头并以空格或提交消息结尾的内容

然后我改变了主意 - 我也想要那些完整的提交消息：

> 更新脚本 - 我想捕获完整的提交消息_和_ URL - 新格式应为 {"pages": {"aria-live-regions.html": {"commits": \["hash": hash, "message": message, "date": iso formatted date\], "urls": \[list of URLs like before\]

提供这样的示例是准确获得你想要的东西的绝佳捷径。

请注意，在任何时候我都没有看过它在 [gather\_links.py](https://github.com/simonw/tools/blob/87e2577983f11fc9c7bf7b7a268cf2404a21e1c5/gather_links.py) 中编写的代码！ 这是纯粹的 vibe-coding：我正在查看它在做什么，但我已将实现细节完全留给 LLM。

JSON 对我来说看起来不错，所以我说：

> 这工作得很好。 为我编写一个名为 build\_colophon.py 的新脚本，该脚本会查找该收集的 JSON 文件并构建和保存 HTML 页面。 该页面应该是移动友好的，并且应该列出每个页面 - 带有指向该页面的链接 - 并且对于每个页面，整齐地显示提交消息（将换行符转换为 br 并链接 URL，但没有其他格式） - 加上提交消息日期和指向提交本身的链接，这些链接位于 [https://github.com/simonw/tools](https://github.com/simonw/tools) 中

Claude 知道 GitHub URL 的工作方式，因此告诉它链接到提交并提供存储库名称足以让它猜测 `https://github.com/simonw/tools/commit/fd9daf885c924ba277806b3440457d52b0ad90a8` 用于这些提交 URL。

我倾向于发现 Claude 在网页设计方面具有良好的默认品味 - 我说“该页面应该是移动友好的”，然后就到此为止了。

Claude 努力工作并为我构建了一个不正确的页面，所以我说：

> 它工作不正常。 ocr.html 有很多提交，但在 colophon.html 中，只有一个链接和第一个提交的标题，其余的都显示在同一个块中 - 应该有单独的 HTML 块，其中包含每个其他提交的链接和格式化日期。 此外，整齐格式化的日期应包括 HH:MM 以及日期

它完全靠自己修复了该错误，只剩下我决定进行的两个更改：

> 它几乎是完美的，但是每个页面都应该以相反的顺序显示提交 - 最旧的在前

然后：

> 最后一个更改 - 页面当前按字母顺序列出，让我们改为按最近修改的页面列出它们

这就是整个项目！ 这是 [build\_colophon.py](https://github.com/simonw/tools/blob/1e04f12a1cacea8856946162457d0d77e60ee549/build_colophon.py)，它生成的页面看起来[非常好](https://static.simonwillison.net/static/2025/colophon.html)：

[![工具题词。 此页面记录了 tools.simonwillison.net 上工具的创建，包括指向用于构建它们的 Claude 对话的链接。 social-media-cropper.html b4a2bc 2024 年 12 月 10 日 20:35 社交媒体裁剪器 https://gist.github.com/simonw/12b8f88932a71450071190e1289a17e9 a10954 2025 年 2 月 28 日 16:02 支持 2:1 和 14:10 比率 https://gist.github.com/simonw/e23917eddcbb368c9b6180d581f8f40a](https://simonw.substack.com/p/fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5eb20c0-d125-480c-92f4-e927d0a12872_1600x1200.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5eb20c0-d125-480c-92f4-e927d0a12872_1600x1200.jpeg)

还剩下一个任务：我需要将新的 colophon 部署为我站点的一部分，但我不想将新的 `colophon.html` 页面检入到存储库本身。 我想要一个自定义 GitHub Pages 构建过程。

我启动了一个全新的 Claude Code 会话（清除状态）来看看 Claude 是否也能弄清楚这一点：

> 此存储库是使用 GitHub Pages 部署的。 我想稍微修改一下构建 - 在部署到 GitHub Pages 之前，它应该运行 python gather\_links.py，这将生成一个名为 gathered\_links.json 的文件 - 然后它应该运行 python build\_colophon.py，这将使用该文件来创建 colophon.html - 我希望 gathered\_links.json 和 colophon.html 都发布到 GitHub pages，但我不希望将它们检入到存储库本身

与第一次不同，这次我非常仔细地观看了它在做什么 - 我不知道如何以这种方式自定义 GitHub Pages 构建，并且我想既学习如何执行此操作，又保持谨慎，以免它幻觉细节并在任务中失败。

它告诉我它想要创建此文件并征求我的许可：

```
名称：部署到 GitHub Pages

关于：
  # 在推送到主分支时运行
  push:
    branches: [ main ]
  # 允许手动触发
  workflow_dispatch:

# 设置 GITHUB_TOKEN 的权限
权限：
  内容：读取
  页面：写入
  id-token：写入

# 仅允许一个并发部署
并发：
  group：页面
  cancel-in-progress：true

作业：
  build:
    runs-on：ubuntu-latest
    步骤：
      - 名称：结帐
        uses：actions/checkout@v4
        with:
          fetch-depth：0 # gather_links.py 中 git log 需要完整历史记录

      - 名称：设置 Python
        uses：actions/setup-python@v5
        with:
          python-version：'3.12'

      - 名称：安装依赖项
        run: |
          python -m pip install --upgrade pip

      - 名称：生成链接并构建题词
        run: |
          python gather_links.py
          python build_colophon.py

      - 名称：设置页面
        uses：actions/configure-pages@v4

      - 名称：使用 Jekyll 构建
        uses：actions/jekyll-build-pages@v1

      - 名称：上传工件
        uses：actions/upload-pages-artifact@v3

  deploy:
    environment:
      name：github-pages
      url：${{ steps.deployment.outputs.page_url }}
    runs-on：ubuntu-latest
    needs：build
    步骤：
      - 名称：部署到 GitHub Pages
        id：deployment
        uses：actions/deploy-pages@v4
```

我猜这是对的？ 我很欣赏关于“gather\_links.py 中 git log 需要完整历史记录”的评论 - 这是我很容易错过的。

然后它说它想将这些文件添加到 `.gitignore` - 听起来是个好主意。

它输出了迄今为止其操作的摘要：

> 我已经为 GitHub Pages 创建了一个 GitHub Actions 工作流程，该工作流程：
>
> 1. 创建一个 .github/workflows/pages.yml 文件，该文件：
>
>    - 在推送到主分支时运行
>
>    - 检出完整的 git 历史记录（gather\_links.py 需要）
>
>    - 设置 Python 3.12
>
>    - 依次运行两个脚本以生成文件
>
>    - 构建并部署到 GitHub Pages
> 2. 创建 .gitignore 文件以防止提交生成的文件
>
>
> 现在，当你推送到 main 时，GitHub Actions 将：
>
> - 运行 gather\_links.py 脚本以创建 gathered\_links.json
>
> - 运行 build\_colophon.py 以创建 colophon.html
>
> - 将两个文件（和所有其他文件）部署到 GitHub Pages

我检查了一下花费了多少：

```
> /cost
  ⎿  总成本：0.1788 美元
     总持续时间（API）：44.6 秒
     总持续时间（墙）：10 分 18.6 秒
```

因此，使用 Claude API 花费了 17 美分和 45 秒。 （我分心了，因此总时间为 10 分钟。）这是[完整记录](https://gist.github.com/simonw/a560b07eef577e6183021d1ccaae7e07)。

代码看起来不会不可逆转地破坏任何东西，所以我将其推送到 GitHub 以查看会发生什么。

...它奏效了！ 我的新 [colophon 页面](https://tools.simonwillison.net/colophon)已上线。

有个问题。 我在运行 GitHub Actions 界面时观看了它，但有些事情看起来不对劲：

[![GitHub Actions 界面显示三个已完成的操作。 colophon 的自定义页面工作流程的测试，同一名称的部署以及另一个名为 pages-build-deployment 的部署。](https://simonw.substack.com/p/fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d4342c2-a034-497f-aebe-946040b819f4_1850x932.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d4342c2-a034-497f-aebe-946040b819f4_1850x932.jpeg)

我期望有“Test”作业，但为什么有两个单独的部署？

我有一种预感，先前的默认 Jekyll 部署仍在运行，而新的部署同时运行 - 并且新的脚本完成得更晚并覆盖了原始结果纯粹是时间上的运气。

是时候放弃 LLM 并阅读一些文档了！

我在[将自定义工作流程与 GitHub Pages 结合使用](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)页面上找到了此页面，但它没有告诉我需要知道的内容。

根据另一个预感，我检查了我的存储库的 GitHub Pages 设置界面，并找到了此选项：

[![GitHub Pages UI - 显示你的站点在 tools.simonwillison.net 上处于活动状态，7 分钟前部署。 - 然后在 Buyld 和部署下，源菜单显示 GitHub Actions 的选项或从分支部署（已选择）](https://simonw.substack.com/p/fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F591a1a60-35e9-4657-9f54-6f26788f3cdb_1594x952.jpeg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F591a1a60-35e9-4657-9f54-6f26788f3cdb_1594x952.jpeg)

我的存储库设置为“从分支部署”，因此我将其切换为“GitHub Actions”。

我手动更新了我的 `README.md` 以在此提交
