def password_strength_checker():
    print("\n Password Strength Checker")
    password = input("Enter your Password : ")
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength +=1
    else:
        feedback.append("Password should be at least 8 characters long")

    if any(char.isupper() for char in password):
        strength +=1
    else:
        feedback.append("Add atleast one UPPERCASE character")

    if any(char.islower() for char in password):
        strength +=1
    else:
        feedback.append("Add atleast one lowercase character")

    if any(char.isdigit() for char in password):
        strength +=1
    else:
        feedback.append("Add atleast one digit (0 - 9) to your password")

    special_chars = "~!@#$%^&*()_+=-"

    if any(char in special_chars for char in password ):
        strength +=1
    else :
        feedback.append("Add atleast one Special Character in your Password i.e {special_chars}")

    print("\n Password Analysis : ")

    if strength == 5:
        print("This is a Strong Password")
    
    elif strength >= 3 :
        print("Good, but could be Stronger")

    else :
        print("This is a Weak Password , try another one")

    if feedback:
        print("\n Suggestions to improve : ")
        for suggestion in feedback :
            print(f"-{suggestion}")

password_strength_checker()
