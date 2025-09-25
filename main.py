USER = "prav"
HOST = "MacBook-Pro-Prav"
SYMBOL = "%"
CWD = "~"

def parse(s):
    p = s.strip().split()
    return (p[0], p[1:]) if p else ("", [])

def cmd_ls(args):
    print(f"[stub] ls -> args: {args}")

def cmd_cd(args):
    print(f"[stub] cd -> args: {args}")

def repl():
    while True:
        try:
            line = input(f"{USER}@{HOST} {CWD} {SYMBOL} ")
            cmd, args = parse(line)
            if not cmd:
                continue
            if cmd == "exit":
                code = 0
                if args:
                    try: code = int(args[0])
                    except: print("exit: argument must be a number"); code = 0
                print("Bye!")
                raise SystemExit(code)
            if cmd == "ls":
                cmd_ls(args); continue
            if cmd == "cd":
                cmd_cd(args); continue
            print(f"command not found: {cmd}")
        except KeyboardInterrupt:
            print("^C")
        except EOFError:
            print(); break
        except Exception as e:
            print(f"error: {e}")

if __name__ == "__main__":
    repl()
