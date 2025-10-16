has_account=True
email_verified=False
can_login=has_account and email_verified
print("Can login:",can_login)

email="g@example.com"
is_email_valid="@" in email
print("Email valid:",is_email_valid)

userage=17
is_age_valid=userage>=18
print("Age valid:",is_age_valid)

can_login_final=has_account and email_verified and is_email_valid and is_age_valid
print("Can login final:",can_login_final)

print("Has account:",has_account is True)