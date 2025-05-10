---
title: JWT认证工具
jd_id: node-jwt-auth-001
created: 2025-05-09 09:57
updated: 2025-05-09 09:57
type: snippet
status: active
language: javascript
schema: v1
tags: [lang/javascript, 主题/认证, 主题/安全, 主题/node]
complexity: 3       # 1-5，越高越复杂
reusability: 5      # 1-5，越高越容易复用
performance: 4      # 1-5，越高性能越好
maintainability: 4  # 1-5，越高越容易维护
tested: true        # 是否经过测试
environment: node    # browser/node/all
---

# JWT认证工具

## 📝 概述

JWT（JSON Web Token）是一种用于在网络应用间安全传递声明的开放标准。本代码片段提供了一套完整的JWT工具函数，包括生成token、验证token、刷新token等功能，适用于Node.js后端API的用户认证系统。

## 🧩 代码

```javascript
const jwt = require('jsonwebtoken');
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

/**
 * JWT认证工具类
 */
class JWTAuth {
  /**
   * 初始化JWT工具
   * @param {Object} options - 配置选项
   * @param {string} options.secretKey - 密钥（对称加密时使用）
   * @param {string} options.privateKeyPath - 私钥路径（非对称加密时使用）
   * @param {string} options.publicKeyPath - 公钥路径（非对称加密时使用）
   * @param {string} options.algorithm - 加密算法，默认为HS256
   * @param {number} options.expiresIn - 过期时间（秒），默认为1小时
   * @param {number} options.refreshExpiresIn - 刷新token过期时间（秒），默认为7天
   * @param {string} options.issuer - 签发者
   */
  constructor(options = {}) {
    this.options = {
      algorithm: 'HS256',
      expiresIn: 60 * 60, // 1小时
      refreshExpiresIn: 60 * 60 * 24 * 7, // 7天
      issuer: 'api-service',
      ...options
    };

    // 根据算法选择加密方式
    if (this.options.algorithm.startsWith('HS')) {
      if (!this.options.secretKey) {
        throw new Error('对称加密算法需要提供secretKey');
      }
      this.secretOrPrivateKey = this.options.secretKey;
      this.publicKey = this.options.secretKey;
    } else if (this.options.algorithm.startsWith('RS') || this.options.algorithm.startsWith('ES')) {
      if (!this.options.privateKeyPath || !this.options.publicKeyPath) {
        throw new Error('非对称加密算法需要提供privateKeyPath和publicKeyPath');
      }
      this.secretOrPrivateKey = fs.readFileSync(path.resolve(this.options.privateKeyPath));
      this.publicKey = fs.readFileSync(path.resolve(this.options.publicKeyPath));
    } else {
      throw new Error(`不支持的算法: ${this.options.algorithm}`);
    }

    // 用于存储无效token的集合
    this.blacklist = new Set();
  }

  /**
   * 生成访问令牌
   * @param {Object} payload - 要编码到令牌中的数据
   * @returns {string} 生成的JWT令牌
   */
  generateToken(payload) {
    const token = jwt.sign(payload, this.secretOrPrivateKey, {
      algorithm: this.options.algorithm,
      expiresIn: this.options.expiresIn,
      issuer: this.options.issuer,
      jwtid: crypto.randomBytes(16).toString('hex') // 添加唯一ID，用于吊销
    });
    return token;
  }

  /**
   * 生成刷新令牌
   * @param {Object} payload - 要编码到令牌中的数据
   * @returns {string} 生成的刷新令牌
   */
  generateRefreshToken(payload) {
    // 刷新令牌中只存储最小必要信息
    const refreshPayload = {
      userId: payload.userId,
      type: 'refresh'
    };

    const refreshToken = jwt.sign(refreshPayload, this.secretOrPrivateKey, {
      algorithm: this.options.algorithm,
      expiresIn: this.options.refreshExpiresIn,
      issuer: this.options.issuer,
      jwtid: crypto.randomBytes(16).toString('hex')
    });

    return refreshToken;
  }

  /**
   * 验证令牌
   * @param {string} token - 要验证的JWT令牌
   * @returns {Object|false} 解码后的payload或验证失败返回false
   */
  verifyToken(token) {
    try {
      // 检查黑名单
      if (this.blacklist.has(token)) {
        return false;
      }

      const decoded = jwt.verify(token, this.publicKey, {
        algorithms: [this.options.algorithm],
        issuer: this.options.issuer
      });

      return decoded;
    } catch (error) {
      console.error('Token验证失败:', error.message);
      return false;
    }
  }

  /**
   * 刷新访问令牌
   * @param {string} refreshToken - 刷新令牌
   * @returns {Object|false} 包含新访问令牌和刷新令牌的对象，或验证失败返回false
   */
  refreshAccessToken(refreshToken) {
    const decoded = this.verifyToken(refreshToken);
    
    if (!decoded || decoded.type !== 'refresh') {
      return false;
    }

    // 创建新的访问令牌
    const newPayload = {
      userId: decoded.userId
    };

    const accessToken = this.generateToken(newPayload);
    const newRefreshToken = this.generateRefreshToken(newPayload);

    return {
      accessToken,
      refreshToken: newRefreshToken,
      expiresIn: this.options.expiresIn
    };
  }

  /**
   * 吊销令牌（添加到黑名单）
   * @param {string} token - 要吊销的令牌
   * @returns {boolean} 是否成功吊销
   */
  revokeToken(token) {
    try {
      // 验证令牌是否有效
      const decoded = jwt.decode(token);
      if (!decoded) {
        return false;
      }

      // 加入黑名单
      this.blacklist.add(token);
      
      // 注意：在生产环境中应该使用Redis等持久化存储黑名单
      
      return true;
    } catch (error) {
      console.error('Token吊销失败:', error.message);
      return false;
    }
  }

  /**
   * 从请求头中提取令牌
   * @param {Object} req - Express请求对象
   * @returns {string|null} 提取的令牌或null
   */
  extractTokenFromHeader(req) {
    if (!req.headers.authorization) {
      return null;
    }

    const parts = req.headers.authorization.split(' ');
    if (parts.length !== 2 || parts[0] !== 'Bearer') {
      return null;
    }

    return parts[1];
  }

  /**
   * 清理过期的黑名单令牌（在生产环境中应定期执行）
   */
  cleanupBlacklist() {
    const now = Math.floor(Date.now() / 1000);
    this.blacklist.forEach(token => {
      try {
        const decoded = jwt.decode(token);
        if (decoded && decoded.exp < now) {
          this.blacklist.delete(token);
        }
      } catch (error) {
        // 无效token直接移除
        this.blacklist.delete(token);
      }
    });
  }
}

module.exports = JWTAuth;
```

