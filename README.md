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
<<<<<<< HEAD
    print("Hello! and Goodbye!")
    print("How are you?")

def demo_func() -> None:
    print("Hi!")

def two_sum() -> None:
    print(5 + 6)

def ping() -> None:
    print("pong")
=======
    pass

print("Hello")
>>>>>>> dev

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
