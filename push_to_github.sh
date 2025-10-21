#!/bin/bash

# 显示当前仓库状态
echo "=== 当前Git仓库状态 ==="
git status
echo ""

# 检查是否有未提交的更改
if [[ $(git status --porcelain) ]]; then
    echo "警告: 有未提交的更改，请先提交所有更改。"
    exit 1
fi

echo "=== 提交历史统计 ==="
git log --oneline | wc -l
echo ""

echo "=== 推送到GitHub指南 ==="
echo "要将本地仓库推送到GitHub，请按照以下步骤操作："
echo ""
echo "1. 首先，在GitHub上创建一个新的空仓库"
echo "2. 然后运行以下命令将本地仓库与GitHub仓库关联："
echo ""
echo "   # 请将 YOUR_GITHUB_USERNAME 和 YOUR_REPOSITORY_NAME 替换为实际值"
echo "   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git"
echo ""
echo "3. 推送代码到GitHub："
echo ""
echo "   git push -u origin main"
echo ""
echo "注意：如果您使用SSH密钥，请使用SSH URL：git@github.com:YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git"
echo ""
echo "=== 提交历史预览 ==="
git log --oneline -n 5

echo ""
echo "执行以上命令后，您应该能在GitHub上看到您的仓库和所有提交历史。"