## 🚀 使用示例

### 基本使用（Express中间件）

```javascript
const express = require('express');
const JWTAuth = require('./jwt-auth');
const app = express();

// 初始化JWT工具
const jwtAuth = new JWTAuth({
  secretKey: 'your-super-secret-key-should-be-very-long',
  expiresIn: 3600, // 1小时
});

// 登录接口
app.post('/api/login', (req, res) => {
  // 这里应该有验证用户名密码的逻辑
  const user = { userId: '123', username: 'test_user', role: 'admin' };
  
  // 生成访问令牌和刷新令牌
  const accessToken = jwtAuth.generateToken(user);
  const refreshToken = jwtAuth.generateRefreshToken(user);
  
  res.json({
    accessToken,
    refreshToken,
    expiresIn: 3600
  });
});

// 认证中间件
const authenticate = (req, res, next) => {
  const token = jwtAuth.extractTokenFromHeader(req);
  
  if (!token) {
    return res.status(401).json({ message: '未提供认证令牌' });
  }
  
  const decoded = jwtAuth.verifyToken(token);
  if (!decoded) {
    return res.status(401).json({ message: '认证失败或令牌已过期' });
  }
  
  // 将用户信息添加到请求对象
  req.user = decoded;
  next();
};

// 受保护的接口
app.get('/api/protected', authenticate, (req, res) => {
  res.json({
    message: '认证成功',
    user: req.user
  });
});

// 刷新令牌接口
app.post('/api/refresh-token', (req, res) => {
  const { refreshToken } = req.body;
  
  if (!refreshToken) {
    return res.status(400).json({ message: '未提供刷新令牌' });
  }
  
  const tokens = jwtAuth.refreshAccessToken(refreshToken);
  if (!tokens) {
    return res.status(401).json({ message: '刷新令牌无效或已过期' });
  }
  
  res.json(tokens);
});

// 登出接口
app.post('/api/logout', authenticate, (req, res) => {
  const token = jwtAuth.extractTokenFromHeader(req);
  jwtAuth.revokeToken(token);
  
  res.json({ message: '成功登出' });
});

app.listen(3000, () => {
  console.log('服务器运行在 http://localhost:3000');
});
```

