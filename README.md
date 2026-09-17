# Отчёт по практическому заданию

## «Технологии разработки программного обеспечения»

### Тема работы

Изучение способов слияния ветвей в Git с использованием **Merge**, **Squash Commits** и **Rebase**.

---

## Цель работы

Изучить основные способы объединения изменений из различных ветвей Git:

* `Merge` — объединение истории двух ветвей;
* `Squash` — объединение нескольких коммитов в один;
* `Rebase` — перенос коммитов одной ветви поверх другой.

Для каждого способа была создана отдельная ветвь и выполнено слияние с основной ветвью `main`.

---

# 1. Merge

## Создание ветви

Для демонстрации обычного слияния была создана ветвь `merge-example`:

```bash
git switch main
git switch -c merge-test
```

В новой ветви был изменен файл `demo.py` и выполнено два коммита

До слияния история имела следующий вид:

```text
A---B             main
     \
      C---D       merge-test
```

## Выполнение Merge

Для слияния была выбрана основная ветвь:

```bash
git switch main
```

После чего выполнена команда:

```bash
git merge --no-ff merge-test -m "Merge branch merge-example"
```

Параметр `--no-ff` используется для принудительного создания отдельного Merge Commit.

После операции история имеет следующий вид:

```text
A---B-------M     main
     \     /
      C---D       merge-test
```

Где `M` — Merge Commit.

## Результат

При использовании `Merge` коммиты `C` и `D` сохраняются в истории Git. Дополнительно создаётся Merge Commit, который объединяет две ветви.

Историю можно посмотреть командой:

```bash
git log --oneline --graph --all --decorate*   8e3aca6 (HEAD -> main) Merge branch merge-example
|\
| * 8b76c62 (merge-test) 2 commit
| * 0af4e50 1 commit
|/
*   42c3874 (origin/main, origin/HEAD) Merge pull request #2 from imuftiev/dev2
|\
| * 8213357 (origin/dev2, dev2) controlflow init in dev2
|/
*   7dca38c Merge pull request #1 from imuftiev/dev
|\
| * 19f32f1 workflow init in dev1
|/
* 25b36f4 mock class init
* 2d09f52 test_func init
* 419dd04 person1

```

---

# 2. Squash Commits

## Создание ветви

Для демонстрации Squash была создана отдельная ветвь:

```bash
git switch main
git switch -c squash-test
```

В ней был изменен файл `demo.py` и выполнено три отдельных коммита


```

До выполнения Squash история выглядит следующим образом:

```text
A---B---M             main
         \
          C---D---E   squatestple
```

## Выполнение Squash

Переходим в основную ветвь:

```bash
git switch main
```

Выполняем:

```bash
git merge --squash squash-test
```

Данная команда объединяет изменения из коммитов `C`, `D` и `E` и помещает результат в staging area.

После этого создаётся один новый коммит:

```bash
git commit -m "sqush commit"
```

Получаем:

```text
          C---D---E   squash-test
         /
A---B---M---S         main
```

Где `S` содержит совокупность изменений:

```text
S = C + D + E
```

## Результат

В отличие от обычного `Merge`, отдельные коммиты ветви `squash-example` не переносятся в историю `main`.

Вместо нескольких коммитов:

```text
C → D → E
```

в основной ветви появляется один итоговый коммит:

```text
S
```

Это позволяет сохранить историю основной ветви более компактной.

```bash
$ git log --oneline --graph --all --decorate
* b8b38fc (HEAD -> main) sqush commit
| * 496b441 (squash-test) 3 commit squash
| * 4cc7e5b 2 commit squash
| * 0684536 1 commit squash
|/
*   8e3aca6 Merge branch merge-example
|\
| * 8b76c62 (merge-test) 2 commit
| * 0af4e50 1 commit
|/
*   42c3874 (origin/main, origin/HEAD) Merge pull request #2 from imuftiev/dev2
|\
| * 8213357 (origin/dev2, dev2) controlflow init in dev2
|/
*   7dca38c Merge pull request #1 from imuftiev/dev
|\
| * 19f32f1 workflow init in dev1
|/
* 25b36f4 mock class init
* 2d09f52 test_func init
* 419dd04 person1

