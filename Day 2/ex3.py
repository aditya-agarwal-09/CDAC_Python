mail = input("Enter the email id: ")
if(mail.count("@")==1):
    new_id = mail.split('@')[1]
    print(new_id)
else:
    print("invalid email")