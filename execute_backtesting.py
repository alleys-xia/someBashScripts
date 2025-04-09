import subprocess
import sys
import time

# 固定参数
TCP_ADDRESS = "tcp://210.14.72.18:26666"
USERNAME = "00033259"
PASSWORD = "59009571"

def run_script(script_name, times):
    # 构建完整的命令，包含固定参数
    command = ['python', script_name, TCP_ADDRESS, USERNAME, PASSWORD]
    
    # 运行指定次数
    for i in range(times):
        print(f"正在执行第 {i+1} 次运行...")
        try:
            # 运行脚本并等待其完成
            subprocess.run(command, check=False)
        except Exception as e:
            print(f"运行出错: {e}")
        print(f"第 {i+1} 次运行完成")
        
        # 如果不是最后一次运行，则等待2秒
        if i < times - 1:
            print("等待2秒后开始下一次运行...")
            time.sleep(2)
        
        print("-" * 50)

def main():
    # 检查参数数量
    if len(sys.argv) < 2:
        print("使用方法: python run_multiple.py <script_name> [次数]")
        print("例如: python run_multiple.py demo.py 5")
        sys.exit(1)
    
    # 获取脚本名称
    script_name = sys.argv[1]
    
    # 获取运行次数，如果未提供则默认为3
    try:
        times = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        if times <= 0:
            print("错误：运行次数必须大于0")
            sys.exit(1)
    except ValueError:
        print("错误：次数必须是一个有效的整数")
        sys.exit(1)
    
    run_script(script_name, times)

if __name__ == "__main__":
    main()


# example: python execute_backtesting.py demo_lev2.py 5     运行5次