### 非对称加密（使用公钥/私钥）

```javascript
// 先生成密钥对:
// openssl genrsa -out private.key 2048
// openssl rsa -in private.key -pubout -out public.key

const jwtAuth = new JWTAuth({
  algorithm: 'RS256',
  privateKeyPath: './keys/private.key',
  publicKeyPath: './keys/public.key',
  expiresIn: 3600
});

// 之后使用方式与基本示例相同
```

## 📊 参数说明

### 构造函数参数

| 参数名 | 类型 | 默认值 | 必填 | 描述 |
|-------|------|-------|------|------|
| options | Object | {} | ❌ | 配置选项 |
| options.secretKey | String | - | 视算法而定 | 密钥（对称加密时必填） |
| options.privateKeyPath | String | - | 视算法而定 | 私钥路径（非对称加密时必填） |
| options.publicKeyPath | String | - | 视算法而定 | 公钥路径（非对称加密时必填） |
| options.algorithm | String | 'HS256' | ❌ | 加密算法 |
| options.expiresIn | Number | 3600 | ❌ | 令牌有效期（秒） |
| options.refreshExpiresIn | Number | 604800 | ❌ | 刷新令牌有效期（秒） |
| options.issuer | String | 'api-service' | ❌ | 令牌发行者 |

### 方法参数

#### generateToken(payload)

| 参数名 | 类型 | 默认值 | 必填 | 描述 |
|-------|------|-------|------|------|
| payload | Object | - | ✅ | 要编码到令牌中的数据 |

#### verifyToken(token)

| 参数名 | 类型 | 默认值 | 必填 | 描述 |
|-------|------|-------|------|------|
| token | String | - | ✅ | 要验证的JWT令牌 |

## 📋 返回值

### generateToken(payload)

| 类型 | 描述 |
|------|------|
| String | 生成的JWT令牌 |

### verifyToken(token)

| 类型 | 描述 |
|------|------|
| Object/false | 解码后的payload或验证失败返回false |

### refreshAccessToken(refreshToken)

| 类型 | 描述 |
|------|------|
| Object/false | 包含新accessToken和refreshToken的对象，或失败返回false |

## ⚠️ 注意事项

- 在生产环境中，应使用更长的密钥和非对称加密算法（如RS256）
- 令牌黑名单应使用Redis等持久化存储，而不是内存中的Set
- 不要在令牌中存储敏感信息，因为JWT可以被解码（但不能被篡改）
- 刷新令牌应存储在安全的位置，如HTTP-only cookie
- 定期清理黑名单中的过期令牌，避免内存泄漏
- 考虑在生产环境中使用专门的认证服务，如Auth0、Okta等

## 🔍 工作原理

JWT由三部分组成：头部（Header）、载荷（Payload）和签名（Signature）。

1. **头部**包含令牌类型和签名算法
2. **载荷**包含声明（如用户信息、过期时间等）
3. **签名**用于验证令牌的完整性和真实性

本工具通过`jsonwebtoken`库实现JWT的生成和验证，同时添加了刷新令牌和令牌吊销功能，使其适用于完整的认证系统。

## 🔄 替代方案

- **Passport.js**：提供多种认证策略的认证中间件
- **OAuth2**：更完整的授权框架，适用于跨服务认证
- **Session-based Auth**：基于会话的传统认证方式
- **Auth0/Okta**：专业的第三方认证服务

## 📚 相关代码片段

- [[Express错误处理中间件]]
- [[密码哈希与比对]]
- [[CORS配置]]

## 🔗 相关概念

- [[认证与授权]]
- [[非对称加密]]
- [[OAuth2认证流程]]

## 📖 参考资料

- [JWT官方文档](https://jwt.io/introduction)
- [jsonwebtoken库文档](https://github.com/auth0/node-jsonwebtoken)
- [JWT安全最佳实践](https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/)

## 📝 使用情境

- RESTful API身份验证
- 单页应用(SPA)认证
- 微服务之间的认证
- 跨域认证
- 移动应用API认证

## 🏷️ 修改历史

- 2025-05-09 - 创建初始版本 