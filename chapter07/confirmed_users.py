#define two list unconfirmed_users\confirmed_users
unconfirmed_users=['alice','brain','candace']
confirmed_users = []
for unconfirmed_user in unconfirmed_users:
    print(unconfirmed_user,end=" ")
# if unconfirmed_users  list has element and pop()
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    # confirmed_user list append this element equals print reverse
    confirmed_users.append(current_user)
print()
for confirmed_user in confirmed_users:
    print(confirmed_user,end=" ")