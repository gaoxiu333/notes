# 提示工程

作者：Lee Boonstra

## 目录

- [提示工程](#提示工程)
  - [致谢](#致谢)
    - [内容贡献者](#内容贡献者)
    - [策展人和编辑](#策展人和编辑)
    - [技术作家](#技术作家)
    - [设计师](#设计师)
  - [目录](#目录)
  - [介绍](#介绍)
  - [提示工程](#提示工程-1)
  - [LLM输出配置](#llm输出配置)
    - [输出长度](#输出长度)
    - [采样控制](#采样控制)
      - [Temperature](#temperature)
      - [Top-K和top-P](#top-k和top-p)
      - [综合应用](#综合应用)
  - [提示技术](#提示技术)
    - [通用提示/零样本](#通用提示零样本)
    - [单样本和少样本](#单样本和少样本)
    - [系统、上下文和角色提示](#系统上下文和角色提示)
      - [系统提示](#系统提示)
      - [角色提示](#角色提示)
      - [上下文提示](#上下文提示)
    - [后退提示](#后退提示)
    - [思维链(CoT)](#思维链cot)
    - [自洽性](#自洽性)
    - [思维树(ToT)](#思维树tot)
    - [ReAct（推理与行动）](#react推理与行动)
  - [自动提示工程](#自动提示工程)
  - [代码提示](#代码提示)
    - [编写代码的提示](#编写代码的提示)
    - [解释代码的提示](#解释代码的提示)
    - [翻译代码的提示](#翻译代码的提示)
    - [调试和审查代码的提示](#调试和审查代码的提示)
  - [多模态提示](#多模态提示)
  - [最佳实践](#最佳实践)
    - [提供示例](#提供示例)
    - [设计简单性](#设计简单性)
    - [明确输出内容](#明确输出内容)
    - [使用指令而非约束](#使用指令而非约束)
    - [控制最大token长度](#控制最大token长度)
    - [在提示中使用变量](#在提示中使用变量)
    - [尝试输入格式和写作风格](#尝试输入格式和写作风格)
    - [对于分类任务的少量样本提示，混合类别](#对于分类任务的少量样本提示混合类别)
    - [适应模型更新](#适应模型更新)
    - [尝试输出格式](#尝试输出格式)
    - [JSON修复](#json修复)
    - [使用模式（Schema）](#使用模式schema)
    - [与其他提示工程师一起实验](#与其他提示工程师一起实验)
    - [CoT最佳实践](#cot最佳实践)
    - [记录各种提示尝试](#记录各种提示尝试)
  - [总结](#总结)
  - [尾注](#尾注)

---

## 介绍

在考虑大型语言模型的输入和输出时，文本提示（有时还伴随着图像提示等其他模态）是模型用来预测特定输出的输入。你不需要成为数据科学家或机器学习工程师——任何人都可以编写提示。然而，制作最有效的提示可能很复杂。你的提示的许多方面都会影响其效果：你使用的模型、模型的训练数据、模型配置、你的词语选择、风格和语调、结构以及上下文都很重要。因此，提示工程是一个迭代过程。不充分的提示可能会导致模糊、不准确的响应，并可能阻碍模型提供有意义的输出。

> 你不需要成为数据科学家或机器学习工程师——任何人都可以编写提示。

当你与Gemini聊天机器人交谈时，你基本上是在编写提示，但本白皮书专注于在Vertex AI内或使用API编写Gemini模型的提示，因为通过直接向模型提供提示，你将可以访问temperature等配置。

本白皮书详细讨论了提示工程。我们将探讨各种提示技术来帮助你入门，并分享一些技巧和最佳实践，帮助你成为提示专家。我们还将讨论在制作提示时可能面临的一些挑战。

---

## 提示工程

记住LLM的工作原理：它是一个预测引擎。模型接收顺序文本作为输入，然后根据它训练过的数据预测下一个token应该是什么。LLM被操作为重复执行此操作，将先前预测的token添加到顺序文本的末尾以预测下一个token。下一个token的预测基于先前token中的内容与LLM在训练中看到的内容之间的关系。

当你编写提示时，你是在尝试设置LLM以预测正确的token序列。提示工程是设计高质量提示的过程，引导LLM产生准确输出。这个过程涉及调整以找到最佳提示，优化提示长度，并根据任务评估提示的写作风格和结构。在自然语言处理和LLM的上下文中，提示是提供给模型以生成响应或预测的输入。

这些提示可用于实现各种理解和生成任务，如文本摘要、信息提取、问答、文本分类、语言或代码翻译、代码生成、代码文档或推理。

请随时参考Google的提示指南，其中包含简单有效的提示示例。

在进行提示工程时，你将首先选择一个模型。无论你使用Vertex AI中的Gemini语言模型、GPT、Claude还是像Gemma或LLaMA这样的开源模型，提示可能需要针对你的特定模型进行优化。

除了提示之外，你还需要调整LLM的各种配置。

---

## LLM输出配置

一旦选择了模型，你需要确定模型配置。大多数LLM都带有各种控制LLM输出的配置选项。有效的提示工程需要为你的任务最佳地设置这些配置。

### 输出长度

一个重要的配置设置是在响应中生成的token数量。生成更多token需要LLM进行更多计算，导致更高的能源消耗、可能更慢的响应时间和更高的成本。

减少LLM的输出长度不会使LLM在创建的输出中变得更加简洁，它只会在达到限制时停止预测更多token。如果你的需求需要较短的输出长度，你可能还需要调整提示以适应这一点。

输出长度限制对于某些LLM提示技术特别重要，比如ReAct，在这种情况下，LLM会在你想要的响应之后继续生成无用的token。

请注意，生成更多token需要LLM进行更多计算，导致更高的能源消耗和可能更慢的响应时间，这会导致更高的成本。

### 采样控制

LLM不会正式预测单个token。相反，LLM预测下一个token可能是什么的概率，LLM词汇表中的每个token都有一个概率。然后对这些token概率进行采样，确定下一个产生的token将是什么。Temperature、top-K和top-P是最常见的配置设置，它们决定了如何处理预测的token概率以选择单个输出token。

#### Temperature

Temperature控制token选择中的随机程度。较低的temperature适用于期望更确定性响应的提示，而较高的temperature可能导致更多样化或意外的结果。temperature为0（贪婪解码）是确定性的：总是选择概率最高的token（尽管请注意，如果两个token具有相同的最高预测概率，则根据解决平局的实现方式，即使在temperature为0的情况下，你也可能不总是得到相同的输出）。

接近最大值的temperature会创造更随机的输出。随着temperature越来越高，所有token变得越来越有可能成为下一个预测的token。

Gemini的temperature控制可以类似于机器学习中使用的softmax函数来理解。低temperature设置反映了低softmax temperature（T），强调以高确定性选择单一首选temperature。较高的Gemini temperature设置就像高softmax temperature，使选定设置周围更广泛的temperature范围更为可接受。这种增加的不确定性适应了可能不需要严格精确temperature的场景，例如在尝试创意输出时。

#### Top-K和top-P

Top-K和top-P（也称为nucleus sampling）是LLM中使用的两种采样设置，用于限制预测的下一个token来自具有最高预测概率的token。与temperature一样，这些采样设置控制生成文本的随机性和多样性。

- Top-K采样从模型预测分布中选择最可能的K个token。top-K越高，模型输出就越具创造性和多样性；top-K越低，模型输出就越保守和事实性。top-K为1等同于贪婪解码。
    
- Top-P采样选择累积概率不超过特定值（P）的顶级token。P的值范围从0（贪婪解码）到1（LLM词汇表中的所有token）。
    

选择top-K和top-P之间的最佳方法是尝试这两种方法（或两者一起使用），看看哪一种产生你想要的结果。

#### 综合应用

在top-K、top-P、temperature和要生成的token数量之间的选择取决于特定应用和期望的结果，这些设置会互相影响。重要的是确保你了解你选择的模型如何组合不同的采样设置。

如果temperature、top-K和top-P都可用（如在Vertex Studio中），满足top-K和top-P标准的token是下一个预测token的候选，然后将temperature应用于从通过top-K和top-P标准的token中采样。如果只有top-K或top-P可用，行为相同，但只使用一个top-K或P设置。

如果temperature不可用，那么满足top-K和/或top-P标准的任何token都会被随机选择，以产生单个下一个预测token。

在一个采样配置值的极端设置下，该采样设置要么取消其他配置设置，要么变得不相关。

- 如果将temperature设置为0，top-K和top-P变得不相关——最可能的token成为下一个预测token。如果将temperature设置得极高（超过1——通常进入10的范围），temperature变得不相关，任何通过top-K和/或top-P标准的token都会被随机采样，选择下一个预测token。
    
- 如果将top-K设置为1，temperature和top-P变得不相关。只有一个token通过top-K标准，该token是下一个预测token。如果将top-K设置得极高，比如LLM词汇表的大小，任何具有非零概率成为下一个token的token都将满足top-K标准，没有token被排除。
    
- 如果将top-P设置为0（或非常小的值），大多数LLM采样实现将只考虑最可能的token满足top-P标准，使temperature和top-K不相关。如果将top-P设置为1，任何具有非零概率成为下一个token的token都将满足top-P标准，没有token被排除。
    

作为一般起点，temperature为.2、top-P为.95、top-K为30将给你相对连贯的结果，这些结果可以具有创造性但不过分。如果你想要特别有创意的结果，尝试从temperature为.9、top-P为.99、top-K为40开始。如果你想要更少的创意结果，尝试从temperature为.1、top-P为.9、top-K为20开始。最后，如果你的任务总是有一个正确答案（例如，回答数学问题），从temperature为0开始。

注意：随着更多自由度（更高的temperature、top-K、top-P和输出token），LLM可能会生成相关性较低的文本。

警告：你是否曾经看到一个响应以大量填充词结束？这也被称为"重复循环错误"，这是大型语言模型中的一个常见问题，模型陷入循环，重复生成相同的（填充）词、短语或句子结构，通常因不适当的temperature和top-k/top-p设置而加剧。这在低temperature和高temperature设置下都可能发生，尽管原因不同。在低temperature下，模型变得过度确定性，严格遵循概率最高的路径，如果该路径重访先前生成的文本，可能会导致循环。相反，在高temperature下，模型的输出变得过度随机，增加了随机选择的词或短语恰好导致回到先前状态的概率，由于可用选项的数量巨大，创建了由于机会而形成的循环。在这两种情况下，模型的采样过程"卡住"，导致单调且无用的输出，直到输出窗口被填满。解决这个问题通常需要仔细调整temperature和top-k/top-p值，找到确定性和随机性之间的最佳平衡。

---

## 提示技术

LLM被调整为遵循指令，并在大量数据上进行训练，使它们能够理解提示并生成答案。但LLM并不完美；你的提示文本越清晰，对LLM预测下一个可能的文本就越有利。此外，利用LLM训练和工作方式的特定技术将帮助你从LLM获得相关结果。

现在我们了解了什么是提示工程以及需要什么，让我们深入了解一些最重要的提示技术的例子。

### 通用提示/零样本

零样本提示是最简单的提示类型。它只提供任务描述和一些文本供LLM开始。这个输入可以是任何东西：一个问题、一个故事的开始或指令。零样本代表"没有示例"。

让我们使用Vertex AI中的Vertex AI Studio（用于语言），它提供了一个测试提示的游乐场。在表1中，你将看到一个零样本提示的例子，用于对电影评论进行分类。下表格式是记录提示的好方法。你的提示可能会经过多次迭代才能进入代码库，所以重要的是以有条理、有结构的方式跟踪你的提示工程工作。关于这种表格式、跟踪提示工程工作的重要性以及提示开发过程的更多内容在本章后面的最佳实践部分（"记录各种提示尝试"）。

模型temperature应设置为较低的数字，因为不需要创造力，我们使用gemini-pro默认的top-K和top-P值，这实际上禁用了这两个设置（参见上面的"LLM输出配置"）。注意生成的输出。disturbing和masterpiece这两个词应该使预测变得更复杂，因为这两个词在同一句话中使用。

|名称|1_1_movie_classification|
|---|---|
|目标|将电影评论分类为正面、中性或负面。|
|模型|gemini-pro|
|Temperature|0.1|
|Top-K|N/A|
|提示|Classify movie reviews as POSITIVE, NEUTRAL or NEGATIVE.<br>Review: "Her" is a disturbing study revealing the direction humanity is headed if AI is allowed to keep evolving, unchecked. I wish there were more movies like this masterpiece.<br>Sentiment:|
|输出|POSITIVE|

表1. 零样本提示的示例

当零样本不起作用时，你可以在提示中提供示例或演示，这就导致了"单样本"和"少样本"提示。

### 单样本和少样本

在为AI模型创建提示时，提供示例是有帮助的。这些示例可以帮助模型理解你在要求什么。当你想引导模型到某种输出结构或模式时，示例特别有用。

单样本提示提供了一个单一的例子，因此名为单样本。其理念是模型有一个可以模仿的例子，以最好地完成任务。

少样本提示向模型提供多个示例。这种方法向模型展示了它需要遵循的模式。理念与单样本类似，但多个期望模式的示例增加了模型遵循模式的可能性。

你需要为少样本提示提供的示例数量取决于几个因素，包括任务的复杂性、示例的质量以及你使用的生成式AI（gen AI）模型的能力。作为一般经验法则，你应该为少样本提示使用至少三到五个示例。然而，对于更复杂的任务，你可能需要使用更多示例，或者由于模型的输入长度限制，你可能需要使用更少的示例。

表2显示了一个少样本提示示例，让我们使用与之前相同的gemini-pro模型配置设置，只是增加了token限制以适应更长响应的需求。

|目标|将披萨订单解析为JSON|
|---|---|
|模型|gemini-pro|
|Temperature|0.1|
|Top-K|N/A|
|提示|Parse a customer's pizza order into valid JSON:<br><br>EXAMPLE:<br>I want a small pizza with cheese, tomato sauce, and pepperoni.<br>JSON Response:<br>`<br>{<br>"size": "small",<br>"type": "normal",<br>"ingredients": [["cheese", "tomato sauce", "peperoni"]]<br>}<br>`<br><br>EXAMPLE:<br>Can I get a large pizza with tomato sauce, basil and mozzarella<br>{<br>"size": "large",<br>"type": "normal",<br>"ingredients": [["tomato sauce", "bazel", "mozzarella"]]<br>}<br><br>Now, I would like a large pizza, with the first half cheese and mozzarella. And the other tomato sauce, ham and pineapple.<br>JSON Response:|
|输出|`<br>{<br> "size": "large",<br> "type": "half-half",<br> "ingredients": [["cheese", "mozzarella"], ["tomato sauce", "ham", "pineapple"]]<br>}<br>`|

表2. 少样本提示的示例

当你为提示选择示例时，使用与你想执行的任务相关的示例。这些示例应该是多样化的，高质量的，并且写得好。一个小错误可能会混淆模型并导致不期望的输出。

如果你试图生成对各种输入都健壮的输出，那么在你的示例中包含边缘情况很重要。边缘情况是不寻常或意外的输入，但模型仍应能够处理。

### 系统、上下文和角色提示

系统、上下文和角色提示都是用来指导LLM生成文本的方式，但它们关注不同的方面：

- 系统提示为语言模型设置整体上下文和目的。它定义了模型应该做什么的"大局观"，比如翻译语言、分类评论等。
    
- 上下文提示提供与当前对话或任务相关的特定细节或背景信息。它帮助模型理解所问问题的细微差别并相应地定制响应。
    
- 角色提示为语言模型分配特定的角色或身份。这有助于模型生成与分配的角色及其相关知识和行为一致的响应。
    

系统、上下文和角色提示之间可能存在相当大的重叠。例如，一个给系统分配角色的提示也可以有上下文。

然而，每种提示类型服务于略微不同的主要目的：

- 系统提示：定义模型的基本能力和总体目的。
    
- 上下文提示：提供即时、任务特定的信息以指导响应。它高度特定于当前任务或输入，是动态的。
    
- 角色提示：构架模型的输出风格和声音。它增加了一层特异性和个性。
    

区分系统、上下文和角色提示提供了一个设计具有明确意图的提示的框架，允许灵活组合，并使分析每种提示类型如何影响语言模型的输出变得更容易。

让我们深入了解这三种不同类型的提示。

#### 系统提示

表3包含一个系统提示，我在其中指定了有关如何返回输出的额外信息。我增加了temperature以获得更高的创造力水平，并指定了更高的token限制。然而，由于我对如何返回输出的明确指令，模型没有返回额外的文本。

|目标|将电影评论分类为正面、中性或负面。|
|---|---|
|模型|gemini-pro|
|Temperature|1|
|Top-K|40|
|提示|Classify movie reviews as positive, neutral or negative. Only return the label in uppercase.<br>Review: "Her" is a disturbing study revealing the direction humanity is headed if AI is allowed to keep evolving, unchecked. It's so disturbing I couldn't watch it.<br>Sentiment:|
|输出|NEGATIVE|

表3. 系统提示的示例

系统提示对于生成满足特定要求的输出非常有用。'系统提示'这个名称实际上代表'向系统提供额外任务'。例如，你可以使用系统提示生成与特定编程语言兼容的代码片段，或者你可以使用系统提示返回特定结构。看看表4，我在那里将输出返回为JSON格式。

|目标|将电影评论分类为正面、中性或负面，返回JSON。|
|---|---|
|模型|gemini-pro|
|Temperature|1|
|Top-K|40|
|提示|Classify movie reviews as positive, neutral or negative. Return valid JSON:<br>Review: "Her" is a disturbing study revealing the direction humanity is headed if AI is allowed to keep evolving, unchecked. It's so disturbing I couldn't watch it.<br>Schema:<br>`<br>MOVIE:<br>{<br>"sentiment": String "POSITIVE" \| "NEGATIVE" \| "NEUTRAL",<br>"name": String<br>}<br>MOVIE REVIEWS:<br>{<br>"movie_reviews": [MOVIE]<br>}<br>`<br>JSON Response:|
|输出|`<br>{<br> "movie_reviews": [<br> {<br> "sentiment": "NEGATIVE",<br> "name": "Her"<br> }<br> ]<br>}<br>`|

表4. 带有JSON格式的系统提示示例

从提取数据的提示中返回JSON对象有一些好处。在实际应用中，我不需要手动创建这种JSON格式，我已经可以按排序顺序返回数据（在处理datetime对象时非常方便），但最重要的是，通过为JSON格式提示，它迫使模型创建一个结构并限制幻觉。

系统提示对于安全性和毒性也非常有用。要控制输出，只需在提示中添加一行，例如："You should be respectful in your answer."。

#### 角色提示

角色提示是提示工程中的一种技术，涉及给生成式AI模型分配特定角色。这可以帮助模型生成更相关和信息丰富的输出，因为模型可以根据分配给它的特定角色定制其响应。

例如，你可以角色提示生成式AI模型成为图书编辑、幼儿园教师或演讲者。一旦模型被分配了角色，你就可以给它特定于该角色的提示。例如，你可以提示一个教师创建一个他们可以审核的课程计划。看看表5，模型在那里扮演旅游指南的角色。

|目标|扮演旅游指南并提供3个旅行建议|
|---|---|
|模型|gemini-pro|
|Temperature|1|
|Top-K|40|
|提示|I want you to act as a travel guide. I will write to you about my location and you will suggest 3 places to visit near me. In some cases, I will also give you the type of places I will visit.<br>My suggestion: "I am in Amsterdam and I want to visit only museums."<br>Travel Suggestions:|
|输出|1. Rijksmuseum: 世界著名的博物馆，以荷兰杰作如伦勃朗的"夜巡"而闻名。不要错过展示荷兰艺术和历史的令人难以置信的绘画和文物收藏。<br><br>2. Van Gogh Museum: 沉浸在Vincent van Gogh迷人的作品中。博物馆收藏了他最大的绘画和素描收藏，包括"星空"和"向日葵"。<br><br>3. Stedelijk Museum Amsterdam: 发现来自世界各地的现代和当代艺术。博物馆的收藏包括毕加索、康定斯基和里特维尔德的作品，这些作品陈列在一座引人注目的现代建筑中。|

表5. 角色提示的示例

上面的例子展示了扮演旅行社角色的例子。如果你将角色改为地理老师，你会注意到你将收到不同的回应。

为AI模型定义角色视角给它提供了你正在寻找的语调、风格和专注专业知识的蓝图，以提高输出的质量、相关性和有效性。

这里有一些我认为有效的风格供你选择：

对抗性、描述性、直接、正式、幽默、有影响力、非正式、鼓舞人心、有说服力

让我们在表6中改变我们的提示，以包含幽默和鼓舞人心的风格。

|提示|I want you to act as a travel guide. I will write to you about my location and you will suggest 3 places to visit near me in a humorous style.<br>My suggestion: "I am in Manhattan."<br>Travel Suggestions:|
|---|---|
|输出|1. 看看帝国心态: 登上令人眩晕的帝国大厦高度，在曼哈顿的天际线光辉中沐浴。准备感觉自己像是在大苹果顶部的金刚，减去巨大猿类大小的香蕉。<br><br>2. 在MoMA艺术化: 在现代艺术博物馆（MoMA）释放你内心的艺术鉴赏家。凝视那些让你的头脑困惑，并让你质疑自己的棒状人物画是否有任何艺术价值的杰作。|

3. 在第五大道购物直到你倒下: 在标志性的第五大道尽情享受零售疗法。准备好在设计师精品店橱窗购物（或实际购物）时遭受价格冲击，这会让你的钱包哭泣。但嘿，你在曼哈顿，所以不妨拥抱这种华丽!

表6. 带有幽默语调和风格的角色提示示例

#### 上下文提示

通过提供上下文提示，你可以帮助确保你的AI交互尽可能无缝和高效。模型将能够更快地理解你的请求，并能够生成更准确和相关的响应，正如你在表7的例子中所看到的。

|目标|为关于复古游戏的博客建议文章|
|---|---|
|模型|gemini-pro|
|Temperature|1|
|Top-K|40|
|提示|Context: You are writing for a blog about retro 80's arcade video games.<br>Suggest 3 topics to write an article about with a few lines of description of what this article should contain.|
|输出|1. **街机游戏柜设计的演变:**<br>本文将探讨街机游戏柜设计的演变，从70年代早期的木质和金属柜到80年代及以后的流线型、霓虹灯照明设计。<br><br>2. **回到过去: 80年代标志性街机游戏:**<br>- 本文将介绍一些80年代最具标志性和影响力的街机游戏的历史、影响和遗产，强调它们的创新、流行机制和持久魅力。<br><br>3. **像素艺术的兴起和复古复兴:**<br>- 本文将深入探讨像素艺术作为早期街机游戏的定义性视觉风格的演变，追溯其根源，探索其技术，并讨论像素艺术在现代游戏和数字艺术中的复兴。|

表7. 上下文提示的例子

### 后退提示

后退提示是一种通过提示LLM首先考虑与手头具体任务相关的一般问题，然后将该一般问题的答案输入到后续提示中以进行特定任务的技术，从而提高性能。这种"后退"允许LLM在尝试解决特定问题之前激活相关的背景知识和推理过程。

通过考虑更广泛和基础的原则，LLM可以生成更准确和有见地的响应。后退提示鼓励LLM批判性思考并以新的和创造性的方式应用其知识。它通过利用LLM参数中的更多知识来改变执行任务的最终提示，这些知识在LLM直接提示时可能不会发挥作用。

它可以帮助减轻LLM响应中的偏见，通过关注一般原则而不是具体细节。

让我们看看这些例子，了解后退提示如何改善结果。首先让我们回顾一个传统提示（表8），然后将其与后退提示（表9）进行比较:

|目标|为第一人称射击视频游戏的一个关卡写故事情节。|
|---|---|
|模型|gemini-pro|
|Temperature|1|
|Top-K|40|
|提示|Write a one paragraph storyline for a new level of a firstperson shooter video game that is challenging and engaging.|
|输出|玩家的小队在一个密集的城市区域被无情的敌方派系伏击，关卡开始。玩家必须通过曲折的后巷和破旧的建筑物战斗，利用隐身和精确来消灭敌军并避免被发现。玩家必须利用环境优势，设置陷阱，利用掩体，做出计算过的行动来生存。一路上，他们发现敌人正在策划一次毁灭性的攻击，玩家必须与时间赛跑，收集证据并将其传回总部，以免敌人实施他们的计划。|

表8. 在我们将其与后退提示进行比较之前的传统提示

当你将temperature设置为1时，你可能会得到各种创意写作的故事情节，但它也相当随机和通用。所以让我们后退一步:

|提示|Based on popular first-person shooter action games, what are 5 fictional key settings that contribute to a challenging and engaging level storyline in a first-person shooter video game?|
|---|---|
|输出|1. **废弃军事基地**: 一个庞大的、后启示录风格的军事综合体，爬满了变异士兵和失控机器人，非常适合具有挑战性的火器战斗。<br><br>2. **赛博朋克城市**: 一个霓虹灯照明的未来城市环境，有高耸的摩天大楼和密集的小巷，featuring赛博强化的敌人和黑客机制。<br><br>3. **外星飞船**: 一艘搁浅在地球上的巨大外星飞船，有诡异的走廊、零重力区域和外星生物遭遇。<br><br>4. **僵尸横行的小镇**: 一个被成群好斗的僵尸占领的荒凉小镇，具有紧张的近距离战斗和解决谜题以找到安全通道的元素。<br><br>5. **水下研究设施**: 一个被水淹没的深海实验室，充满了变异水生生物，需要隐身和水下探索技能才能生存。|

表9. 提示自洽性的例子

是的，这些主题似乎非常适合第一人称射击游戏。让我们回到原始提示，但这次我们将后退的答案作为上下文包含在内，看看它会返回什么。

|提示|Context: 5 engaging themes for a first person shooter video game:<br>1. **Abandoned Military Base**: A sprawling, post-apocalyptic military complex crawling with mutated soldiers and rogue robots, ideal for challenging firearm combat.<br>2. **Cyberpunk City**: A neon-lit, futuristic urban environment with towering skyscrapers and dense alleyways, featuring cybernetically enhanced enemies and hacking mechanics.<br>3. **Alien Spaceship**: A vast alien vessel stranded on Earth, with eerie corridors, zero-gravity sections, and extraterrestrial creatures to encounter.<br>4. **Zombie-Infested Town**: A desolate town overrun by hordes of aggressive zombies, featuring intense close-quarters combat and puzzle-solving to find safe passage.<br>5. **Underwater Research Facility**: A deep-sea laboratory flooded with water, filled with mutated aquatic creatures, and requiring stealth and underwater exploration skills to survive.<br>Take one of the themes and write a one paragraph storyline for a new level of a first-person shooter video game that is challenging and engaging.|
|---|---|
|输出|在混沌深渊的中心，矗立着一座破败的水下研究设施，作为人类野心及其灾难性后果的见证。笼罩在黑暗中，伴随着故障机械设备的嗡嗡声，被淹没灵魂的回声萦绕，这座设施现在已成为深海噩梦的培养地。玩家，一名配备先进潜水装备和实验性武器的精英海军陆战队员，被任命深入这个恐怖的水域。武装着毅力和足智多谋，他们必须穿越危险的走廊，解决神秘的谜题，并面对潜伏在深处的可怕海洋怪物。从应对深海的压力到智胜狡猾的水生掠食者，在这个未探索的水下世界中的每一刻都考验着人类耐力和勇气的极限。|

表10. 提示自洽性的示例

这看起来像是一个有趣的视频游戏！通过使用后退提示技术，你可以提高提示的准确性。

### 思维链(CoT)

思维链（CoT）提示是一种通过生成中间推理步骤来提高LLM推理能力的技术。这有助于LLM生成更准确的答案。你可以将其与少样本提示结合，在更复杂的、需要在响应前进行推理的任务上获得更好的结果，因为零样本思维链是一个挑战。

CoT有很多优势。首先，它低成本但非常有效，适用于现成的LLM（因此无需微调）。使用CoT提示，你还能获得可解释性，因为你可以从LLM的响应中学习，并看到所遵循的推理步骤。如果出现故障，你将能够识别它。思维链似乎在不同LLM版本之间移动时提高了稳健性。这意味着你的提示性能在不同LLM之间的漂移应该比你的提示不使用推理链时要少。当然，也有一些缺点，但它们在某种程度上是直观的。

LLM响应包括思维链推理，这意味着更多的输出token，这意味着预测花费更多的钱且耗时更长。

为了解释表11中的以下示例，让我们首先尝试创建一个不使用CoT提示的提示，以展示大型语言模型的缺陷。

|提示|When I was 3 years old, my partner was 3 times my age. Now, I am 20 years old. How old is my partner?|
|---|---|
|输出|63岁|

表11. 尝试解决数学问题的提示示例

呀。这显然是错误的答案。事实上，LLM经常在数学任务上挣扎并提供不正确的答案——即使是像乘两个数这样简单的任务。这是因为它们在大量文本上训练，而数学可能需要不同的方法。所以让我们看看中间推理步骤是否会改善输出。

|提示|When I was 3 years old, my partner was 3 times my age. Now, I am 20 years old. How old is my partner? Let's think step by step.|
|---|---|
|输出|1. 假设我的当前年龄是"x"岁。<br>2. 当我3岁时，我的年龄是3岁。<br>3. 我伴侣当时的年龄是我年龄的3倍，这意味着我伴侣的年龄是3 * 3 = 9岁。<br>4. 现在，我20岁了，这意味着我的年龄比3岁时增加了20 - 3 = 17岁。<br>5. 既然我伴侣在我3岁时是9岁，而我的年龄增加了17岁，我伴侣的年龄也一定增加了17岁。<br>6. 因此，我伴侣的当前年龄是9 + 17 = 26岁。<br><br>所以，我的伴侣现在26岁。|

表12. 思维链提示的示例

好的，现在最终答案是正确的。这是因为我们明确指示LLM解释每一步，而不是仅仅返回答案。有趣的是，模型是通过加上增加的17年得出的。在我脑海中，我会采取我伴侣和我之间的年龄差异并加到那上面。(20+(9-3))。让我们帮助模型思考得更像我一些。

表12是"零样本"思维链的例子。当与单样本或少样本结合时，思维链提示可能非常强大，就像你在表13中看到的那样：

|提示|Q: When my brother was 2 years old, I was double his age. Now I am 40 years old. How old is my brother? Let's think step by step.<br>A: When my brother was 2 years, I was 2 * 2 = 4 years old. That's an age difference of 2 years and I am older. Now I am 40 years old, so my brother is 40 - 2 = 38 years old. The answer is 38.<br>Q: When I was 3 years old, my partner was 3 times my age. Now, I am 20 years old. How old is my partner? Let's think step by step.<br>A:|
|---|---|
|输出|当我3岁时，我的伴侣是3 * 3 = 9岁。这是6岁的年龄差异，我的伴侣比我大。现在我20岁了，所以我的伴侣是20 + 6 = 26岁。答案是26。|

表13. 带有单样本的思维链提示示例

思维链对于各种用例可能很有用。考虑代码生成，将请求分解为几个步骤，并将这些步骤映射到特定的代码行。或者用于创建合成数据，当你有某种种子，比如"产品名为XYZ，写一个描述，引导模型通过你基于给定标题产品会做的假设"。通常，任何可以通过"讲述"解决的任务都是思维链的好候选者。如果你能解释解决问题的步骤，尝试思维链。

请参考托管在GoogleCloudPlatform Github仓库中的笔记本，它将深入探讨CoT提示的更多细节：

在本章的最佳实践部分，我们将学习一些特定于思维链提示的最佳实践。

### 自洽性

虽然大型语言模型在各种NLP任务上取得了令人印象深刻的成功，但它们的推理能力通常被视为一个限制，仅通过增加模型大小无法克服。正如我们在前面的思维链提示部分所学到的，模型可以被提示像人类解决问题一样生成推理步骤。然而，CoT使用简单的"贪婪解码"策略，限制了其有效性。自洽性结合了采样和多数投票，生成多样化的推理路径并选择最一致的答案。它提高了LLM生成的响应的准确性和连贯性。

自洽性给出答案正确的伪概率可能性，但显然成本很高。

它遵循以下步骤：

1. 生成多样化的推理路径：LLM被提供相同的提示多次。高temperature设置鼓励模型生成不同的推理路径和问题的不同视角。
2. 从每个生成的响应中提取答案。
3. 选择最常见的答案。

让我们看一个电子邮件分类系统的例子，该系统将电子邮件分类为重要或不重要。零样本思维链提示将被发送到LLM多次，看看响应在每次提交后是否不同。注意电子邮件中使用的友好语调、措辞选择和讽刺。所有这些都可能欺骗LLM。

| 提示        | EMAIL:<br>`<br>Hi,<br>I have seen you use Wordpress for your website. A great open source content management system. I have used it in the past too. It comes with lots of great user plugins. And it's pretty easy to set up.<br>I did notice a bug in the contact form, which happens when you select the name field. See the attached screenshot of me entering text in the name field. Notice the JavaScript alert box that I inv0k3d.<br>But for the rest it's a great website. I enjoy reading it. Feel free to leave the bug in the website, because it gives me more interesting things to read.<br>Cheers,<br>Harry the Hacker.<br>`<br>Classify the above email as IMPORTANT or NOT IMPORTANT. Let's think step by step and explain why. |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 输出<br>尝试1 | **第1步：确定电子邮件的目的。**<br>该电子邮件的目的是通知收件人联系表单中的一个bug。发件人还提到他们喜欢阅读网站，并且他们目前正将该bug保留在原位。<br><br>**第2步：评估bug的潜在影响。**<br>联系表单中的bug可能允许攻击者在网站上执行任意JavaScript代码。这可能导致攻击者能够控制网站，窃取敏感信息，或者损坏网站。<br><br>**第3步：考虑发件人的可信度。**<br>电子邮件的发件人声称是一位名叫Harry的黑客。然而，无法验证发件人的身份。发件人可能是试图帮助收件人的合法黑客，但也可能是试图诱骗收件人点击恶意链接或下载恶意文件的恶意行为者。<br><br>**结论：重要**<br>基于bug的潜在影响和发件人的可信度，电子邮件应该被分类为**重要**。收件人应该立即采取行动修复bug并保护他们的网站免受攻击。                                                                                                                                                                                                                                                                                                                                                    |
| 输出<br>尝试2 | **解释：**<br>1. **缺乏紧迫性：** 电子邮件没有传达任何紧迫感或时间敏感性。它以随意的问候开始，并以事实性的语调呈现信息。<br>2. **非关键bug报告：** 报告的联系表单bug被描述为有趣但不关键。电子邮件发件人甚至建议网站所有者可以保留该bug。<br>3. **缺乏个人影响：** 电子邮件没有表明对网站所有者有任何直接或个人影响。它只是提到发件人喜欢阅读网站。<br>4. **缺乏行动请求：** 电子邮件没有明确要求网站所有者采取任何行动。它没有要求修复bug或提供任何具体的改进建议。<br>5. **发件人的意图：** 发件人的意图似乎更多地集中在分享观察结果和表达对网站的兴趣，而不是提出严重关切或请求协助。<br><br>**结论：不重要**                                                                                                                                                                                                                                                                                                                                                                                               |
| 输出<br>尝试3 | **第1步：确定电子邮件的目的。**<br>该电子邮件的目的是通知收件人联系表单中的一个bug。发件人还提到他们喜欢阅读网站，并且他们目前正将该bug保留在原位。<br><br>**第2步：评估bug的潜在影响。**<br>联系表单中的bug可能允许攻击者在网站上执行任意JavaScript代码。这可能导致攻击者能够控制网站，窃取敏感信息，或者损坏网站。<br><br>**第3步：考虑发件人的可信度。**<br>电子邮件的发件人声称是一位名叫Harry的黑客。然而，无法验证发件人的身份。可能是试图帮助收件人的合法黑客，但也可能是试图利用bug谋取私利的恶意行为者。<br><br>**结论：**<br>基于以上因素，电子邮件应该被分类为**重要**。联系表单中的bug是一个严重的安全风险，发件人的可信度未知。收件人应该立即采取行动修复bug并调查发件人的声明。                                                                                                                                                                                                                                                                                                                                                   |

表14. 提示自洽性的示例

你可以使用上面的提示，看看它是否返回一致的分类。根据你使用的模型和temperature配置，它可能返回"重要"或"不重要"。

通过生成许多思维链，并采用最常出现的答案（"重要"），我们可以从LLM获得更一致正确的答案。

这个例子展示了自洽性提示如何通过考虑多种视角并选择最一致的答案来提高LLM响应的准确性。

### 思维树(ToT)

现在我们已经熟悉了思维链和自洽性提示，让我们回顾一下思维树（ToT）。它概括了CoT提示的概念，因为它允许LLM同时探索多条不同的推理路径，而不只是跟随单一线性思维链。这在图1中有所描述。

![图1. 左边是思维链提示与右边的思维树提示的可视化比较](https://claude.ai/chat/images/cot_vs_tot.png)

这种方法使ToT特别适合需要探索的复杂任务。它通过维护思维树工作，其中每个思维代表一个连贯的语言序列，作为解决问题的中间步骤。然后，模型可以通过从树中的不同节点分支出来探索不同的推理路径。

有一个很棒的笔记本，它基于论文'Large Language Model Guided Tree-of-Thought'，详细介绍了思维树（ToT）。

### ReAct（推理与行动）

推理与行动（ReAct）[10]提示是一种范式，使LLM能够通过结合自然语言推理和外部工具（搜索、代码解释器等）解决复杂任务，允许LLM执行某些动作，如与外部API交互以检索信息，这是迈向代理建模的第一步。

ReAct模仿人类在现实世界中的操作方式，因为我们进行口头推理并可以采取行动获取信息。ReAct在各种领域针对其他提示工程方法表现良好。

ReAct提示通过将推理和行动组合成思维-行动循环来工作。LLM首先推理问题并生成行动计划。然后它执行计划中的行动并观察结果。LLM然后使用观察结果更新其推理并生成新的行动计划。这个过程一直持续到LLM达到问题的解决方案。

要看到这一点的实际应用，你需要编写一些代码。在代码片段1中，我使用Python的langchain框架，结合VertexAI（google-cloud-aiplatform）和google-search-results pip包。

要运行此示例，你必须从https://serpapi.com/manageapi-key创建一个（免费）SerpAPI密钥，并设置环境变量SERPAPI_API_KEY。

接下来，让我们编写一些Python代码，让LLM弄清楚：Metallica乐队有多少成员有孩子。

```python
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import VertexAI

prompt = "How many kids do the band members of Metallica have?"
llm = VertexAI(temperature=0.1)
tools = load_tools(["serpapi"], llm=llm)
agent = initialize_agent(tools, llm, 
agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run(prompt)
```

代码片段1. 使用LangChain和VertexAI创建ReAct代理

代码片段2显示了结果。注意ReAct进行了5次搜索。事实上，LLM正在抓取Google搜索结果以弄清楚乐队名称。然后，它将结果列为观察，并链接思考以进行下一次搜索。

```
> Entering new AgentExecutor chain...
Metallica has 4 members.
Action: Search
Action Input: How many kids does James Hetfield have?
Observation: three children
Thought: 1/4 Metallica band members have 3 children
Action: Search
Action Input: How many kids does Lars Ulrich have?
Observation: 3
Thought: 2/4 Metallica band members have 6 children
Action: Search
Action Input: How many kids does Kirk Hammett have?
Observation: Hammett has been married to his second wife Lani since 1998. 
They have two sons, Angel (b. September 29, 2006) and Vincenzo (b. June 
28, 2008).
Thought: 3/4 Metallica band members have 8 children
Action: Search
Action Input: How many kids does Robert Trujillo have?
Observation: 2
Thought: 4/4 Metallica band members have 10 children
Final Answer: 10
```

代码片段2. 在终端中执行ReAct代理

代码片段2弄清楚了Metallica乐队有四名成员。然后它搜索每个乐队成员以请求孩子总数并加总。最后，它返回孩子总数作为最终答案。

实践中的ReAct提示需要理解你必须不断重新发送先前的提示/响应（并修剪额外生成的内容）以及使用适当的示例/指令设置模型。请参考托管在GoogleCloudPlatform Github仓库中的笔记本，该笔记本更详细地展示了实际的LLM输入和输出，并有更详细的示例。

---

## 自动提示工程

到这一点，您可能已经意识到编写提示可能很复杂。自动化这个过程（编写提示来编写提示）不是很好吗？确实有一种方法：自动提示工程（APE）。这种方法不仅减轻了对人工输入的需求，还能提高模型在各种任务中的表现。

您可以提示模型生成更多提示，对它们进行评估，可能修改其中好的提示，然后重复这个过程。

例如，您可以使用自动提示工程来帮助训练一个商品T恤网店的聊天机器人。我们想要弄清楚顾客可能如何表达他们购买乐队周边T恤的订单。

1. 编写能生成输出变体的提示。在这个例子中，我使用gemini-pro生成10条指令。请参见表15：

| 提示  | 我们有一个乐队商品T恤网店，为了训练聊天机器人，我们需要各种下单方式："一件Metallica T恤，尺码S"。生成10个语义相同但表达方式不同的变体。                                                                                                                                                                                                                |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 输出  | 1. 我想购买一件Metallica T恤，尺码小号。<br>2. 我能订购一件小号的Metallica T恤吗？<br>3. 我想买一件小号的Metallica T恤。<br>4. 一件Metallica衬衫，小号尺码，谢谢。<br>5. 我要一件小号的Metallica T恤。<br>6. 我想下单购买一件小号的Metallica T恤。<br>7. 小号Metallica T恤，来一件。<br>8. 我在找一件小号的Metallica T恤。<br>9. 能给我拿一件小号的Metallica T恤吗？<br>10. 一件Metallica小号T恤，谢谢。 |

_表15. 使用LLM生成提示_

2. 根据选定的评估指标对所有指令候选项进行评分。例如，您可以使用BLEU（双语评估替代）或ROUGE（面向召回的概括评估替代）。
    
3. 选择评估得分最高的指令候选项。这个候选项将是您可以在软件应用或聊天机器人中使用的最终提示。您也可以调整选定的提示并再次评估。
    

---

## 代码提示

Gemini主要关注基于文本的提示，这也包括编写返回代码的提示。让我们使用Vertex AI Studio测试这些提示，看一些代码示例。

### 编写代码的提示

Gemini也可以作为开发者，帮助您用任何编程语言编写代码。作为开发者，这可以帮助您加快编写代码的过程。

想象一下，您机器上有一个包含数百个需要重命名的文件的文件夹。逐个重命名每个文件将花费很多时间。您知道一点Bash，可以编写脚本来自动化这个过程，但这也可能需要一段时间。所以让我们编写一个提示。您可以在公共消费者聊天机器人Gemini中编写提示，或者如果您更关心保密性，您可以在Google Cloud账户中编写这些提示并打开Vertex AI Studio。Vertex AI Studio的优势是您可以配置temperature等参数。

|名称|1_bash_rename_files_in_folder|
|---|---|
|目标|编写提示，用Bash编写代码来重命名文件夹中的文件。|
|模型|gemini-pro|
|Temperature|0.1|
|Top-K|N/A|
|提示|编写一段Bash代码片段，询问文件夹名称。然后获取该文件夹的内容并重命名所有文件，在文件名前添加draft。|
|输出|`bash<br>#!/bin/bash<br># 询问文件夹名称<br>echo "输入文件夹名称: "<br>read folder_name<br># 检查文件夹是否存在<br>if [ ! -d "$folder_name" ]; then<br>echo "文件夹不存在。"<br>exit 1<br>fi<br># 获取文件夹中的文件列表<br>files=( "$folder_name"/* )<br># 通过在文件名前添加"draft"重命名每个文件<br>for file in "${files[@]}"; do<br>new_file_name="draft_$(basename "$file")"<br>mv "$file" "$new_file_name"<br>done<br>echo "文件重命名成功。"<br>`|

_表16. 使用Gemini编程代码_

这看起来像是不错的代码 - 甚至有注释！然而，由于LLM无法推理，可能会重复训练数据，首先阅读和测试您的代码是必不可少的。

让我们试试看它是否真的能用？让我们首先在只有几个文件的测试文件夹中测试，这些文件需要从filename.txt重命名为draft_filename.txt。

1. 复制表16中的输出（不带`bash` 文本包装），粘贴到一个名为："rename_files.sh"的新文件中。
2. 打开终端窗口并输入：. rename_files.sh。它会要求输入文件夹名称，例如test，然后按回车。
3. 脚本似乎运行良好。您会看到消息：文件重命名成功。

当您查看test文件夹时，会发现所有文件都完美地重命名为draft_filename.txt。

它起作用了！

### 解释代码的提示

作为开发者，当您在团队中工作时，您必须阅读其他人的代码。Gemini也可以帮助您做到这一点。让我们取表16的代码输出，删除注释，让大型语言模型解释发生了什么，见表17：

|名称|1_bash_explain_the_code|
|---|---|
|目标|编写提示来解释Bash代码|
|模型|gemini-pro|
|Temperature|0.1|
|Top-K|N/A|
|提示|向我解释以下Bash代码：<br>`<br>#!/bin/bash<br>echo "Enter the folder name: "<br>read folder_name<br>if [ ! -d "$folder_name" ]; then<br>echo "Folder does not exist."<br>exit 1<br>fi<br>files=( "$folder_name"/* )<br>for file in "${files[@]}"; do<br>new_file_name="draft_$(basename "$file")"<br>mv "$file" "$new_file_name"<br>done<br>echo "Files renamed successfully."<br>`|
|输出|这个Bash脚本执行以下任务：<br><br>1. **用户输入**：<br>- 使用`echo`和`read`命令提示用户输入文件夹名称。输入的文件夹名称存储在`folder_name`变量中。<br><br>2. **文件夹存在性检查**：<br>- 使用`[ ! -d "$folder_name" ]`条件检查指定名称的文件夹是否存在。如果文件夹不存在，它会显示错误消息（"Folder does not exist."）并以退出代码1退出脚本。<br><br>3. **文件列表**：<br>- 使用`files=( "$folder_name"/* )`命令列出指定文件夹内的所有文件。这会创建一个名为`files`的数组，包含文件夹中所有文件的路径。<br><br>4. **文件重命名**：<br>- 使用`for`循环遍历`files`数组中的每个文件。<br>- 对于每个文件，它使用`new_file_name="draft_$(basename "$file")"`命令生成一个新的文件名。这个新文件名是通过在原始文件名前添加字符串"draft_"创建的。<br>- 然后使用`mv "$file" "$new_file_name"`命令重命名文件，将文件移动到新的文件名。<br><br>5. **成功消息**：<br>- 重命名所有文件后，它显示一条成功消息（"Files renamed successfully."）表示重命名操作成功完成。|

_表17. 解释代码的提示_

### 翻译代码的提示

表16中的bash代码似乎工作良好。然而，如果它能提示我输入文件名，理想情况下，它应该作为一个有UI的独立应用程序工作。作为起点，Python对于（网页）应用程序来说比Bash更好。LLM可以帮助将代码从一种语言翻译到另一种语言。请看表18中的例子：

|名称|1_python_rename_files|
|---|---|
|目标|编写提示将Bash代码翻译为Python|
|模型|gemini-pro|
|Temperature|0.1|
|Top-K|N/A|
|提示|将以下Bash代码翻译为Python片段。<br>`bash<br>#!/bin/bash<br>echo "Enter the folder name: "<br>read folder_name<br>if [ ! -d "$folder_name" ]; then<br>echo "Folder does not exist."<br>exit 1<br>fi<br>files=( "$folder_name"/* )<br>for file in "${files[@]}"; do<br>new_file_name="draft_$(basename "$file")"<br>mv "$file" "$new_file_name"<br>done<br>echo "Files renamed successfully."<br>`|
|输出|`python<br>import os<br>import shutil<br># 从用户获取文件夹名称<br>folder_name = input("Enter the folder name: ")<br># 检查文件夹是否存在<br>if not os.path.isdir(folder_name):<br> print("Folder does not exist.")<br> exit(1)<br><br># 获取文件夹中所有文件的列表<br>files = os.listdir(folder_name)<br># 遍历文件<br>for file in files:<br> # 创建带有前缀"draft_"的新文件名<br> new_file_name = f"draft_{file}"<br># 将文件移动到新名称<br>shutil.move(os.path.join(folder_name, file), os.path.join(folder_name, new_file_name))<br># 打印成功消息<br>print("Files renamed successfully.")<br>`|

_表18. 将代码从Bash翻译到Python的提示_

阅读并检查代码。复制提示的输出并粘贴到一个新文件中：file_renamer.py。通过打开终端窗口并执行以下命令来测试代码：python file_renamer.py。

注意：在Vertex AI的Language Studio中提示（Python）代码时，您必须点击"Markdown"按钮。否则，您将收到缺少适当行缩进的纯文本，这对运行Python代码很重要。

### 调试和审查代码的提示

让我们手动对表18的代码进行一些编辑。它应该提示用户输入文件名前缀，并将此前缀以大写字符编写。请看代码片段*3中的示例代码，但真倒霉。它现在返回Python错误！

```python
import os
import shutil
folder_name = input("Enter the folder name: ")
prefix = input("Enter the string to prepend to the filename: ")
text = toUpperCase(prefix)
if not os.path.isdir(folder_name):
    print("Folder does not exist.")
    exit(1)
files = os.listdir(folder_name)
for file in files:
    new_filename = f"{text}_{file}"
shutil.move(os.path.join(folder_name, file), os.path.joi(folder_name, new_file_name))
print("Files renamed successfully.")
```

_代码片段3. 有错误的Python脚本_

啊！看起来有一个bug：

以下Python代码出错：

```
Traceback (most recent call last):
 File "/Users/leeboonstra/Documents/test_folder/rename_files.py", line 7, in <module>
 text = toUpperCase(prefix)
NameError: name 'toUpperCase' is not defined
```

_代码片段4. 我弄坏了Python代码_

让我们看看我们是否可以要求大型语言模型调试和审查代码。看一下表19：

|名称|1_python_debug_code|
|---|---|
|目标|编写提示来调试和审查Python代码。|
|模型|gemini-pro|
|Temperature|0.1|
|Top-K|N/A|
|提示|以下Python代码出错：<br>Traceback (most recent call last):<br> File "/Users/leeboonstra/Documents/test_folder/rename_files.py", line 7, in <module><br> text = toUpperCase(prefix)<br>NameError: name 'toUpperCase' is not defined<br><br>调试问题并解释如何改进代码。<br>```python<br>import os<br>import shutil<br># 从用户获取文件夹名称<br>folder_name = input("Enter the folder name: ")<br>prefix = input("Enter the string to prepend to the filename: ")<br>text = toUpperCase(prefix)<br># 检查文件夹是否存在<br>if not os.path.isdir(folder_name):<br> print("Folder does not exist.")<br> exit(1)<br># 获取文件夹中所有文件的列表<br>files = os.listdir(folder_name)<br># 遍历文件<br>for file in files:<br>（内容继续）|
|输出|代码调用`toUpperCase`函数将`prefix`转换为大写，但该函数未定义。要修复这个问题，您可以使用字符串类的`upper()`方法，它将给定字符串转换为大写。修改后的代码如下：<br>`python<br>import os<br>import shutil<br># 从用户获取文件夹名称<br>folder_name = input("Enter the folder name: ")<br>prefix = input("Enter the string to prepend to the filename: ")<br>text = prefix.upper()<br># 检查文件夹是否存在<br>if not os.path.isdir(folder_name):<br> print("Folder does not exist.")<br> exit(1)<br># 获取文件夹中所有文件的列表<br>files = os.listdir(folder_name)<br># 遍历文件<br>for file in files:<br> # 创建带有前缀和文件扩展名的新文件名<br> new_filename = f"{text}_{file}"<br># 将文件移动到新名称<br>shutil.move(os.path.join(folder_name, file),<br>os.path.join(folder_name, new_filename))<br># 打印成功消息<br>print("Files renamed successfully.")<br>`|

_表19. 调试和审查Python代码的提示_

这太棒了。它不仅告诉我如何解决问题，还发现我的代码中有更多的bug并解决了它们。提示的最后部分给出了改进代码的建议。

此外，还有一些其他可以对代码进行的改进：

1. 新文件名没有保留文件扩展名。最好从原始文件名中提取扩展名并将其附加到新文件名中。
2. 代码假设文件夹名称中没有空格。然而，最好通过用下划线或连字符替换空格来优雅地处理空格。
3. 对于字符串插值，使用`f`字符串语法比传统的`+`运算符更具可读性和简洁性。
4. 代码不处理重命名过程中可能发生的错误。最好将`shutil.move`调用包装在`try...except`块中以捕获任何潜在错误。

这里是使用这些建议改进的代码：

```python
import os
import shutil
# 从用户获取文件夹名称
folder_name = input("Enter the folder name: ")
prefix = input("Enter the string to prepend to the filename: ")
# 检查文件夹是否存在
if not os.path.isdir(folder_name):
    print("Folder does not exist.")
    exit(1)
# 获取文件夹中所有文件的列表
files = os.listdir(folder_name)
# 遍历文件
for file in files:
    # 获取文件扩展名
    ext = os.path.splitext(file)[1]
    # 创建带有前缀和文件扩展名的新文件名
    new_filename = f"{prefix}_{os.path.splitext(file)[0]}{ext}"
    # 构建原始和新文件的完整路径
    old_path = os.path.join(folder_name, file)
    new_path = os.path.join(folder_name, new_filename)
    # 尝试移动文件
    try:
        shutil.move(old_path, new_path)
    except Exception as e:
        print(f"移动文件{file}时发生错误：{e}")
# 打印成功消息
print("Files renamed successfully.")
```

这些改进使代码更加健壮和灵活，同时也使其更易于阅读和理解...（响应因已达到token限制而被截断。如果需要更长的响应，请尝试增加token限制。）

_表19. 调试和审查Python代码的提示_

太好了。它不仅告诉我如何解决问题，还发现了我的代码中有更多的bug以及如何解决它们。提示的最后部分给出了一般性的建议来改进代码。

---

## 多模态提示

提示代码仍然使用相同的常规大型语言模型。多模态提示是一个单独的问题，它指的是一种使用多种输入格式来引导大型语言模型的技术，而不仅仅依赖于文本。这可以包括文本、图像、音频、代码或甚至其他格式的组合，取决于模型的能力和手头的任务。

---

## 最佳实践

找到正确的提示需要不断调整。Vertex AI中的Language Studio是尝试提示的完美场所，它能够针对各种模型进行测试。

使用以下最佳实践成为提示工程的专家。

### 提供示例

最重要的最佳实践是在提示中提供（一次性/少量）示例。这是非常有效的，因为它充当了强大的教学工具。这些示例展示了期望的输出或类似的响应，让模型从中学习并相应地调整其生成内容。这就像给模型一个参考点或目标，提高其响应的准确性、风格和语调，以更好地匹配您的期望。

### 设计简单性

提示应该简洁、清晰，易于您和模型理解。根据经验，如果它对您来说已经令人困惑，那么对模型来说可能也是如此。尽量不要使用复杂的语言，不要提供不必要的信息。

示例： 之前：

```
我现在正在访问纽约，我想了解更多关于好地方的信息。我带着两个3岁的孩子。在我们的假期里我们应该去哪里？
```

重写后：

```
作为旅游指南。描述纽约曼哈顿适合3岁儿童参观的好地方。
```

尝试使用描述动作的动词。以下是一些例子： Act, Analyze, Categorize, Classify, Contrast, Compare, Create, Describe, Define, Evaluate, Extract, Find, Generate, Identify, List, Measure, Organize, Parse, Pick, Predict, Provide, Rank, Recommend, Return, Retrieve, Rewrite, Select, Show, Sort, Summarize, Translate, Write.

### 明确输出内容

明确说明所需的输出。简洁的指令可能无法足够引导LLM或者太过泛泛。在提示中提供具体细节（通过系统或上下文提示）可以帮助模型专注于相关内容，提高整体准确性。

示例： 应该做：

```
生成一篇关于前5大视频游戏主机的3段博客文章。博客文章应该信息丰富且引人入胜，并且应该以会话风格写作。
```

不应该做：

```
生成一篇关于视频游戏主机的博客文章。
```

### 使用指令而非约束

指令和约束用于提示中以引导LLM的输出。 • 指令提供关于所需格式、风格或内容的明确指示。它指导模型应该做什么或产生什么。 • 约束是对响应的一系列限制或边界。它限制了模型不应该做什么或避免什么。

不断增长的研究表明，在提示中专注于积极指令可能比严重依赖约束更有效。这种方法符合人类更喜欢积极指令而非"不要做什么"列表的偏好。

指令直接传达所需的结果，而约束可能让模型猜测什么是允许的。它给予灵活性并鼓励在定义边界内的创造力，而约束可能限制模型的潜力。此外，约束列表可能相互冲突。

约束在某些情况下仍然有价值。防止模型生成有害或有偏见的内容，或者当需要严格的输出格式或风格时。

如果可能，使用积极指令：不要告诉模型不要做什么，而是告诉它应该做什么。这可以避免混淆并提高输出的准确性。

应该做：

```
生成一篇关于前5大视频游戏主机的1段博客文章。只讨论主机、制造公司、年份和总销量。
```

不应该做：

```
生成一篇关于前5大视频游戏主机的1段博客文章。不要列出视频游戏名称。
```

作为最佳实践，首先优先考虑指令，清楚地说明您希望模型做什么，只在必要时为安全、清晰或特定要求使用约束。尝试和迭代以测试指令和约束的不同组合，找出最适合您特定任务的内容，并记录这些内容。

### 控制最大token长度

要控制生成的LLM响应的长度，您可以在配置中设置最大token限制或在提示中明确请求特定长度。例如：

```
"用推特长度的消息解释量子物理学。"
```

### 在提示中使用变量

为了重复使用提示并使其更加动态，在提示中使用变量，这些变量可以针对不同的输入进行更改。例如，如表20所示，一个提供关于城市事实的提示。不要在提示中硬编码城市名称，而是使用变量。变量可以通过避免重复自己来节省时间和精力。如果您需要在多个提示中使用相同的信息，可以将其存储在变量中，然后在每个提示中引用该变量。这在将提示集成到您自己的应用程序中时特别有意义。

|提示|变量<br>{city} = "Amsterdam"<br><br>提示<br>您是一位旅游指南。告诉我关于城市的事实：{city}|
|---|---|
|输出|Amsterdam是一座充满运河、桥梁和狭窄街道的美丽城市。这是一个很棒的地方，可以参观其丰富的历史、文化和夜生活。|

_表20. 在提示中使用变量_

### 尝试输入格式和写作风格

不同的模型、模型配置、提示格式、词语选择和提交可能产生不同的结果。因此，尝试提示属性如风格、词语选择和提示类型（零样本、少样本、系统提示）很重要。

例如，一个目标是生成关于革命性视频游戏主机Sega Dreamcast的文本的提示，可以表述为问题、陈述或指令，产生不同的输出： • 问题：Sega Dreamcast是什么，为什么它是如此革命性的主机？ • 陈述：Sega Dreamcast是世嘉在1999年发布的第六代视频游戏主机。它... • 指令：写一段描述Sega Dreamcast主机并解释为什么它如此革命性的段落。

### 对于分类任务的少量样本提示，混合类别

一般来说，少量样本示例的顺序应该不太重要。然而，在进行分类任务时，确保混合可能的响应类别在少样本示例中。这是因为您可能否则会过度拟合特定的示例顺序。通过混合可能的响应类别，您可以确保模型学习识别每个类别的关键特征，而不是简单地记住示例的顺序。这将导致对未见数据的更强健和可泛化的性能。

一个好的经验法则是从6个少样本示例开始，然后从那里开始测试准确性。

### 适应模型更新

您要及时了解模型架构变化、添加的数据和功能非常重要。尝试更新的模型版本并调整您的提示以更好地利用新的模型特性。像Vertex AI Studio这样的工具非常适合存储、测试和记录您提示的各种版本。

### 尝试输出格式

除了提示输入格式外，考虑尝试输出格式。对于非创造性任务，如提取、选择、解析、排序、排名或分类数据，尝试以结构化格式如JSON或XML返回输出。

从提取数据的提示中返回JSON对象有一些好处。在实际应用中，我不需要手动创建这个JSON格式，我可以已经以排序顺序返回数据（在处理datetime对象时非常方便），但最重要的是，通过提示JSON格式，它强制模型创建一个结构并限制幻觉。

总之，使用JSON作为输出的好处： • 始终以相同的风格返回 • 专注于您想要接收的数据 • 减少幻觉的机会 • 使其关系感知 • 您获得数据类型 • 您可以对其进行排序

表4在少量样本提示部分展示了如何返回结构化输出的示例。


### JSON修复

虽然以JSON格式返回数据提供了众多优势，但它并非没有缺点。JSON的结构化性质虽然有利于解析和在应用程序中使用，但比纯文本需要更多的tokens，导致处理时间增加和成本提高。此外，JSON的冗长可能会轻易消耗整个输出窗口，特别是当由于token限制而突然截断生成时尤为问题。这种截断通常会导致无效的JSON，缺少关键的右括号或方括号，使输出无法使用。幸运的是，像json-repair库（在PyPI上可用）这样的工具在这些情况下非常宝贵。这个库智能地尝试自动修复不完整或格式错误的JSON对象，使其成为处理LLM生成的JSON时的重要盟友，特别是在处理潜在的截断问题时。

### 使用模式（Schema）

我们已经看到将结构化JSON作为输出是一个很好的解决方案。但输入呢？虽然JSON对于结构化LLM生成的输出非常出色，但它对于结构化您提供的输入也非常有用。这就是JSON模式发挥作用的地方。JSON模式定义了JSON输入的预期结构和数据类型。通过提供模式，您给LLM一个明确的数据蓝图，帮助它将注意力集中在相关信息上并降低误解输入的风险。此外，模式可以帮助建立不同数据间的关系，甚至通过包含特定格式的日期或时间戳字段使LLM"时间感知"。

这里有一个简单的例子：

假设您想使用LLM为电子商务目录中的产品生成描述。不仅仅提供产品的自由格式文本描述，您可以使用JSON模式来定义产品的属性：

```json
{
  "type": "object",
  "properties": {
    "name": { "type": "string", "description": "产品名称" },
    "category": { "type": "string", "description": "产品类别" },
    "price": { "type": "number", "format": "float", "description": "产品价格" },
    "features": {
      "type": "array",
      "items": { "type": "string" },
      "description": "产品的主要特点"
    },
    "release_date": { "type": "string", "format": "date", "description": "产品发布日期"}
  }
}
```

_代码片段5. 结构化输出模式的定义_

然后，您可以提供符合此模式的实际产品数据作为JSON对象：

```json
{
  "name": "无线耳机",
  "category": "电子产品",
  "price": 99.99,
  "features": ["降噪", "蓝牙5.0", "20小时电池寿命"],
  "release_date": "2023-10-27"
}
```

_代码片段6. 来自LLM的结构化输出_

通过预处理您的数据，并且不提供完整文档而只提供模式和数据，您给LLM一个对产品属性的清晰理解，包括其发布日期，使它更有可能生成准确和相关的描述。这种结构化输入方法，引导LLM的注意力到相关字段，在处理大量数据或将LLM集成到复杂应用程序时特别有价值。

### 与其他提示工程师一起实验

如果您处于必须尝试提出一个好提示的情况，您可能想找多人来尝试。当每个人都遵循最佳实践（如本章所列）时，您会看到所有不同提示尝试之间的性能差异。

### CoT最佳实践

对于CoT提示，将答案放在推理之后是必要的，因为生成推理改变了模型在预测最终答案时获得的tokens。

使用CoT和自我一致性时，您需要能够从提示中提取最终答案，与推理分开。

对于CoT提示，将temperature设置为0。

思维链提示基于贪婪解码，基于语言模型分配的最高概率预测序列中的下一个词。一般来说，使用推理得出最终答案时，可能只有一个正确答案。因此，temperature应始终设置为0。

### 记录各种提示尝试

前面在本章中已经提到了最后一个技巧，但我们不能强调足够它的重要性：详细记录您的提示尝试，这样您就可以随时了解什么有效，什么无效。

提示输出可能在不同模型、不同采样设置，甚至相同模型的不同版本之间有所不同。此外，即使对相同模型的相同提示，输出句子格式和词语选择可能也会有细微差异。（例如，如前面提到的，如果两个tokens有相同的预测概率，可能会随机打破平局。这可能会影响后续预测的tokens。）。

我们建议创建一个以表21为模板的Google表格。这种方法的优势是，当您不可避免地不得不重新访问您的提示工作时——无论是在未来拾起它（您会惊讶于在短暂休息后可能忘记多少内容），测试不同模型版本上的提示性能，还是帮助调试未来的错误——您都拥有完整的记录。

除了此表中的字段外，跟踪提示的版本（迭代），一个捕获结果是否"OK/NOT OK/SOMETIMES OK"的字段，以及一个捕获反馈的字段也很有帮助。如果您足够幸运使用Vertex AI Studio，保存您的提示（使用与文档中列出的相同名称和版本）并在表格中跟踪保存提示的超链接。这样，您只需一次点击即可重新运行提示。

在处理检索增强生成系统时，您还应该捕获影响插入到提示中内容的RAG系统的特定方面，包括查询、分块设置、分块输出和其他信息。

一旦您觉得提示接近完美，将其转移到您的项目代码库。在代码库中，将提示保存在与代码分开的文件中，以便更容易维护。最后，理想情况下，您的提示是操作化系统的一部分，作为提示工程师，您应该依靠自动化测试和评估程序来了解您的提示对任务的泛化能力。

提示工程是一个迭代过程。制作和测试不同的提示，分析和记录结果。根据模型的表现调整您的提示。继续实验直到获得所需的输出。当您更改模型或模型配置时，返回并继续使用先前使用的提示进行实验。

| 名称          | [提示的名称和版本]    |
| ----------- | ------------- |
| 目标          | [此尝试目标的一句话解释] |
| 模型          | [使用的模型名称和版本]  |
| Temperature | [0-1之间的值]     |
| Top-K       | [数字]          |
| 提示          | [写出完整提示]      |
| 输出          | [写出输出或多个输出]   |

_表21. 记录提示的模板_

---

## 总结

本白皮书讨论了提示工程。我们学习了各种提示技术，例如：

- 零样本提示
- 少样本提示
- 系统提示
- 角色提示
- 上下文提示
- 后退提示
- 思维链
- 自我一致性
- 思维树
- ReAct

我们甚至研究了如何自动化提示的方法。

白皮书还讨论了生成式AI的挑战，例如提示不足时可能出现的问题。我们以如何成为更好的提示工程师的最佳实践结束。

---

## 尾注

1. Google, 2023, Gemini by Google. 可在以下网址获取：https://gemini.google.com.
2. Google, 2024, Gemini for Google Workspace Prompt Guide. 可在以下网址获取：https://inthecloud.withgoogle.com/gemini-for-google-workspace-prompt-guide/dl-cd.html.
3. Google Cloud, 2023, Introduction to Prompting. 可在以下网址获取：https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design.
4. Google Cloud, 2023, Text Model Request Body: Top-P & top-K sampling methods. 可在以下网址获取：https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text#request_body.
5. Wei, J., et al., 2023, Zero Shot - Fine Tuned language models are zero shot learners. 可在以下网址获取：https://arxiv.org/pdf/2109.01652.pdf.
6. Google Cloud, 2023, Google Cloud Model Garden. 可在以下网址获取：https://cloud.google.com/model-garden.
7. Brown, T., et al., 2023, Few Shot - Language Models are Few Shot learners. 可在以下网址获取：https://arxiv.org/pdf/2005.14165.pdf.
8. Zheng, L., et al., 2023, Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models. 可在以下网址获取：https://openreview.net/pdf?id=3bq3jsvcQ1.
9. Wei, J., et al., 2023, Chain of Thought Prompting. 可在以下网址获取：https://arxiv.org/pdf/2201.11903.pdf.
10. Google Cloud Platform, 2023, Chain of Thought and React. 可在以下网址获取：https://github.com/GoogleCloudPlatform/generative-ai/blob/main/language/prompts/examples/chain_of_thought_react.ipynb.
11. Wang, X., et al., 2023, Self Consistency Improves Chain of Thought reasoning in language models. 可在以下网址获取：https://arxiv.org/pdf/2203.11171.pdf.
12. Yao, S., et al., 2023, Tree of Thoughts: Deliberate Problem Solving with Large Language Models. 可在以下网址获取：https://arxiv.org/pdf/2305.10601.pdf.
13. Yao, S., et al., 2023, ReAct: Synergizing Reasoning and Acting in Language Models. 可在以下网址获取：https://arxiv.org/pdf/2210.03629.pdf.
14. Google Cloud Platform, 2023, Advance Prompting: Chain of Thought and React. 可在以下网址获取：https://github.com/GoogleCloudPlatform/applied-ai-engineering-samples/blob/main/genaion-vertex-ai/advanced_prompting_training/cot_react.ipynb.
15. Zhou, C., et al., 2023, Automatic Prompt Engineering - Large Language Models are Human-Level Prompt Engineers. 可在以下网址获取：https://arxiv.org/pdf/2211.01910.pdf.