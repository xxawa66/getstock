# 部署指南 - A股股票K线分析应用

本指南将帮助你将股票分析应用部署到云端，让任何人都可以通过一个链接访问。

## 📋 部署前准备

1. **GitHub账户**：如果你还没有GitHub账户，请先注册一个（免费）
2. **项目文件**：确保你已经准备好了以下文件：
   - `streamlit_app.py`
   - `requirements.txt`
   - `.streamlit/config.toml`
   - `index.html`
   - `README.md`

---

## 🚀 方式一：Streamlit Community Cloud部署

### 优势
- ✅ 功能完整，获取实时股票数据
- ✅ 专业的Python后端支持
- ✅ 自动部署和更新
- ✅ 免费使用

### 步骤1：创建GitHub仓库

1. 访问 [GitHub](https://github.com/) 并登录
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 填写仓库信息：
   - **Repository name**：例如 `stock-analysis-app`
   - **Description**：例如 "A股股票K线分析应用"
   - 选择 **Public**（公开仓库）
4. 点击 "Create repository"

### 步骤2：上传文件到GitHub

#### 方法A：使用GitHub网页界面上传（推荐新手）

1. 在新创建的仓库页面，点击 "uploading an existing file"
2. 将以下文件拖拽到上传区域：
   - `streamlit_app.py`
   - `requirements.txt`
   - `.streamlit/config.toml`
   - `README.md`
3. 在底部填写提交信息：
   - "Add files via upload"
4. 点击 "Commit changes"

#### 方法B：使用Git命令行（推荐有经验的用户）

```bash
# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit"

# 添加远程仓库（替换YOUR_USERNAME和REPO_NAME）
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

### 步骤3：部署到Streamlit Community Cloud

1. 访问 [Streamlit Community Cloud](https://share.streamlit.io/)
2. 点击右上角的 "Sign in"，选择使用GitHub账户登录
3. 登录后，点击 "New app" 按钮
4. 填写部署信息：
   - **Repository**：选择你刚才创建的仓库
   - **Branch**：选择 `main`
   - **Main file path**：输入 `streamlit_app.py`
   - **App URL**：输入你的应用名称（如：`stock-analysis-app`）
5. 点击 "Deploy" 按钮

### 步骤4：等待部署完成

- 部署过程通常需要1-3分钟
- 你可以看到实时的部署日志
- 部署成功后，你会看到类似这样的链接：
  ```
  https://stock-analysis-app.streamlit.app
  ```

### 步骤5：测试应用

1. 点击部署完成后的链接
2. 输入股票代码（如：600000）
3. 点击"查询"按钮
4. 查看K线图和数据

### 更新应用

当你修改代码后：

1. 将更改推送到GitHub
2. Streamlit会自动检测并重新部署
3. 通常1-2分钟后更新完成

---

## 🌐 方式二：GitHub Pages部署

### 优势
- ✅ 完全免费
- ✅ 无需配置服务器
- ✅ 部署速度快
- ✅ 支持自定义域名
- ✅ 无需Python环境

### 步骤1：创建GitHub仓库

1. 访问 [GitHub](https://github.com/) 并登录
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 填写仓库信息：
   - **Repository name**：例如 `stock-analysis-html`
   - **Description**：例如 "A股股票K线分析 - HTML版本"
   - 选择 **Public**（公开仓库）
4. 点击 "Create repository"

### 步骤2：上传HTML文件

#### 方法A：使用GitHub网页界面上传（推荐新手）

1. 在新创建的仓库页面，点击 "uploading an existing file"
2. 将 `index.html` 文件拖拽到上传区域
3. 在底部填写提交信息：
   - "Add index.html"
4. 点击 "Commit changes"

#### 方法B：使用Git命令行

```bash
# 初始化Git仓库
git init

# 添加HTML文件
git add index.html

# 提交更改
git commit -m "Add index.html"

# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# 推送到GitHub
git branch -M main
git push -u origin main
```

### 步骤3：启用GitHub Pages

1. 进入你的GitHub仓库
2. 点击顶部的 **Settings** 标签
3. 在左侧菜单中向下滚动，找到 **Pages**（在 "Code and automation" 部分）
4. 在 **Build and deployment** 部分：
   - **Source**：选择 `Deploy from a branch`
   - **Branch**：选择 `main` 分支
   - **Folder**：选择 `/ (root)` 目录
5. 点击 **Save** 按钮

### 步骤4：等待部署完成

- 部署过程通常需要1-2分钟
- 在Pages设置页面，你会看到部署状态
- 部署成功后，你会看到类似这样的链接：
  ```
  https://YOUR_USERNAME.github.io/REPO_NAME/
  ```

### 步骤5：测试应用

1. 点击部署完成后的链接
2. 输入股票代码（如：600000）
3. 点击"查询"按钮
4. 查看K线图和数据

### 更新应用

当你修改HTML文件后：

1. 将更改推送到GitHub
2. GitHub Pages会自动检测并重新部署
3. 通常1-2分钟后更新完成

---

## 🔗 分享你的应用

部署完成后，你可以将链接分享给任何人：

### Streamlit版本链接格式
```
https://your-app-name.streamlit.app
```

### GitHub Pages版本链接格式
```
https://your-username.github.io/your-repo-name/
```

### 分享方式

1. **直接分享链接**：复制链接发送给他人
2. **嵌入到网站**：使用iframe嵌入到其他网站
3. **社交媒体**：发布到微信、微博等平台
4. **文档中引用**：在README或文档中添加链接

---

## 📊 两种方式对比

| 特性 | Streamlit版本 | GitHub Pages版本 |
|------|--------------|-----------------|
| 功能完整性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 实时数据 | ✅ | ❌（模拟数据） |
| 部署难度 | 中等 | 简单 |
| 访问速度 | 中等 | 快 |
| 免费额度 | 充足 | 无限制 |
| 需要Python | 是 | 否 |
| 适合场景 | 生产环境 | 演示/教学 |

---

## 🛠️ 故障排除

### Streamlit部署问题

**问题：部署失败**
- 检查 `requirements.txt` 文件是否正确
- 确保所有依赖包都列在文件中
- 查看Streamlit的部署日志

**问题：应用运行缓慢**
- 减少数据量
- 优化代码逻辑
- 考虑使用缓存

**问题：数据获取失败**
- 检查网络连接
- 确认akshare库版本
- 查看错误日志

### GitHub Pages部署问题

**问题：页面无法访问**
- 确保仓库是公开的
- 检查Pages设置是否正确
- 等待部署完成

**问题：404错误**
- 确认文件名是 `index.html`
- 检查文件是否在根目录
- 清除浏览器缓存

**问题：样式显示异常**
- 检查HTML文件是否完整
- 确认CDN链接是否可访问
- 尝试使用不同的浏览器

---

## 📚 进阶配置

### 自定义域名（GitHub Pages）

1. 在你的域名DNS设置中添加CNAME记录：
   ```
   CNAME  your-username.github.io
   ```
2. 在GitHub仓库的Pages设置中添加自定义域名
3. 等待DNS生效（通常需要24-48小时）

### Streamlit应用配置

编辑 `.streamlit/config.toml` 文件来自定义：
- 主题颜色
- 字体设置
- 服务器配置
- 安全设置

### 添加分析统计

使用Google Analytics或其他分析工具来跟踪访问量：

**对于GitHub Pages：**
```html
<!-- 在index.html的<head>标签中添加 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

---

## 🎯 最佳实践

1. **版本控制**：使用Git管理代码版本
2. **文档完善**：保持README文件更新
3. **定期更新**：及时更新依赖包
4. **性能优化**：优化加载速度和响应时间
5. **错误处理**：添加友好的错误提示
6. **安全考虑**：不要在代码中暴露敏感信息

---

## 📞 获取帮助

如果遇到问题：

1. 查看 [Streamlit文档](https://docs.streamlit.io/)
2. 查看 [GitHub Pages文档](https://docs.github.com/en/pages)
3. 在GitHub上提交Issue
4. 搜索相关问题的解决方案

---

## 🎉 完成！

恭喜你成功部署了股票分析应用！现在你可以：

- 分享链接给朋友和同事
- 在演示中使用这个应用
- 继续开发和改进功能
- 收集用户反馈

祝使用愉快！🚀