```
# 3. Rebase

### Создание ветки
Для демонстрации Rebase была создана отдельная ветвь:

```bash
git switch main
git switch -c rebase-test
```
В ней был добавлен файл `README.md` и выполнено два отдельных коммита
Получилось так:
```text
        было
          ↓
          B---C
         /
A-------D


        стало
          ↓
A---D---B'---C'
```
```bash
$ git log --oneline --graph --all --decorate
* 01e611d (HEAD -> rebase-test) rebase desc
* 605d950 README init
* 061b4ae (main) api init
* b8b38fc sqush commit
| * 496b441 (squash-test) 3 commit squash
| * 4cc7e5b 2 commit squash
| * 0684536 1 commit squash
|/
*   8e3aca6 Merge branch merge-example
|\
| * 8b76c62 (merge-test) 2 commit
| * 0af4e50 1 commit
|/
*   42c3874 (origin/main, origin/HEAD) Merge pull request #2 from imuftiev/dev2
|\
| * 8213357 (origin/dev2, dev2) controlflow init in dev2
|/
*   7dca38c Merge pull request #1 from imuftiev/dev
|\
| * 19f32f1 workflow init in dev1
|/
* 25b36f4 mock class init
* 2d09f52 test_func init
* 419dd04 person1
```

# Конфликты слияния
```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main)$ git merge dev
Auto-merging demo.py
CONFLICT (content): Merge conflict in demo.py
Automatic merge failed; fix conflicts and then commit the result.
```
```text
def test_func() -> None:
    print("Hello! and Goodbye!")
    print("How are you?")

def demo_func() -> None:
    print("Hi!")

def two_sum() -> None:
    print(5 + 6)

def ping() -> None:
    print("pong")
    pass

print("Hello")

test_func()
```text
```text
commit hash: 730fda5 
```

```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person2/std-project (main)
$ git merge origin/dev2
Merge made by the 'ort' strategy.
 mock.py | 3 +++
 1 file changed, 3 insertions(+)
```

```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person3/std-project (main)
$ git merge origin/dev3
Updating 63eb261..8ee7f23
Fast-forward
 demo.py | 1 -
 1 file changed, 1 deletion(-)
```
```text
Fast-forward
```
# git log, cherry pick, git reset
```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person3/std-project (dev3)
$ git log
commit 15b0f475798c5a5bcce2f8ea1f11683ff7509dad (HEAD -> dev3, origin/dev3)
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 13:22:51 2026 +0300

    change file

commit 8ee7f23c0a2709e9a4a7372a2b0a98048c31da9e
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 12:00:31 2026 +0300

    dev3 branch change

commit 63eb261ad87aaf63f5db9e7003e357a98fc49627
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 11:42:13 2026 +0300

    README update

commit 01e611d169e0177de912683e0b2b55ebcec90083
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 11:32:47 2026 +0300

    rebase desc

commit 605d950742ab202f8a1aaf8e7e591971a5541936
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
:
commit 15b0f475798c5a5bcce2f8ea1f11683ff7509dad (HEAD -> dev3, origin/dev3)
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 13:22:51 2026 +0300

    change file

commit 8ee7f23c0a2709e9a4a7372a2b0a98048c31da9e
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 12:00:31 2026 +0300

    dev3 branch change

commit 63eb261ad87aaf63f5db9e7003e357a98fc49627
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 11:42:13 2026 +0300

    README update

commit 01e611d169e0177de912683e0b2b55ebcec90083
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 11:32:47 2026 +0300

    rebase desc

commit 605d950742ab202f8a1aaf8e7e591971a5541936
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 11:29:52 2026 +0300

    README init

commit 061b4aef97bb0182174f35a48108a0601520e5d0
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 11:37:16 2026 +0300

    api init

commit b8b38fca8c5d9021f79161e3f6b5a268a411dea4
Author: imcode <128029980+ilyas11m@users.noreply.github.com>
Date:   Thu Sep 17 11:15:43 2026 +0300

    sqush commit

commit 8e3aca620d7503eb89d4854575822dea8c40393c
Merge: 42c3874 8b76c62
```

### git reset --hard
```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person3/std-project (dev3)
$ git reset --hard 8ee7f23c
HEAD is now at 8ee7f23 dev3 branch change

