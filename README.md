# 🧠 Shell Emulator — Variant 17

Минимальный учебный эмулятор командной оболочки macOS/UNIX, написанный на Python.  
Проект выполнен по варианту **№ 17**.  
Имитация поведения консоли macOS с пользовательским приглашением вида:
```
prav@MacBook-Pro-VFS ~ %
```

---

## 📍 Этап 1 — REPL

**Цель:** создать минимальный прототип эмулятора.

### Реализовано
- CLI-интерфейс с macOS-приглашением;
- Простой парсер команд и аргументов;
- Поддержка кавычек `' '` и `" "`;
- Команды-заглушки `ls`, `cd`;
- Команда `exit`;
- Обработка ошибок и пустых строк.

---

## ⚙️ Этап 2 — Конфигурация

**Цель:** сделать эмулятор настраиваемым.

### Реализовано
- Аргументы командной строки:
  - `--vfs <путь>` — путь к виртуальной файловой системе;
  - `--script <путь>` — путь к стартовому скрипту.
- Стартовый скрипт выполняется построчно (эмулируется ввод);
- Ошибочные строки пропускаются;
- Служебная команда `conf-dump` выводит все параметры в формате `ключ=значение`.

---

## 🚀 Запуск

Интерактивно:
```bash
python3 main.py
```

С параметрами:
```bash
python3 main.py --vfs /Users/prav/vfs --script scripts/demo.txt
```

---

## 📜 Пример стартового скрипта (scripts/demo.txt)

```bash
# test script
conf-dump
ls "test folder"
cd src
foo
exit 0
```

---

## 💻 Скрипты для тестирования

**macOS / Linux:**

### `run_with_vfs.sh`
```bash
#!/usr/bin/env bash
python3 main.py --vfs "/Users/prav/vfs"
```

### `run_with_script.sh`
```bash
#!/usr/bin/env bash
python3 main.py --script "scripts/demo.txt"
```

### `run_full.sh`
```bash
#!/usr/bin/env bash
python3 main.py --vfs "/tmp/vfs" --script "scripts/demo.txt"
```

**⚠️ Если получаешь “permission denied”:**
```bash
chmod +x run_with_vfs.sh run_with_script.sh run_full.sh
```

**Windows-альтернатива:**
```bat
python main.py --vfs "C:\Users\prav\vfs" --script "scripts\demo.txt"
pause
```

---

## 🧩 Команды эмулятора

| Команда | Описание |
|----------|-----------|
| `ls` | Заглушка: выводит список аргументов |
| `cd` | Заглушка: выводит список аргументов |
| `exit [код]` | Завершает выполнение |
| `conf-dump` | Показывает текущие параметры эмулятора |

---

## 🧠 Примеры тестов (для проверки)

### ✅ Ввод в консоль
```
prav@MacBook-Pro-VFS ~ % ls a b c
[stub] ls -> args: ['a', 'b', 'c']

prav@MacBook-Pro-VFS ~ % ls "my folder"
[stub] ls -> args: ['my folder']

prav@MacBook-Pro-VFS ~ % cd test
[stub] cd -> args: ['test']

prav@MacBook-Pro-VFS ~ % conf-dump
vfs_path=/Users/prav/vfs
startup_script=scripts/demo.txt
user=prav
host=MacBook-Pro-VFS
cwd=~

prav@MacBook-Pro-VFS ~ % exit 0
Bye!
```

### ✅ Пример ошибочной строки
```
prav@MacBook-Pro-VFS ~ % foo
command not found: foo
```

---

## 🧾 Структура репозитория

```
my-rep/
├── main.py                # основной код эмулятора
├── README.md              # описание проекта (этот файл)
├── run_with_vfs.sh
├── run_with_script.sh
├── run_full.sh
└── scripts/
    └── demo.txt           # стартовый скрипт
```

---

## 🧑‍💻 Автор

**Петрусенко Лев Анатольевич (praaav)**  
Вариант 17
