# A股股票K线分析应用

MFE5150 FDA Web App Demo - 一个用于分析A股股票K线数据的Web应用

## 📋 项目概述

本项目提供两种部署方式，让用户无需安装Python或配置环境即可使用股票分析功能：

1. **Streamlit版本** - 功能完整的Python应用，部署在Streamlit Community Cloud
2. **HTML版本** - 纯前端应用，部署在GitHub Pages

## 🚀 部署方式

### 方式一：Streamlit Community Cloud部署（推荐用于完整功能）

#### 步骤1：准备GitHub仓库

1. 在GitHub上创建一个新的公开仓库
2. 将以下文件推送到仓库：
   - `streamlit_app.py` - Streamlit应用主文件
   - `requirements.txt` - Python依赖包
   - `.streamlit/config.toml` - Streamlit配置文件

#### 步骤2：部署到Streamlit Community Cloud

1. 访问 [Streamlit Community Cloud](https://share.streamlit.io/)
2. 点击 "New app"
3. 连接你的GitHub账户
4. 选择刚才创建的仓库
5. 选择 `streamlit_app.py` 作为主文件
6. 点击 "Deploy"

#### 步骤3：等待部署完成

- 部署通常需要1-3分钟
- 完成后你会获得一个分享链接（如：`https://your-app-name.streamlit.app`）

### 方式二：GitHub Pages部署（推荐用于快速访问）

#### 步骤1：准备GitHub仓库

1. 在GitHub上创建一个新的公开仓库
2. 将 `index.html` 文件推送到仓库根目录

#### 步骤2：启用GitHub Pages

1. 进入仓库的 **Settings** 页面
2. 在左侧菜单中找到 **Pages**
3. 在 **Source** 下拉菜单中选择 **Deploy from a branch**
4. 选择 **main** 分支和 **/ (root)** 目录
5. 点击 **Save**

#### 步骤3：等待部署完成

- 部署通常需要1-2分钟
- 完成后访问 `https://your-username.github.io/your-repo-name/`

## 📦 项目文件说明

### Streamlit版本文件

- **streamlit_app.py** - Streamlit应用主文件，包含完整的股票分析功能
- **requirements.txt** - Python依赖包列表
- **.streamlit/config.toml** - Streamlit应用配置

### HTML版本文件

- **index.html** - 独立的HTML文件，包含所有前端逻辑和样式

## 💻 本地运行

### 运行Streamlit版本

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行应用：
```bash
streamlit run streamlit_app.py
```

3. 在浏览器中打开 `http://localhost:8501`

### 运行HTML版本

直接在浏览器中打开 `index.html` 文件即可

## 🎯 功能特性

### Streamlit版本
- ✅ 实时获取A股股票数据
- ✅ 交互式K线图（使用Plotly）
- ✅ 数据统计显示
- ✅ CSV数据下载
- ✅ 响应式设计

### HTML版本
- ✅ 模拟股票数据（用于演示）
- ✅ 交互式K线图（使用ECharts）
- ✅ 数据统计显示
- ✅ CSV数据下载
- ✅ 完全离线可用
- ✅ 无需后端服务器

## 📊 数据来源

- **Streamlit版本**：使用akshare库获取实时A股数据
- **HTML版本**：使用模拟数据演示功能（适合教学和演示）

## 🔧 技术栈

### Streamlit版本
- Python 3.x
- Streamlit
- akshare
- pandas
- plotly

### HTML版本
- HTML5
- CSS3
- JavaScript
- ECharts

## 📝 使用说明

1. 输入A股股票代码（如：600000、000001等）
2. 点击"查询"按钮获取数据
3. 查看K线图和数据统计
4. 可以下载CSV格式的原始数据

## 🌐 分享链接

部署完成后，你可以将以下链接分享给他人：

- **Streamlit版本**：`https://your-app-name.streamlit.app`
- **HTML版本**：`https://your-username.github.io/your-repo-name/`

## 📚 注意事项

1. Streamlit版本需要网络连接以获取实时数据
2. HTML版本使用模拟数据，适合演示和教学
3. 两个版本都支持在移动设备上访问
4. 无需用户安装任何软件或配置环境

## 🤝 贡献

欢迎提交问题和改进建议！

## 📄 许可证

MIT License

## 👨‍💻 作者

MFE5150 FDA Web App Demo
