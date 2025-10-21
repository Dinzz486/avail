#!/usr/bin/env python3
import os
import json
import subprocess
import datetime
import random

# 读取配置文件
def load_config():
    with open('commit_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# 执行Git命令
def run_git_command(command):
    print(f"执行: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"错误: {result.stderr}")
    return result.returncode == 0

# 创建随机内容的文件
def create_random_file(commit_num, date):
    filename = f"commit_{date}_{commit_num}.txt"
    content = f"这是第{commit_num}次提交在{date}的内容 {random.randint(1000, 9999)}"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return filename

# 主函数
def main():
    config = load_config()
    total_commits = config['totalCommits']
    total_days = config['totalDays']
    commit_dates = config['commitDates']
    
    print(f"开始自动提交: 总计{total_commits}次提交，分布在{total_days}天")
    
    # 设置Git用户名和邮箱（如果没有设置）
    run_git_command("git config user.name 'Auto Commit Bot'")
    run_git_command("git config user.email 'auto-commit@example.com'")
    
    current_commit = 0
    
    for date_info in commit_dates:
        date = date_info['value']
        commits_for_day = date_info['commitNumber']
        print(f"处理日期: {date}, 提交次数: {commits_for_day}")
        
        for i in range(1, commits_for_day + 1):
            current_commit += 1
            # 创建随机内容文件
            filename = create_random_file(i, date)
            
            # 添加文件到Git
            run_git_command(f"git add {filename}")
            
            # 设置提交时间为指定日期的随机时间
            time_str = f"{date} {random.randint(9, 18)}:{random.randint(0, 59)}:{random.randint(0, 59)}"
            env = os.environ.copy()
            env['GIT_COMMITTER_DATE'] = time_str
            env['GIT_AUTHOR_DATE'] = time_str
            
            # 执行提交
            commit_cmd = f"git commit -m 'Auto commit {current_commit}/{total_commits} on {date}'"
            print(f"执行: {commit_cmd} (时间: {time_str})")
            result = subprocess.run(commit_cmd, shell=True, text=True, capture_output=True, env=env)
            if result.returncode != 0:
                print(f"提交错误: {result.stderr}")
            else:
                print(f"提交成功: {current_commit}/{total_commits}")
    
    print("\n所有提交完成！")
    print("执行 'git log' 查看提交历史")
    
    # 显示提交统计信息
    print("\n提交统计:")
    run_git_command("git log --oneline | wc -l")
    run_git_command("git log --pretty=format:'%ad' --date=short | sort | uniq -c")

if __name__ == "__main__":
    main()