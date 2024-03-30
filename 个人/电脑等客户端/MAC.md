## 外挂硬盘

MacOS 外挂硬盘，需要对硬盘进行分区时应该使用哪种格式来格式化？分区工具又有哪些呢？

分区工具：
- 使用 mac 自带的`磁盘工具`

分区格式：
- Mac OS 拓展：macOS Sierra 以及更早版本的默认文件系统，是旧版系统文件系统。
- APFS：mac 最新的文件系统格式，用来替代Mac OS 拓展；缺点是不兼容 2017 年前的机器。
- ExFAT：如果想在 macOS 和 windows 之间拷贝数据时，选用这种格式。
- 其他常用格式：
	- FAT32: U盘常用格式，可以在任何系统上使用，缺点是单文件最大容量为4GB，传输大文件弊端明显。
	- ExFAT：微软创建用来取代FAT32的格式，单文件支持到1EB，非常适合大文件，Mac也可以使用；缺点是没有文件日志功能，这样就不能记录磁盘文件的修改记录，嗯 会有数据丢失的风险。
	- NTFS：微软创建的格式，没有文件大小限制，支持日志功能，缺点是在mac系统只能读取，想要写入需要第三方工具才能实现。

也就是说2019年现在往后主流使用的格式这3种，他们特点是。

**·APFS**：优点：可靠，安全。对配合苹果电脑使用友好。缺点：不兼容Windows系统。

**·NTFS**：优点：采用日志式，稳定安全，Windows系统使用友好，是主流格式。缺点：苹果电脑只支持读，想要写需要买驱动软件。

**·ExFAT**：优点：对Windows和MAC格式都兼容，对[闪存SSD硬盘](https://www.zhihu.com/search?q=%E9%97%AA%E5%AD%98SSD%E7%A1%AC%E7%9B%98&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A908644008%7D)优化更好。缺点：机械硬盘用这格式数据容易丢。

### 总结：
不考虑 windows 直接使用 APFS 格式
考虑 windows 一部分APFS或者NTFS格式，也可以再加一个 ExFAT 做紧急中转
只考虑 windows 使用 NTFS 格式