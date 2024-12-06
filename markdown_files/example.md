# Pythonコードの例

以下はPythonでHello, World!を出力する簡単な例です。

```python
# Pythonの基本例
print("Hello, World!")
```
条件分岐の例
次に、条件分岐を使用した例を示します。


コードをコピーする
## 条件分岐の例
```python
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

## 使用例
```python
print(check_even_odd(10))  # 出力: Even
print(check_even_odd(7))   # 出力: Odd
リストの操作例
リスト操作の基本的な例です。
```  


コードをコピーする
## リストの基本操作
```python
numbers = [1, 2, 3, 4, 5]

# リストの合計を計算
total = sum(numbers)
print(f"リストの合計: {total}")

# リストの偶数を抽出
evens = [num for num in numbers if num % 2 == 0]
print(f"偶数のリスト: {evens}")
```