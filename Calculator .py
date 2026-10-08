print("--- مرحباً بك في الآلة الحاسبة الذكية ---")

while True:
    print("\nالعمليات المتاحة: +، -، *، /")
    print("اكتب 'خروج' للإنهاء")
    
    choice = input("اختر العملية: ")
    
    if choice == 'خروج':
        print("وداعاً!")
        break
    
    if choice in ['+', '-', '*', '/']:
        try:
            num1 = float(input("أدخل الرقم الأول: "))
            num2 = float(input("أدخل الرقم الثاني: "))
            
            if choice == '+':
                result = num1 + num2
                print(f"النتيجة: {num1} + {num2} = {result}")
            elif choice == '-':
                result = num1 - num2
                print(f"النتيجة: {num1} - {num2} = {result}")
            elif choice == '*':
                result = num1 * num2
                print(f"النتيجة: {num1} * {num2} = {result}")
            elif choice == '/':
                if num2 == 0:
                    print("خطأ: لا يمكن القسمة على صفر!")
                else:
                    result = num1 / num2
                    print(f"النتيجة: {num1} / {num2} = {result}")
        except ValueError:
            print("خطأ: الرجاء إدخال أرقام صحيحة او عشرية.")
    else:
        print("عملية غير صالحة، حاول مرة أخرى.")
