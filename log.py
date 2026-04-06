def login():
    print("===== Student Login =====")
    
    usn = input("Enter USN :")
    
    # Validate USN range (101–180)
    try:
        num = int(usn[-3:])
        if num < 101 or num > 180:
            print("Invalid USN! Not in allowed range.")
            return None
    except:
        print("Invalid USN format!")
        return None

    password = input("Enter Password: ")

    # 🔐 Password = USN
    if password == usn:
        print("Login Successful ✅\n")
        return usn
    else:
        print("Wrong Password ❌ (Password should match USN)")
        return None