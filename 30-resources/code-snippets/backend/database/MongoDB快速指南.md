---
title: MongoDB快速指南
created: {{date:YYYY-MM-DD HH:mm}}
updated: {{date:YYYY-MM-DD HH:mm}}
type: note
status: active
schema: v1
tags: [topic/backend, topic/database, topic/mongodb, topic/nosql, action/reference]
---

# MongoDB快速指南

## 基本概念

MongoDB是一个文档型NoSQL数据库，使用JSON格式存储数据。

- **数据库(Database)**: 包含多个集合的物理容器
- **集合(Collection)**: 类似关系型数据库中的表
- **文档(Document)**: 类似关系型数据库中的行，以BSON格式存储
- **字段(Field)**: 类似关系型数据库中的列

## 基本CRUD操作

### 创建(Create)

```javascript
// 插入单个文档
db.collection.insertOne({
  name: "John",
  age: 30,
  email: "john@example.com"
})

// 插入多个文档
db.collection.insertMany([
  { name: "Alice", age: 25, email: "alice@example.com" },
  { name: "Bob", age: 35, email: "bob@example.com" }
])
```

### 读取(Read)

```javascript
// 查询所有文档
db.collection.find()

// 条件查询
db.collection.find({ age: { $gt: 25 } })

// 投影（只返回特定字段）
db.collection.find({}, { name: 1, email: 1, _id: 0 })

// 限制结果数量
db.collection.find().limit(10)

// 跳过结果
db.collection.find().skip(10)

// 排序
db.collection.find().sort({ age: 1 }) // 1升序，-1降序

// 计数
db.collection.countDocuments({ age: { $gt: 25 } })

// 查找单个文档
db.collection.findOne({ name: "John" })
```

### 更新(Update)

```javascript
// 更新单个文档
db.collection.updateOne(
  { name: "John" },
  { $set: { age: 31, status: "active" } }
)

// 更新多个文档
db.collection.updateMany(
  { age: { $gt: 25 } },
  { $set: { status: "active" } }
)

// 替换整个文档
db.collection.replaceOne(
  { name: "John" },
  { name: "John Doe", age: 31, email: "john.doe@example.com" }
)

// 更新操作符
$set        // 设置字段值
$inc        // 增加数值
$push       // 添加到数组
$pull       // 从数组移除
$addToSet   // 添加到数组（如果不存在）
$unset      // 移除字段
```

### 删除(Delete)

```javascript
// 删除单个文档
db.collection.deleteOne({ name: "John" })

// 删除多个文档
db.collection.deleteMany({ age: { $lt: 25 } })

// 删除集合中所有文档
db.collection.deleteMany({})

// 删除集合
db.collection.drop()

// 删除数据库
db.dropDatabase()
```

## 高级查询

### 查询操作符

```javascript
// 比较操作符
$eq         // 等于
$ne         // 不等于
$gt         // 大于
$gte        // 大于等于
$lt         // 小于
$lte        // 小于等于
$in         // 在指定数组中
$nin        // 不在指定数组中

// 例子
db.collection.find({ age: { $gt: 25, $lt: 50 } })
db.collection.find({ status: { $in: ["active", "pending"] } })

// 逻辑操作符
$and        // 与
$or         // 或
$not        // 非
$nor        // 都不

// 例子
db.collection.find({
  $or: [
    { age: { $lt: 25 } },
    { status: "active" }
  ]
})

// 元素操作符
$exists     // 字段存在
$type       // 字段类型

// 例子
db.collection.find({ email: { $exists: true } })
db.collection.find({ age: { $type: "number" } })

// 数组操作符
$all        // 包含所有指定元素
$elemMatch  // 匹配数组中的元素
$size       // 数组大小

// 例子
db.collection.find({ tags: { $all: ["mongodb", "database"] } })
db.collection.find({ scores: { $elemMatch: { $gt: 80, $lt: 90 } } })
```

### 聚合操作

```javascript
// 聚合管道
db.collection.aggregate([
  { $match: { age: { $gt: 25 } } },           // 筛选
  { $group: { _id: "$status", count: { $sum: 1 } } }, // 分组
  { $sort: { count: -1 } }                    // 排序
])

// 常用聚合操作符
$match      // 筛选文档
$group      // 分组
$project    // 投影
$sort       // 排序
$limit      // 限制结果数量
$skip       // 跳过结果
$unwind     // 展开数组
$lookup     // 连接（类似SQL JOIN）

// 计算平均值
db.collection.aggregate([
  { $group: { _id: null, avgAge: { $avg: "$age" } } }
])

// 查找最大值最小值
db.collection.aggregate([
  { $group: { 
      _id: null, 
      maxAge: { $max: "$age" },
      minAge: { $min: "$age" }
    } 
  }
])

// 分组计数
db.collection.aggregate([
  { $group: { _id: "$status", count: { $sum: 1 } } }
])
```

## 索引

```javascript
// 创建单字段索引
db.collection.createIndex({ age: 1 }) // 1升序，-1降序

// 创建复合索引
db.collection.createIndex({ name: 1, age: -1 })

// 创建唯一索引
db.collection.createIndex({ email: 1 }, { unique: true })

// 创建文本索引
db.collection.createIndex({ description: "text" })

// 创建地理空间索引
db.collection.createIndex({ location: "2dsphere" })

// 查看集合的索引
db.collection.getIndexes()

// 删除索引
db.collection.dropIndex("index_name")
```

## 数据建模

### 嵌入式文档模型

```javascript
// 嵌入式文档（适合一对一或一对少量关系）
db.users.insertOne({
  name: "John",
  contact: {
    email: "john@example.com",
    phone: "123-456-7890",
    address: {
      street: "123 Main St",
      city: "New York",
      zip: "10001"
    }
  },
  orders: [
    { id: "001", product: "Laptop", price: 1200 },
    { id: "002", product: "Phone", price: 800 }
  ]
})
```

### 引用模型

```javascript
// 引用模型（适合一对多或多对多关系）
db.customers.insertOne({
  _id: ObjectId("5f8d0f5b2b0c9ae6b4a2c7a1"),
  name: "John",
  email: "john@example.com"
})

db.orders.insertMany([
  { 
    customer_id: ObjectId("5f8d0f5b2b0c9ae6b4a2c7a1"),
    product: "Laptop",
    price: 1200
  },
  { 
    customer_id: ObjectId("5f8d0f5b2b0c9ae6b4a2c7a1"),
    product: "Phone",
    price: 800
  }
])

// 使用$lookup进行连接查询
db.customers.aggregate([
  { $match: { name: "John" } },
  { $lookup: {
      from: "orders",
      localField: "_id",
      foreignField: "customer_id",
      as: "orders"
    }
  }
])
```

## 最佳实践

1. **适当使用索引**：为常用查询添加索引，但避免过多索引
2. **选择合适的数据模型**：根据查询模式选择嵌入或引用
3. **限制嵌入文档大小**：MongoDB文档最大16MB
4. **批量操作**：使用批量插入/更新提高性能
5. **使用投影**：只返回需要的字段
6. **考虑分片**：对大规模数据使用分片
7. **定期备份**：实施可靠的备份策略

## 相关链接

- [[MongoDB参考]] - 详细的MongoDB使用文档
- [[MongoDB与Node.js]] - MongoDB与Node.js集成指南
- [[NoSQL数据库比较]] - 各种NoSQL数据库的对比 