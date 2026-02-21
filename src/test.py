"""テスト用のサンプルモジュール"""


def greet(name: str) -> str:
    """名前を受け取って挨拶文を返す"""
    return f"Hello, {name}!"


def main() -> None:
    print(greet("World"))


if __name__ == "__main__":
    main()
