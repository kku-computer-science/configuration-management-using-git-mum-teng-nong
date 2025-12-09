def main():
    while True:
        print("\n=== Sorting Program ===")

        count_str = input("จำนวนตัวเลขที่จะกรอก: ").strip()

        if "." in count_str:
            print("กรุณากรอกจำนวนเต็มเท่านั้น")
            continue

        try:
            count = int(count_str)
        except:
            print("กรุณากรอกจำนวนเต็มเท่านั้น")
            continue

        if count <= 0:
            print("จำนวนต้องมากกว่า 0")
            continue

        arr = []
        for i in range(count):
            while True:
                num_str = input(f"ตัวที่ {i+1}: ").strip()
                if "." in num_str:
                    print("ห้ามทศนิยม")
                    continue
                try:
                    num = int(num_str)
                    arr.append(num)
                    break
                except:
                    print("ต้องเป็นจำนวนเต็ม")

        original = arr[:]

        print("\nเลือกวิธีเรียง:")
        print("1 = quick sort")
        print("2 = bubble sort")
        choice = input("เลือก: ").strip()

        if choice == "1":
            result = quick_sort(arr[:])
            print("\nใช้ quick sort เรียงแล้ว:")
        elif choice == "2":
            result = bubble_sort(arr[:])
            print("\nใช้ bubble sort เรียงแล้ว:")
        else:
            print("ตัวเลือกไม่ถูกต้อง")
            continue

        print("ก่อนเรียง:", original)
        print("หลังเรียง :", result)

        again = input("\nทำต่อไหม (y/n): ").lower().strip()
        if again != "y":
            break


if __name__ == "__main__":
    main()