```text
Переместим коммит с dev ветки с хэшем: 97e91f0f814
в ветку dev3:
```

```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person3/std-project (dev3)
$ git cherry-pick 97e91f0f814
[dev3 06a21b9] readme report
 Date: Thu Sep 17 13:37:42 2026 +0300
 1 file changed, 54 insertions(+), 1 deletion(-)
```

```text
Сделаем интерактивный rebase последних трёх коммитов текущей ветки
```

```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main)
$ git rebase -i HEAD~3
Auto-merging demo.py
CONFLICT (content): Merge conflict in demo.py
error: could not apply 1b49ba3... ;rgb:bfbf/bfbf/bfbf:wa
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
hint: Disable this message with "git config set advice.mergeConflict false"
Could not apply 1b49ba3... # ;rgb:bfbf/bfbf/bfbf:wa

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ git rebase -i HEAD~3
fatal: It seems that there is already a rebase-merge directory, and
I wonder if you are in the middle of another rebase.  If that is the
case, please try
        git rebase (--continue | --abort | --skip)
If that is not the case, please
        rm -fr ".git/rebase-merge"
and run me again.  I am stopping in case you still have something
valuable there.


iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ ^C

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ git rebase --continue
demo.py: needs merge
You must edit all merge conflicts and then
mark them as resolved using git add

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ git rebase --continue
demo.py: needs merge
You must edit all merge conflicts and then
mark them as resolved using git add

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ git merge
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ git merge dev
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ git merge
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ git add .

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ git commit "merge conflict resolve"
error: pathspec 'merge conflict resolve' did not match any file(s) known to git

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ git commit -m "merge conflict resolve"
[detached HEAD 2df0dd1] merge conflict resolve
 1 file changed, 1 insertion(+)

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main|REBASE 1/4)
$ git rebase --continue
Successfully rebased and updated refs/heads/main.
```

# Работа с git format-patch
git format-patch — это команда в Git, которая создает текстовые файлы-патчи (заплатки) из ваших коммитов.
Каждый файл содержит не только сами изменения кода (diff), но и полные метаданные: автора, дату, сообщение коммита и порядковый номер. 
Получившийся файл имеет формат электронной почты (mbox).
Перенос кода без сети и репозиториев: Вы можете сохранить изменения на флешку или передать файл через мессенджер, если нет доступа к общему серверу

### Делаем 4 коммита на ветке dev3
```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person3/std-project (dev3)
$ git log --oneline --graph --decorate
* ce75953 (HEAD -> dev3) Third commit - 4 коммит
* bb97ef2 second commit - 3 коммит
* f24c087 changing for git patch - 2 коммит
* 06a21b9 readme report - 1 коммит
* 8ee7f23 dev3 branch change
* 63eb261 README update
* 01e611d rebase desc
* 605d950 README init
* 061b4ae api init
* b8b38fc sqush commit
*   8e3aca6 Merge branch merge-example
|\
| * 8b76c62 2 commit
| * 0af4e50 1 commit
|/
*   42c3874 Merge pull request #2 from imuftiev/dev2
|\
| * 8213357 controlflow init in dev2
|/
*   7dca38c Merge pull request #1 from imuftiev/dev
|\
| * 19f32f1 (dev) workflow init in dev1
|/
* 25b36f4 mock class init
* 2d09f52 test_func init
* 419dd04 person1
```
### Формируем patch
```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person3/std-project (dev3)
$ git format-patch main
0001-readme-report.patch
0002-changing-for-git-patch.patch
0003-second-commit.patch
0004-Third-commit.patch
```
### Применяем патч для main ветки
```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person3/std-project (main)
$ git apply 0002-changing-for-git-patch.patch

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person3/std-project (main)
$ git apply 0003-second-commit.patch

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person3/std-project (main)
$ git apply 0004-Third-commit.patch
0004-Third-commit.patch:19: trailing whitespace.
#Third commit
warning: 1 line adds whitespace errors.
```

```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person3/std-project (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        0001-readme-report.patch
        0002-changing-for-git-patch.patch
        0003-second-commit.patch
        0004-Third-commit.patch

no changes added to commit (use "git add" and/or "git commit -a")
```

