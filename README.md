# Platform Intelligence

追踪 B站花火、巨量星图、小红书蒲公英、快手磁力聚星 的最新动态与市场洞察。

## 功能特性

- 📊 **竞争矩阵** - 四平台8维度综合评分对比
- 📰 **实时动态** - 各平台最新新闻和公告聚合
- 💬 **用户反馈** - 创作者真实使用体验
- 🔄 **每日自动更新** - 北京时间每天 11:00 自动抓取最新数据

## 快速部署

### 方法一：GitHub Pages（推荐，免费）

1. **创建 GitHub 仓库**
   - 点击 [github.com/new](https://github.com/new)
   - 仓库名：`platform-intelligence`（或你喜欢的名字）
   - 选择 **Public**
   - 不要勾选任何初始化选项

2. **推送代码到仓库**
   ```bash
   cd /Users/zhangjinwei/WorkBuddy/20260327105655
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/platform-intelligence.git
   git branch -M main
   git push -u origin main
   ```

3. **启用 GitHub Pages**
   - 进入仓库 → Settings → Pages
   - Source 选择 `Deploy from a branch`
   - Branch 选择 `main`，文件夹选择 `/ (root)`
   - 点击 Save

4. **等待部署完成**
   - 几分钟后访问：`https://YOUR_USERNAME.github.io/platform-intelligence`

5. **启用自动更新**
   - 第一次 push 后，GitHub Actions 会自动运行
   - 之后每天 11:00（北京时间）会自动更新数据

### 方法二：Vercel（替代方案）

1. 将代码推送到 GitHub
2. 注册 [vercel.com](https://vercel.com)
3. 点击 "New Project" → 导入你的 GitHub 仓库
4. Deploy 完成，获得一个 `.vercel.app` 域名

## 自定义域名（可选）

如果你有自己的域名：

### GitHub Pages
1. 仓库 Settings → Pages → Custom domain
2. 输入你的域名（如 `platform.yourcompany.com`）
3. 在你的域名服务商处添加 CNAME 记录

### Vercel
域名会自动配置 HTTPS，无需额外操作。

## 更新数据

### 自动更新
已配置 GitHub Actions，每天北京时间 11:00 自动运行。

### 手动更新
```bash
python crawler.py
```

### 添加/修改新闻
编辑 `crawler.py` 中的 `DATA_SOURCE` 字典，添加对应平台的新闻数据。

## 项目结构

```
├── index.html          # 主页面
├── crawler.py          # 数据爬虫脚本
├── requirements.txt    # Python 依赖
├── data.json           # 生成的 JSON 数据
├── .github/
│   └── workflows/
│       └── daily-update.yml  # GitHub Actions 配置
└── README.md
```

## 技术栈

- HTML5 + CSS3 + Vanilla JavaScript
- 无需后端，纯静态部署
- Google Fonts (Inter)
- SVG 图标

---

Powered by WorkBuddy Agent · 2026
