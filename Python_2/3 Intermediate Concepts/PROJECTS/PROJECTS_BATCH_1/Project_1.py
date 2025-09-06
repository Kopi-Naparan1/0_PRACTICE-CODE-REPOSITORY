
def count_down_up(n=0, mode=None, max_n=None):
    if mode == "up":
        if n == max_n:
            print("Kaboom!!!")
        else:
            print(n)
            count_down_up(n + 1, mode='up', max_n=max_n)
    elif mode == "down":
        if n == 0:
            print("Kaboom!!!")
        else:
            print(n)
            count_down_up(n - 1, mode='down')


def main():
    count_down_up(10, mode="down")
    count_down_up(10, mode="up", max_n=100)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")