```text
Вариант 6. «Работа с алиасами для упрощения команд Git»
Откройте терминал и выполните команду nano ~/.gitconfig для от-крытия файла конфигурации Git в текстовом редакторе Nano.
В файле конфигурации Git добавьте следующие строки для создания алиасов:   
[alias]
st = status
ci = commit
co = checkout
br = branch
df = diff
lg = log --oneline --decorate --all --graph
Это пример алиасов для упрощения команд status, commit, checkout, branch, diff и log.
Сохраните изменения в файле конфигурации Git, нажав Ctrl + O, за-тем Enter, и выйдите из редактора, нажав Ctrl + X.
Перезапустите терминал и выполните команды git st, git ci, git co, git br, git df и git lg для проверки, что алиасы работают корректно.
Создайте алиас git recent для команды git log --oneline -n 5 и проверь-те его работоспособность. 
Измените или удалите существующие алиасы, отредактируйте файл конфигурации Git соответственно.
Для удобства работы команды Git с алиасами рекомендуется доку-ментировать их использование в README вашего проекта или в специ-альном файле с описанием.
Обсудите созданные алиасы с другими участниками проекта, чтобы все могли использовать их.
```
### Ход работы
```bash
\LocalRepository\person1\std-project> ~/.gitconfig
```
```text
[user]
	name = imcode
	email = 128029980+ilyas11m@users.noreply.github.com
[filter "lfs"]
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
	required = true
[http]
	sslVerify = false
```

```text
[user]
	name = imcode
	email = 128029980+ilyas11m@users.noreply.github.com
[filter "lfs"]
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
	required = true
[http]
	sslVerify = false
[alias]
	st = status
	ci = commit
	co = checkout
	br = branch
	df = diff
	lg = log --oneline --decorate --all --graph
```

```bash
iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main)
$ git st
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main)
$ git ci
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main)
$ git co
M       README.md
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main)
$  git br
  dev
* main

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main)
$  git df
diff --git a/README.md b/README.md
index 0a37683..6c4de48 100644
--- a/README.md
+++ b/README.md
@@ -557,3 +557,74 @@ Untracked files:

 no changes added to commit (use "git add" and/or "git commit -a")
 ```
+
+```text
+Вариант 6. «Работа с алиасами для упрощения команд Git»
+Откройте терминал и выполните команду nano ~/.gitconfig для от-крытия файла конфигурации Git в текстовом редакторе Nano.
+В файле конфигурации Git добавьте следующие строки для создания алиасов:
+[alias]
+st = status
+ci = commit
+co = checkout
+br = branch
+df = diff
+lg = log --oneline --decorate --all --graph
+Это пример алиасов для упрощения команд status, commit, checkout, branch, diff и log.
+Сохраните изменения в файле конфигурации Git, нажав Ctrl + O, за-тем Enter, и выйдите из редактора, нажав Ctrl + X.
+Перезапустите терминал и выполните команды git st, git ci, git co, git br, git df и git lg для проверки, что алиасы работают корректно.

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main)
$ git lg
* 0c7b7b3 (HEAD -> main) report update
* 0cb17aa report update patch
* 61b6622 (origin/main, origin/HEAD) report uppdate
* 9c4be3e Report update
* 97e91f0 readme report
*   730fda5 Conflict resolved
|\
| * 2fed8e7 (origin/dev, dev) dev change
| * 1b49ba3 ;rgb:bfbf/bfbf/bfbf:wa
| | * 15b0f47 (origin/dev3) change file
| | * 8ee7f23 dev3 branch change
| |/
|/|
* | 63eb261 README update
* | 01e611d rebase desc
* | 605d950 README init
* | 061b4ae api init
* | b8b38fc sqush commit
* |   8e3aca6 Merge branch merge-example
|\ \
| * | 8b76c62 2 commit
| * | 0af4e50 1 commit
|/ /
* |   42c3874 Merge pull request #2 from imuftiev/dev2
:

iwast@IlyasMuftiev MINGW64 ~/OneDrive/Рабочий стол/LocalRepository/person1/std-project (main)
$ git recent
0c7b7b3 (HEAD -> main) report update
0cb17aa report update patch
61b6622 (origin/main, origin/HEAD) report uppdate
9c4be3e Report update
97e91f0 readme report
```
