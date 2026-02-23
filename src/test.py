"""テスト用のサンプルモジュール"""

DEFAULT_LANG = "ja"


def greet(name: str, lang: str = DEFAULT_LANG) -> str:
    """名前と言語を受け取って挨拶文を返す"""
    if lang == "ja":
        return f"こんにちは、{name}さん！"
    return f"Hello, {name}!"


def main() -> None:
    print(greet("World"))
    print(greet("世界", lang="ja"))


if __name__ == "__main__":
    main()
