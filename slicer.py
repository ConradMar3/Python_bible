#get user e-mail adress

email = input("What is your e-mail adress?:").strip()

#slice out user name
#johndoe@thingy.com

user = email[:email.index("@")]

#slice domain name

domain = email[email.index("@")+1:]

#format message

output = "Your user name is {} and your domain name is {}".format(user, domain)

#display output message

print(output)
