



def main():
    try:
        hey = "hey"
        if True:
            if True:
                while False:
                    pass
                else:
                    return 1/0
    except Exception as e:
            print("Excpetion :", e)
            raise e
    finally:
            print("Hit Finally")
            print(hey)

if __name__ == "__main__":
    main()