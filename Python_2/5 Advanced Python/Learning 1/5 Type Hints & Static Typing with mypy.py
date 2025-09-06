
def exercise_1():
    def add(x: int, y: int) -> int:
        return x + y

    result: int = add(5,5)
    print(result)


def exercise_2():
    names: list[str] = ['Kopi', "Nryo", "Kophalem"]

    for name in names:
        print(name)

    points: tuple[int, int] = (5, 5)
    print(points)

    bank_account: dict[str, int] = {"Bank_1": 1000, "Bank_2": 2000, "Bank_3": 3000 }
    print(bank_account)


def exercise_3():
    def count_words(sentences: list[str]) -> dict:
        word_count = {}
        for sentence in sentences:
            for word in sentence.split():
                word_count[word] = word_count.get(word, 0) + 1
        return word_count

    list_sentences = [
        "This is the first sentence.",
        "Here is the second sentence.",
        "And this is the third sentence."
    ]

    print(count_words(list_sentences))


def exercise_4():
    from typing import Optional, Union

    def find_user(id: int) -> Optional[dict]:
        if id == 0:
            return None
        return {"id": id, "name": "User"}

    print(find_user(60))

    def thoughts(thought: Union[str, int, float]) -> str:
        return str(thought)

    print(thoughts(59))


def exercise_5():



def main():
    # exercise_1()
    # exercise_2()
    # exercise_3()
    exercise_4()



if __name__ == "__main__":
    main()