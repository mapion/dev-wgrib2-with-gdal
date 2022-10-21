import subprocess

def main():
  timeout = 10 # 単位は秒
  try:
    processed = subprocess.run('wgrib2 --version', shell=True, timeout=timeout, stdout=subprocess.PIPE, text=True)
    print(processed.stdout)
  except Exception as e:
    print(e)

if __name__ == "__main__":
  main()