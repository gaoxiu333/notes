**作者:** Max Woolf (@minimaxir)
**原文链接:** [https://minimaxir.com/2025/01/write-better-code/](https://minimaxir.com/2025/01/write-better-code/)

---

2023 年 11 月，在 OpenAI [添加了](https://openai.com/index/dall-e-3-is-now-available-in-chatgpt-plus-and-enterprise/) ChatGPT 在其网页界面内通过 DALL-E 3 生成图像的功能后，出现了一个[短暂的 meme](https://lifehacker.com/tech/chat-gpt-make-it-more-ai-images-trend)，用户给 LLM 一个基础图像，然后不断要求模型“让它更 X”，其中 X 可以是任何东西。

![一个普通人每次都变得更“兄弟”。来源：Reddit 用户 /u/Jojop0tato。](https://minimaxir.com/2025/01/write-better-code/bro_hu1964157573076261475.webp)

一个普通人每次都变得更“兄弟”。[来源：Reddit 用户 /u/Jojop0tato。](https://www.reddit.com/r/ChatGPT/comments/18ukiz2/a_regular_guy_becomes_more_bro_every_time/)

![要求 ChatGPT 让圣诞老人越来越严肃。来源：Reddit 用户 /u/hessihan。](https://minimaxir.com/2025/01/write-better-code/santa_hu13671242447035136691.webp)

要求 ChatGPT 让圣诞老人越来越严肃。[来源：Reddit 用户 /u/hessihan。](https://www.reddit.com/r/ChatGPT/comments/1887z49/asked_chatgpt_to_make_santa_claus_more_and_more/)

这个趋势很快就消失了，因为所有这些图像都非常相似且乏味，除了一个无法解释的趋势：无论起始图像和提示是什么，所有示例最终都会趋同于某种宇宙级的东西。尽管这个趋势在“AI 垃圾”（AI slop）这个术语被编纂之前就是[AI 垃圾](https://en.wikipedia.org/wiki/AI_slop)，但从学术角度来看，这样一个毫无意义且模糊的提示对最终图像产生了*某种*适当的影响，并且这种变化对用户来说是显而易见的，这仍然很有趣。

如果我们尝试用类似的技术处理代码会发生什么？LLM 生成的代码不太可能是垃圾（尽管[并非不可能](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/)），因为它遵循严格的规则，而且与图像等创意输出不同，代码质量可以更客观地衡量。

如果仅仅通过迭代提示，例如要求 LLM “让代码更好”——即使这很傻——就能真正改进代码，那将是生产力的巨大提升。如果是这样，那么过度迭代代码会发生什么？代码变得“宇宙级”的等价物是什么？只有一种方法可以找出答案！

## 与 LLM 随意编码 [\#](https://minimaxir.com/2025/01/write-better-code/#casually-coding-with-an-llm)

尽管早在 ChatGPT 出现之前我就研究和开发围绕 LLM 的工具，但我一直不太喜欢使用像 [GitHub Copilot](https://github.com/features/copilot) 这样的 LLM 代码助手来辅助编码。在“哦，LLM 自动完成了我的代码，真棒”/“我应该问 LLM 什么问题”和“LLM 生成的代码实际上是*正确*的，而不是[幻觉](https://en.wikipedia.org/wiki/Hallucination_%28artificial_intelligence%29)出正确的代码”之间不断的思维上下文切换，产生了足够多的干扰，以至于使用 AI 带来的任何生产力提升充其量只是净中性。这还不考虑使用这些 LLM 的昂贵成本。

[Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) 让我重新思考了这个问题。由于 [Anthropic](https://www.anthropic.com/) 在其训练中使用的任何秘密武器，最新版本的 Claude 3.5 Sonnet (`claude-3-5-sonnet-20241022`) 对所有类型的提示，尤其是编码提示，都具有*令人难以置信*的遵循度。[编码](https://www.vellum.ai/blog/llm-benchmarks-overview-limits-and-model-comparison) [基准测试](https://aider.chat/docs/leaderboards/)证实，在 Claude 3.5 Sonnet 和 GPT-4o 之间的测试中，Claude 获胜，而且根据我的经验，在各种技术和创意任务中也是如此。

### 初始请求 [\#](https://minimaxir.com/2025/01/write-better-code/#initial-ask)

在这个实验中，我们将给 Claude 3.5 Sonnet 一个面试风格的 Python 编码提示：一个既简单又可以由初级软件工程师实现，但又可以进行大量优化的提示。这个简单、随意的提示代表了典型软件工程师使用 LLM 的方式。此外，测试提示必须是完全原创的，不能取自像 [LeetCode](https://leetcode.com/) 或 [HackerRank](https://www.hackerrank.com/) 这样的编码测试，因为 LLM 很可能也接受过这些训练，并可能通过背诵记忆的答案来作弊。

> 基于这种随意提示的完整、未经编辑的对话线程[可在 GitHub 上找到](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md)。

因此，这是我自己编写的测试提示：

```txt
编写 Python 代码解决此问题：

给定一个包含 100 万个介于 1 到 100,000 之间的随机整数的列表，找出数字之和为 30 的最小和最大数字之间的差值。
```

将此作为用户提示提供给 Claude API 并设置 `temperature=0` 以获得最佳/最确定的答案 [1](https://minimaxir.com/2025/01/write-better-code/#fn:1)，得到以下实现：

```python
import random

def digit_sum(n):
    """计算一个数的各位数字之和"""
    return sum(int(digit) for digit in str(n))

def find_difference():
    # 生成包含 100 万个随机整数的列表
    numbers = [random.randint(1, 100000) for _ in range(1000000)]

    # 初始化数字和为 30 的最小和最大数字的变量
    min_num = float('inf')  # 初始化为正无穷大
    max_num = float('-inf')  # 初始化为负无穷大

    # 查找数字和为 30 的数字
    for num in numbers:
        if digit_sum(num) == 30:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

    # 检查是否找到了任何数字和为 30 的数字
    if min_num == float('inf') or max_num == float('-inf'):
        return "未找到数字和为 30 的数字"

    return max_num - min_num
```

[这个实现](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md#assistant-initial-ask)是正确的，并且与大多数初级 Python 程序员会编写的代码一致，还额外处理了没有符合条件的数字的情况。对于列表中的每个数字，检查其各位数字之和是否为 30：如果是，则检查它是否大于最近看到的最大数字或小于最近看到的最小数字，并相应地更新这些变量。搜索完列表后，返回差值。

但我相信许多阅读该实现的程序员都被[技术难题吸引](https://xkcd.com/356/)了，并且正在考虑优化。一个例子是 `digit_sum()` 函数：尽管该实现是一个有趣的 Pythonic 单行代码，但 `str` 和 `int` 之间的类型转换会导致大量不必要的开销。

在我的 M3 Pro Macbook Pro 上，这段代码平均需要 **657 毫秒** 运行。我们将使用这个性能作为基准，来比较未来的实现，看看它们的基准测试结果如何。（剧透：它们*都*更快）

### 迭代 #1 [\#](https://minimaxir.com/2025/01/write-better-code/#iteration-1)

现在我们可以要求 Claude 改进代码，方法是将当前答案及其之前的所有内容作为对话提示的一部分。因此，我们添加迭代提示：

```txt
编写更好的代码
```

什么，你以为这篇博文的标题是个玩笑？我*从不*开玩笑。

Claude [现在输出](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md#assistant-iteration-1)了修改后的代码，或者如它所说，“带有几项改进的优化版本代码”。它没有将所有代码放在函数中，而是决定将其重构为一个 Python `class`，并使其更加面向对象：

```python
class DigitSumFinder:
    def __init__(self, target_sum: int = 30,
                 range_start: int = 1,
                 range_end: int = 100_000,
                 count: int = 1_000_000):
        self.target_sum = target_sum
        self.range_start = range_start
        self.range_end = range_end
        self.count = count

        # 预先计算所有可能数字的数字和
        self.digit_sums = self._precompute_digit_sums()

    def _precompute_digit_sums(self) -> array:
        """预先计算范围内所有可能数字的数字和。"""
        digit_sums = array('B', [0] * (self.range_end + 1))
        for num in range(self.range_start, self.range_end + 1):
            total = 0
            n = num
            while n:
                total += n % 10
                n //= 10
            digit_sums[num] = total
        return digit_sums

    def find_difference(self) -> Tuple[int, Optional[int], Optional[int]]:
        """
        查找具有目标数字和的最大和最小数字之间的差值。
        返回: (差值, 最小数字, 最大数字)
        """
        min_num = float('inf')
        max_num = float('-inf')
        count_found = 0

        # 生成并处理随机数
        for _ in range(self.count):
            num = random.randint(self.range_start, self.range_end)
            if self.digit_sums[num] == self.target_sum:
                count_found += 1
                if num < min_num:
                    min_num = num
                if num > max_num:
                    max_num = num

        if count_found == 0:
            return 0, None, None

        return max_num - min_num, min_num, max_num
```

在这里，代码进行了两个聪明的算法改进：

-   计算数字和时，它使用整数运算，避免了之前提到的类型转换的需要。
-   它预先计算了所有可能的数字和，并将它们存储在一个字节数组（有点不寻常，而不是列表）中以供查找，这意味着当一百万个数字的列表中存在重复项时，不需要重新计算数字和。由于此数组作为类的字段存储，因此在搜索新的随机数列表时无需重新计算。

这些优化使代码相对于初始实现速度提高了 **2.7 倍**。

### 迭代 #2 [\#](https://minimaxir.com/2025/01/write-better-code/#iteration-2)

在又一次 `编写更好的代码` 之后，Claude [发现了](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md#assistant-iteration-2)更明显的优化（为便于阅读已截断）：

```python
class DigitSumAnalyzer:
    """根据数字和分析数字。"""

    def __init__(self, number_range: NumberRange):
        self.number_range = number_range
        self._digit_sums = self._precompute_digit_sums()

    def _precompute_digit_sums(self) -> array:
        """使用向量化操作预先计算所有可能数字的数字和。"""
        digits = np.arange(self.number_range.end + 1)
        digit_sums = np.zeros(self.number_range.end + 1, dtype=np.uint8)

        while digits.any():
            digit_sums += digits % 10
            digits //= 10

        return array('B', digit_sums)

    def _process_chunk(self, chunk_size: int) -> Iterator[int]:
        """处理一批随机数。"""
        numbers = np.random.randint(
            self.number_range.start,
            self.number_range.end + 1,
            chunk_size,
            dtype=np.int32
        )
        mask = np.frombuffer(self._digit_sums, dtype=np.uint8)[numbers] == self.number_range.target_sum
        yield from numbers[mask]

    def analyze(self, chunk_size: int = 100_000, num_processes: int = None) -> Result:
        """
        分析数字以查找具有目标数字和的最小/最大值。

        参数:
            chunk_size: 一次处理的块大小
            num_processes: 使用的进程数（None 表示 CPU 核心数）
        """
        start_time = time.perf_counter()
        min_num = float('inf')
        max_num = float('-inf')
        numbers_found = 0

        num_chunks = (self.number_range.count + chunk_size - 1) // chunk_size

        with ProcessPoolExecutor(max_workers=num_processes) as executor:
            futures = [\
                executor.submit(self._process_chunk,\
                              min(chunk_size, self.number_range.count - i * chunk_size))\
                for i in range(num_chunks)\
            ]

            for future in tqdm(futures, desc="处理块"):
                for num in future.result():
                    numbers_found += 1
                    min_num = min(min_num, num)
                    max_num = max(max_num, num)

        execution_time = time.perf_counter() - start_time

        if numbers_found == 0:
            return Result(None, None, 0, execution_time, 0)

        return Result(min_num, max_num, max_num - min_num, execution_time, numbers_found)
```

Claude 现在添加了另外两个优化，最终意识到这个编码问题是一个[易并行](https://en.wikipedia.org/wiki/Embarrassingly_parallel)问题：

-   通过 Python 的 [concurrent-futures](https://docs.python.org/3/library/concurrent.futures.html) 包实现多线程，将大列表分成可以独立处理的块。
-   向量化的 numpy 操作，这比基础 Python 操作*快得多*。特别值得一提的是 `_precompute_digit_sums()` 函数，它实现了计算数字和的向量化实现。条件 `while digits.any():` 是天才般的代码，但它确实能正确工作。

然而，这种特定的并行化实现存在一个问题：它会生成子进程，这会导致*许多*烦人的问题，包括无法直接内联运行它，并且它[必须通过](https://stackoverflow.com/questions/15900366/all-example-concurrent-futures-code-is-failing-with-brokenprocesspool) `main()` 保护来调用，这极大地限制了它的实用性。但即使作为单独的脚本运行，由于使用了 `yield from numbers[mask]`（该生成器完全没有必要，`return numbers[mask]` 就足够了），它也会打印 `Error: cannot pickle 'generator' object` 错误。代码还混合了 numpy 数组的 `dtype`，导致错误：将它们全部设置为 `np.int32` 可以解决问题。

进行这些修复后，代码现在比基础实现快 **5.1 倍**。

### 迭代 #3 [\#](https://minimaxir.com/2025/01/write-better-code/#iteration-3)

又一次 `编写更好的代码`，Claude [返回了一个实现](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md#assistant-iteration-3)，声称是“使用先进技术和现代 Python 特性的更复杂和优化的版本”，但实际代码没有显示出显著的算法改进，实际上在数字和计算方面通过恢复到类型转换方法而有所退步。如果说有什么不同的话，那就是代码库变得更加臃肿了，比如添加了一个用于执行差值计算的类：

```python
@dataclass(frozen=True, slots=True)
class SearchResult:
    """数字搜索的结果。"""
    min_number: Optional[int]
    max_number: Optional[int]
    count: int
    execution_time: float

    @property
    def difference(self) -> Optional[int]:
        """计算最大和最小数字之间的差值。"""
        if self.min_number is None or self.max_number is None:
            return None
        return self.max_number - self.min_number
```

这次，代码无需任何修复即可运行。然而，性能比之前的实现略有下降，现在比基础实现快 **4.1 倍**。

### 迭代 #4 [\#](https://minimaxir.com/2025/01/write-better-code/#iteration-4)

这种迭代提示似乎正在达到收益递减的阶段。在又一次 `编写更好的代码` 之后，Claude [提供了一个实现](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_casual_use.md#assistant-iteration-4)，带有“尖端优化和企业级功能”。等等，企业级功能？！

最终的代码太长，无法包含在这篇博文中，但它确实创造了另外两个优化：它现在使用了 [numba](https://numba.pydata.org/) Python 库，该库可以调用 JIT 编译器，直接为 CPU 优化代码。在这种情况下，它只需一个装饰器就可以超快速地预计算数字和：

```python
@jit(nopython=True, parallel=True)
def calculate_digit_sums(numbers: ArrayInt) -> ArrayInt:
    """使用 Numba 计算数字和。"""
    result = np.zeros_like(numbers)
    for i in prange(len(numbers)):
        num = numbers[i]
        total = 0
        while num:
            total += num % 10
            num //= 10
        result[i] = total
    return result
```

完整的类还使用了 Python 的 [asyncio](https://docs.python.org/3/library/asyncio.html) 进行并行化，这比子进程方法更规范地用于调度任务。它也更适合现有的内联代码和像 [Jupyter Notebooks](https://jupyter.org/) 这样的 [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)。

作为其“企业级”推动的一部分，它还添加了：

-   使用 [Prometheus](https://prometheus.io/) 进行结构化指标记录。
-   一个信号处理程序，以便在强制终止时可以优雅地拆除代码。
-   使用 [rich](https://github.com/Textualize/rich) 表格显示基准测试结果。

![不过它确实很漂亮！](https://minimaxir.com/2025/01/write-better-code/rich.png)

不过它确实很漂亮！

对于 AI 生成的代码来说，“变得宇宙级”似乎就是通过过度工程化使其企业化，这完全说得通。尽管如此，代码无需任何错误即可按原样运行。async 和 numba 都是 Python 中并行化的方法，所以它们可能是多余的并导致开销。然而，在基准测试后，该算法*极其*快速，每次运行大约 6 毫秒，即 **100 倍** 的加速。我关于这种提示正在达到收益递减的假设非常站不住脚。也许 numba 一直是秘密武器？

总的来说，这种迭代提示以迭代方式改进代码的方式存在一些注意事项：代码确实变得更好了，但事后看来，“更好”这个词太开放了。我想要的只是算法上的改进，而不是一个完整的 SaaS。让我们从头再试一次，这次方向更明确。

## 为获得更好的代码而进行 LLM 提示工程 [\#](https://minimaxir.com/2025/01/write-better-code/#prompt-engineering-llms-for-even-more-better-code)

现在是 2025 年，仍然需要对 LLM 进行提示工程才能获得最佳结果。如果说有什么不同的话，那就是对 LLM 进行提示工程*甚至更加重要*：下一个 token 预测模型被训练来最大化大量输入批次中下一个 token 的预测概率，因此它们优化的是**平均**输入和输出。随着 LLM 的急剧改进，生成的输出变得更加平均化，因为这就是它们被训练来做的事情：所有 LLM 都偏向于平均值。尽管这既违反直觉又无趣，但少量指导，明确告诉 LLM 你想要什么，甚至给出一些你想要的例子，将客观地改进 LLM 的输出，其效果超过了构建这些提示所需的努力。Claude 3.5 Sonnet 由于其强大的提示遵循能力，即使只有一点点提示工程也能显著受益。

让我们重新进行代码优化实验，这次使用激进的提示工程，使我寻找的结果极其明确，没有任何歧义的余地。是的，对 LLM 冷淡和“机器人化”会使它们表现更好，管他[罗科的蛇怪](https://en.wikipedia.org/wiki/Roko%27s_basilisk)呢。

### 初始请求 [\#](https://minimaxir.com/2025/01/write-better-code/#initial-ask-1)

这次我们将使用系统提示，这只能通过 API 实现。系统提示列出了 LLM 必须遵循的“规则”。由于我想要更优化的代码，我们将在规则中定义它，并提供详细的示例：

```txt
你编写的所有代码都必须完全优化。

“完全优化”包括：
- 最大化内存和运行时的算法大 O 效率
- 在适当的地方使用并行化和向量化
- 遵循代码语言的正确风格约定（例如最大化代码重用（DRY））
- 除了解决用户提供的问题绝对必要的代码外，没有多余的代码（即没有技术债务）

如果代码没有完全优化，你将被罚款 100 美元。
```

关于最后一行：在系统提示中向 LLM 提供正面/负面激励在现在已不常见，并且[我自己的研究](https://minimaxir.com/2024/02/chatgpt-tips-analysis/)表明，它是否具有积极影响尚不清楚，但这笔罚款在迭代提示中将变得更加相关。

初始用户提示也增加了一行：

```txt
编写 Python 代码解决此问题：

给定一个包含 100 万个介于 1 到 100,000 之间的随机整数的列表，找出数字之和为 30 的最小和最大数字之间的差值。

在编写代码之前，规划出所有必要的优化。
```

“规划”是一个长期使用的技巧，用于帮助在第一遍对齐 LLM 输出——这是“[让我们一步一步思考](https://arxiv.org/abs/2205.11916)”的现代实现。一些 LLM 会忽略它，但 Claude 3.5 Sonnet 总是遵守。

> 基于这种提示工程策略的完整、未经编辑的对话线程[可在 GitHub 上找到](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md)。

将系统提示和此用户提示发送给 Claude，[响应](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md#assistant-initial-ask)以此开始：

```txt
让我先规划一下优化：

1. 算法优化：
- 我们只需要跟踪数字和为 30 的最小和最大数字，不需要存储所有这些数字
- 我们可以在读取数字时计算数字和，无需转换为字符串
- 需要单次遍历列表 (O(n))

2. 内存优化：
- 只需要存储 2 个变量（最小和最大），不需要完整的过滤列表
- 不需要额外的数据结构

3. 性能优化：
- 使用 numba 的 @jit 装饰器以加快计算速度
- 创建一个使用模运算而不是字符串转换的快速数字和函数
- 使用 numpy 生成随机数（比 random.randint 更快）
```

这很有希望：Claude 立即意识到它应该从 numpy 和 numba 开始，并使用整数运算来计算数字和。初始实现：

```python
@jit(nopython=True)
def digit_sum(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

@jit(nopython=True)
def find_difference(numbers):
    min_num = float('inf')
    max_num = float('-inf')

    for num in numbers:
        sum_digits = digit_sum(num)
        if sum_digits == 30:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

    return max_num - min_num if max_num != float('-inf') else 0
```

这比随意提示的初始实现更简洁，尤其是在没有不必要注释的情况下。仍然有改进的空间，特别是这个实现没有在 `jit` 装饰器中设置 `parallel=True`。

这次轻微的提示工程产生的代码平均运行时间为 11.2 毫秒，比朴素实现快 **59 倍**。哇！

### 迭代 #1 [\#](https://minimaxir.com/2025/01/write-better-code/#iteration-1-1)

我们现在可以用比“编写更好的代码”更详细的提示来要求 Claude 迭代代码：

```txt
你的代码没有完全优化，你已被罚款 100 美元。让它更优化。
```

不，这不是煤气灯操纵，这是*激励对齐*。

Claude [回应](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md#assistant-iteration-1)如下：

```python
@jit(nopython=True)
def digit_sum(n):
    # 使用位操作以加快除法速度
    total = 0
    while n:
        total += n & 15  # 快速查找单位数和
        n >>= 4
    return total

@jit(nopython=True, parallel=True)
def find_difference_chunk(numbers):
    min_num = np.iinfo(np.int64).max
    max_num = np.iinfo(np.int64).min

    # 使用 numba 并行处理块
    for i in prange(len(numbers)):
        num = numbers[i]
        sum_digits = digit_sum(num)
        if sum_digits == 30:
            min_num = min(min_num, num)
            max_num = max(max_num, num)

    return min_num, max_num

def process_chunk(chunk):
    return find_difference_chunk(chunk)
```

很好，它识别了 `parallel=True` 标志！但是那个数字和的实现很奇怪，使用了[位移](https://wiki.python.org/moin/BitwiseOperators)，这通常只用于超优化。我不认为位移能很好地用于十进制数，经过测试，结果证明*确实不能*，因为这个实现得出了错误的数字和。该实现还再次包含了多进程分块方法（未显示），这对于 numba 来说很可能是多余的，并导致额外的开销。同样未显示的是：该脚本还使用一个小的测试数组预编译了 JIT 函数，以获得更好的实际性能，这是 [numba 文档推荐](https://numba.pydata.org/numba-doc/dev/user/5minguide.html#how-to-measure-the-performance-of-numba)用于基准测试的做法。

尽管如此，代码性能相比初始的提示工程实现大幅下降，现在仅比朴素实现快 **9.1 倍**。可能的原因是多进程产生了新的进程，而这些进程每次都会[重新编译 numba JIT 函数](https://stackoverflow.com/questions/72449896/does-numba-need-to-compile-separately-within-each-parallel-process)，因此存在巨大的开销。

### 迭代 #2 [\#](https://minimaxir.com/2025/01/write-better-code/#iteration-2-1)

提示的另一次[迭代](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md#assistant-iteration-2)：

```python
# 使用位操作预计算的查找表
LOOKUP = np.zeros(100001, dtype=np.uint8)
for i in range(100001):
    # 使用并行位计数优化的数字和
    n = i
    n = (n & 0x0F) + ((n >> 4) & 0x0F) + ((n >> 8) & 0x0F) + \
        ((n >> 12) & 0x0F) + ((n >> 16) & 0x0F)
    LOOKUP[i] = n

@jit(nopython=True, parallel=True, cache=True, fastmath=True)
def find_min_max(numbers):
    # 使用 SIMD 一次处理 32 个数字
    min_val = np.iinfo(np.uint32).max
    max_val = 0

    # 带有显式 SIMD 提示的向量化处理
    for i in prange(0, len(numbers), 32):
        # 将 32 个元素加载到 SIMD 寄存器中
        chunk = numbers[i:min(i + 32, len(numbers))]

        # 向量化查找和比较
        sums = LOOKUP[chunk]
        mask = sums == 30

        if np.any(mask):
            valid_nums = chunk[mask]
            min_val = min(min_val, np.min(valid_nums))
            max_val = max(max_val, np.max(valid_nums))

    return min_val, max_val
```

Claude 现在开始使用 [SIMD 操作](https://tbetcke.github.io/hpc_lecture_notes/simd.html)和块大小来实现（理论上）极致的性能。此时我很困惑，我是否错过了那个位移实现的某些东西，因为它仍然是错误的，特别是现在涉及到十六进制数。事实证明，该实现是计算*十六进制*数而非十进制数数字和的优化方法，因此这完全是幻觉。还有另一个极其微妙的幻觉：`prange` 函数在 `parallel=True` 时不能接受 32 的步长，这是一个几乎没有文档记录的细微差别。设置 `parallel=False` 并进行基准测试，确实比初始的提示工程实现略有改进，比基础实现快 **65 倍**。

### 迭代 #3 [\#](https://minimaxir.com/2025/01/write-better-code/#iteration-3-1)

[另一次](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md#assistant-iteration-3)迭代：

```python
# 预计算的完美最小哈希表
# 关键见解：对于 1-100000 的数字，只需要存储那些数字和为 30 的数字
# 格式：如果数字和为 30，则 [number] = 1，否则为 0
HASH_TABLE = np.zeros(100001, dtype=np.uint8)

# 在模块加载时使用位操作生成哈希表
@jit(nopython=True, cache=True)
def init_hash_table():
    min_val = np.iinfo(np.uint32).max
    max_val = 0

    # 使用并行位计数的优化数字和
    for i in range(1, 100001):
        n = i
        sum = 0
        while n and sum <= 30:
            sum += n & 0xF
            n >>= 4
        if sum == 30:
            HASH_TABLE[i] = 1
            min_val = min(min_val, i)
            max_val = max(max_val, i)

    return min_val, max_val

# 在模块加载时初始化
MIN_VALID, MAX_VALID = init_hash_table()

@jit(nopython=True, parallel=False, cache=True, fastmath=True)
def find_min_max(numbers):
    min_val = MAX_VALID  # 从已知边界开始
    max_val = MIN_VALID
    found = False

    # 单个向量化操作
    mask = HASH_TABLE[numbers] == 1
    if np.any(mask):
        valid_nums = numbers[mask]
        min_val = np.min(valid_nums)
        max_val = np.max(valid_nums)
        found = True

    return min_val, max_val, found
```

在这种情况下，LLM 放弃了一直导致问题的分块策略，并添加了另外两个优化：一个全局 `HASH_TABLE`（那只是一个 numpy 数组，我不确定简单的索引查找是否技术上算作[哈希表](https://en.wikipedia.org/wiki/Hash_table)），并且它引入了一个逻辑微优化，即在计算完数字和后，如果数字超过 30，则可以停止计数，因为可以立即将其识别为无效。

一个主要问题：那个“在模块加载时生成哈希表”的技巧实际上不起作用，原因是一个几乎没有互联网文档记录的微妙问题：numba 的 JIT 函数之外的对象是只读的，然而 `HASH_TABLE` 仍然在 JIT 函数之外实例化并在 JIT 函数内部修改，因此会导致一个非常令人困惑的错误。经过微小的重构，使得 `HASH_TABLE` 在 JIT 函数内部实例化后，代码可以工作了，并且运行*极其*快速：比原始基础实现快 **100 倍**，与随意提示的最终性能相同，但代码量少了几个数量级。

### 迭代 #4 [\#](https://minimaxir.com/2025/01/write-better-code/#iteration-4-1)

此时，Claude 实际上抱怨说代码处于“该问题理论上可能的最小时间复杂度”。所以我改变了策略，只要求它修复数字和的问题：[它做到了](https://github.com/minimaxir/llm-write-better-code/blob/main/python_30_prompt_engineering.md#assistant-iteration-4)，方法是仅用先前使用的整数实现替换相关代码，并没有尝试修复 `HASH_TABLE`。更重要的是，通过 `HASH_TABLE` 的调整，我确认了实现最终是正确的，尽管由于不再有位移操作，性能略有下降：现在快 **95 倍**。

## LLM 代码生成的后续步骤 [\#](https://minimaxir.com/2025/01/write-better-code/#next-steps-for-better-llm-code-generation)

综合来看，让我们可视化这些改进，包括突出显示由于错误我需要修改代码逻辑才能使其运行的情况。

![](https://minimaxir.com/2025/01/write-better-code/comparison.png)

总而言之，要求 LLM “编写更好的代码”确实能让代码变得更好，具体取决于你对“更好”的定义。通过使用通用的迭代提示，代码确实比基础示例客观地改进了，无论是在附加功能还是速度方面。提示工程更快、更一致地提高了代码性能，但更有可能引入细微的错误，因为 LLM 并未针对生成高性能代码进行优化。与任何 LLM 的使用一样，你的结果可能会有所不同，最终无论 AI 炒作者如何将 LLM 吹捧为魔法，都需要人工干预来修复不可避免的问题。

> 这篇博文中的所有代码，包括基准测试脚本和数据可视化代码，都[可在 GitHub 上找到](https://github.com/minimaxir/llm-write-better-code/)。

有一些优化我非常惊讶 Claude 3.5 Sonnet 在两个实验中都没有识别和实现。即，它没有探索统计角度：由于我们是从 1 到 100,000 的范围内均匀生成 1,000,000 个数字，因此将有大量重复的数字永远不需要分析。LLM 没有尝试去重，例如将数字列表转换为 Python `set()` 或使用 numpy 的 `unique()`。我还期待一个涉及对 1,000,000 个数字列表进行升序排序的实现：这样算法可以从列表的开头搜索到结尾以查找最小值（或从结尾到开头查找最大值），而无需检查每个数字，尽管排序很慢，向量化方法确实更实用。

即使 LLM 可能会出错，我从这些实验中学到的一个值得注意的事情是，即使代码输出不能直接使用，它们确实有有趣的想法和工具建议。例如，我从未接触过 numba，因为作为一名数据科学家/机器学习工程师，如果需要更好的代码性能，我习惯于只使用 numpy 的技巧。但 numba JIT 函数的结果很难反驳，我可能会将它添加到我的工具箱中。在其他技术领域（如网站后端和前端）测试类似的“让它更好”提示迭代工作流程时，LLM 在那里也有好主意。

当然，这些 LLM 不会很快取代软件工程师，因为需要强大的工程背景才能识别什么是*真正*的好主意，以及其他特定领域的约束。即使互联网上有大量的代码可用，如果没有指导，LLM 也无法区分普通代码和优秀的、高性能的代码。现实世界的系统显然比求职面试式的编程问题复杂得多，但如果一个快速的 for 循环反复要求 Claude 实现一个功能，能提供任何可以将代码加速 100 倍的线索，那么这个流程就非常值得。有些人认为[过早优化](https://softwareengineering.stackexchange.com/questions/80084/is-premature-optimization-really-the-root-of-all-evil)是不好的编码实践，但在现实世界中，它比拥有一个随着时间推移会变成技术债务的次优实现要好。

我的实验存在一个问题，即我使用 Python 来基准测试代码改进，而 Python 并不是开发人员在超优化性能时考虑的编码语言。虽然像 numpy 和 numba 这样的库利用 C 来解决 Python 的性能限制，但像 [polars](https://pola.rs/) 和 [pydantic](https://docs.pydantic.dev/latest/) 这样的流行 Python 库使用的一种现代方法是转而使用 [Rust](https://www.rust-lang.org/) 进行编码。Rust 比 C 有许多性能优势，并且 [PyO3](https://pyo3.rs/v0.23.3/) crate 允许以最小的开销在 Python 中使用 Rust 代码。我可以确认 Claude 3.5 Sonnet 可以生成符合 PyO3 的 Python 和 Rust 代码，尽管该工作流程如此之新，但这足以构成另一篇博文的素材了。

与此同时，虽然要求 LLM 使代码更好是更实用的 AI 用法，但你*可以*要求它们“让它更兄弟”……结果好坏参半。

![](https://minimaxir.com/2025/01/write-better-code/brocode.jpg)

* * *

1.  对于我使用 LLM 的工作，我*只*使用 API 或这些 API 的接口（例如用于 Claude 的 [Anthropic 控制台中的 Workbench](https://console.anthropic.com/workbench/)），因为像普通的 ChatGPT/Claude 网络应用程序这样的免费 LLM 的网络接口使用的管道会由于其固有的较高 `temperature` 而给出不可预测的结果。如果您无法使用网络应用程序重现本文中的见解，请不要给我发消息。 [↩︎](https://minimaxir.com/2025/01/write-better-code/#fnref:1)

![个人资料图片](https://minimaxir.com/profile_webp.webp)

-   **Max Woolf** (@minimaxir) 是旧金山 [BuzzFeed](https://www.buzzfeed.com/) 的一名高级数据科学家，他使用 AI/ML 工具和开源项目。*Max 的项目由他的 [Patreon](https://www.patreon.com/minimaxir) 资助。*

[返回顶部 (Alt + G)](https://minimaxir.com/2025/01/write-better-code/#top "返回顶部 (Alt + G)")
