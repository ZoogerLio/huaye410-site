# Personal Academic Homepage

这是一个使用 Astro 制作的静态个人学术主页。日常更新主要集中在：

```text
content/          个人资料、论文、项目和经历
public/images/    照片和背景图
```

通常不需要修改 `src/` 中的网页代码。

## 本地预览

先安装 [Node.js](https://nodejs.org/)，然后在项目目录运行：

```bash
npm install
npm run dev
```

终端会显示本地网址，通常是 `http://localhost:4321/`。按住 `Control` 并点击网址即可打开。

发布前可以运行：

```bash
npm run build
```

## 修改个人简介

打开 `content/profile.yaml`。

- `name`：姓名
- `role`：当前身份
- `affiliation`：学校或机构
- `introduction`：用于搜索引擎和网页简介的一句话
- `biography`：Biography 段落；每个以 `-` 开头的项目是一段
- `email`、`location`：邮箱和所在地

YAML 对缩进敏感，请保留现有的两个空格缩进。包含冒号的长文本建议保留双引号。

## 修改 Research Interests

在 `content/profile.yaml` 中找到 `interests`：

```yaml
interests:
  - title: "Human-Centered AI"
    description: "A short explanation of this research area."
```

复制整个 `- title` 条目即可增加方向；删除整个条目即可移除。

## 添加 Publication

打开 `content/publications.yaml`，复制以下内容并粘贴到文件末尾：

```yaml
- id: "short-unique-name-2026"
  title: "Paper Title"
  authors: "Author A, Your Name, and Author B"
  venue: "Journal or Conference"
  year: 2026
  selected: true
  doi: "https://doi.org/10.xxxx/example"
  pdf: "/papers/example.pdf"
  project: "https://example.com/project"
  website: "https://example.com"
```

- `id` 必须唯一，推荐使用简短标题加年份。
- `selected` 字段保留用于将来设置代表作；目前所有论文统一显示在 Publications 页面。
- `doi`、`pdf`、`project`、`website` 都是可选字段。不需要的整行删除即可。
- 网站会自动按 `year` 从新到旧排序。
- 本地论文 PDF 可以放入 `public/papers/`，然后使用 `/papers/文件名.pdf`。

## 添加 Research Project

打开 `content/projects.yaml`，复制：

```yaml
- id: "project-short-name"
  title: "Project Title"
  period: "2025-present"
  description: "One or two sentences describing the project."
  url: "https://example.com/project"
```

如果没有项目网页，删除 `url` 行。

## 修改 Education / Experience

打开 `content/experience.yaml`：

```yaml
- id: "phd-example"
  type: "education"
  institution: "University Name"
  role: "PhD in Your Field"
  period: "2023-present"
  description: "Optional short description."
```

`type` 只能填写 `education` 或 `experience`。没有说明时可以删除 `description`。

## 更换照片

1. 准备一张横向照片，推荐比例为 4:3，尺寸至少 1200 × 900 像素。
2. 将照片命名为 `profile.jpg`。
3. 用它替换 `public/images/profile.jpg`。

如果使用不同文件名，需要同时修改 `content/profile.yaml` 中的 `profileImage`。

## 更换页首背景

1. 准备一张宽幅横图，推荐至少 1800 像素宽。
2. 命名为 `hero-background.jpg`。
3. 替换 `public/images/hero-background.jpg`。

也可以修改 `content/profile.yaml` 的 `heroImage` 使用其他文件名。

## 更换页尾背景

1. 准备一张淡色宽幅横图，推荐至少 1800 像素宽。
2. 命名为 `footer-background.jpg`。
3. 替换 `public/images/footer-background.jpg`。

也可以修改 `content/profile.yaml` 的 `footerImage` 使用其他文件名。

## CV 当前未公开

网站目前不提供 CV 查看或下载入口，`public/` 中也不保存 CV。需要重新公开时，请先检查 PDF 中是否包含电话号码、住址等不希望公开的信息，再恢复下载入口。

## 修改联系方式和外部链接

邮箱、地点和链接都在 `content/profile.yaml`。例如：

```yaml
links:
  - label: "Google Scholar"
    url: "https://scholar.google.com/..."
  - label: "LinkedIn"
    url: "https://www.linkedin.com/in/..."
```

## 修改导航栏目

在 `content/profile.yaml` 中找到 `navigation`：

```yaml
navigation:
  - label: "About"
    href: "/"
  - label: "Research"
    href: "/research/"
  - label: "Publications"
    href: "/publications/"
  - label: "Contact"
    href: "/contact/"
```

可以修改显示文字或调整顺序。`href` 是目标位置；不要删除开头的 `/`。

## 添加新的栏目

现有页面分别位于 `src/pages/index.astro`、`research.astro`、`publications.astro` 和 `contact.astro`。添加全新栏目需要修改对应页面文件；建议先保存副本，或让熟悉 HTML 的人协助。

如果栏目只是 Research、Publication、Project 或 Experience 的新条目，不需要创建新 section，只需修改对应 YAML 文件。

## 日常发布：GitHub Desktop

网站仓库使用 `ZoogerLio/huaye410-site`，正式网址是 `https://huaye410.site`。第一次发布后，日常更新不需要再配置 GitHub Pages 或阿里云：

1. 修改 YAML，或者同名替换照片和背景。
2. 可选运行 `npm run dev` 检查效果。
3. 打开 GitHub Desktop，在左下角 **Summary** 填写本次修改，例如 `Update biography`。
4. 点击 **Commit to main**。
5. 点击顶部的 **Push origin**。
6. 等待几分钟；仓库中的 GitHub Actions 会自动构建并发布网站。

如果发布失败，打开 GitHub 仓库的 **Actions** 页面查看红色的失败记录。只有绿色勾号表示发布成功。

## 第一次发布到 GitHub Pages

1. 登录 GitHub，在账号 `ZoogerLio` 下新建公开仓库 `huaye410-site`。不要在网页端额外创建 README、License 或 `.gitignore`。
2. 在 GitHub Desktop 中选择 **Add an Existing Repository from your Local Drive**，选择本项目文件夹。如果提示尚未建立 Git 仓库，先选择 **Create a Repository**，名称填写 `huaye410-site`。
3. 提交全部文件，点击 **Publish repository**，并确认仓库不是 Private。
4. 打开仓库 **Settings → Pages**，将 **Build and deployment → Source** 设置为 **GitHub Actions**。
5. 打开 **Actions** 页面，等待 `Deploy to GitHub Pages` 显示绿色勾号。

项目已经包含 `.github/workflows/deploy.yml`，生产构建固定使用 `https://huaye410.site` 和网站根路径。更多说明见 [Astro 官方 GitHub Pages 指南](https://docs.astro.build/en/guides/deploy/github/)。

## 连接 huaye410.site

1. 打开 GitHub 仓库的 **Settings → Pages**。
2. 在 **Custom domain** 中填写 `huaye410.site` 并保存。
3. 在阿里云的 `huaye410.site` DNS 解析页面添加四条 `@` 类型的 A 记录，记录值分别为：
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
4. 添加一条 `www` 类型的 CNAME 记录，记录值为 `ZoogerLio.github.io`。
5. 删除与 `@` 或 `www` 冲突的旧 A、AAAA 或 CNAME 记录，不要添加 `*` 通配符记录。
6. 等待 GitHub 的 DNS 检查通过，然后勾选 **Enforce HTTPS**。DNS 和证书可能需要一段时间才能生效。

项目中的 `public/CNAME` 已固定为 `huaye410.site`。详细原理见 [GitHub 自定义域名说明](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)。

## 发布前隐私检查

GitHub 免费账户的 Pages 仓库是公开的。不要将密码、API Key、身份证明、私人地址、未公开论文或研究数据放入本项目。

- `public/` 下的图片、PDF 和其他文件都会公开。
- 删除文件并不能自动清除以前已经公开提交的 Git 历史；敏感文件不要提交。
- 没有添加开源 License，公开可见不代表主动授权他人复制使用。

## 文件结构

```text
academic-homepage/
├── content/
│   ├── profile.yaml
│   ├── publications.yaml
│   ├── projects.yaml
│   └── experience.yaml
├── public/
│   ├── images/
│   │   ├── profile.jpg
│   │   ├── hero-background.jpg
│   │   └── footer-background.jpg
├── src/
│   ├── components/
│   ├── layouts/
│   ├── pages/
│   └── styles/
└── README.md
```

当前网页已经使用 Ye Hua 的资料和照片，CV 暂不公开。发布前仍建议检查公开邮箱和论文信息是否为最新版本。
