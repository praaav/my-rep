#вариант 17 у меня :)
USER = "user"
HOST = "MacBook-Pro-VFS"
SYMBOL = "%"
CWD = "~"


def parse(s):
    out, buf, q = [], "", None
    for ch in s.strip():
        if q:
            if ch == q: q = None
            else: buf += ch
        else:
            if ch in ("'", '"'): q = ch
            elif ch.isspace():
                if buf: out.append(buf); buf = ""
            else: buf += ch
    if buf: out.append(buf)
    return (out[0], out[1:]) if out else ("", [])

def cmd_ls(args): print(f"[stub] ls -> args: {args}")
def cmd_cd(args): print(f"[stub] cd -> args: {args}")

def parse_cli(argv):
    vfs, script = "", ""
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ("--vfs", "-v") and i+1 < len(argv): vfs = argv[i+1]; i += 2
        elif a in ("--script", "-s") and i+1 < len(argv): script = argv[i+1]; i += 2
        else: i += 1
    return {"vfs_path": vfs, "startup_script": script}

def run_line(line, conf):
    cmd, args = parse(line)
    if not cmd: return "ok"
    if cmd == "exit":
        code = 0
        if args:
            try: code = int(args[0])
            except: print("exit: argument must be a number"); code = 0
        print("Bye!")
        raise SystemExit(code)
    if cmd == "ls": cmd_ls(args); return "ok"
    if cmd == "cd": cmd_cd(args); return "ok"
    if cmd == "conf-dump":
        print(f"vfs_path={conf['vfs_path']}")
        print(f"startup_script={conf['startup_script']}")
        print(f"user={USER}")
        print(f"host={HOST}")
        print(f"cwd={CWD}")
        return "ok"
    print(f"command not found: {cmd}")
    return "err"  # ошибочная строка (для скрипта — пропускаем)

def run_script(path, conf):
    try:
        with open(path, "r", encoding="utf-8") as f:
            for raw in f:
                line = raw.rstrip("\n")
                if not line or line.lstrip().startswith("#"):  # пустые/комментарии
                    continue
                print(f"{USER}@{HOST} {CWD} {SYMBOL} {line}")
                try:
                    st = run_line(line, conf)
                    # 'err' просто пропускаем
                except SystemExit:
                    raise
                except Exception as e:
                    print(f"error: {e}")  # тоже пропускаем и идём дальше
    except FileNotFoundError:
        print(f"script not found: {path}")

def repl(conf):
    while True:
        try:
            line = input(f"{USER}@{HOST} {CWD} {SYMBOL} ")
            run_line(line, conf)
        except KeyboardInterrupt:
            print("^C")
        except EOFError:
            print(); break
        except Exception as e:
            print(f"error: {e}")

if __name__ == "__main__":
    import sys
    conf = parse_cli(sys.argv[1:])
    if conf["startup_script"]:
        run_script(conf["startup_script"], conf)
    repl(conf)
