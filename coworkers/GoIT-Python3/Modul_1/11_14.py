# def is_valid_password(password):
        # if password == []:
        #  return False
        # for i in password:
        #  if len(password) != 8:
        #     return False
        #  for i in password:
        #     if i  not in '0123456789':
        #         return False
        #     if i not in 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z':
        #         return False
        #     if i not in 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z':
        #         return False
        #     else:
        #      return True
# def is_valid_password(password):
#     result = 0
#     if len(password) == 8:
#         return True
#     for i in password:
#         if i in '0123456789':
#             break
#         if i == i.lower():
#             break
#         if i in i.upper():
#             break
#         if i in '!@#$%^&*()_+-=':
#             break
#         return True
#     else:
#             return False
            
# def is_valid_password(password):
#     password = {password}
#     lower = {'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'}
#     upper = {'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'}
#     numbers = {'0123456789'}
#     sumbols = {'!@#$%^&*()_+-='}
#     result = 0
#     if len(password) == 8:
#         return True
#     for password in lower and upper and numbers and not sumbols:
#             return True
#     else:
#           return False
    # if result == 2:
    #   return True

# def is_valid_password(password):
#     flag = True
#     for i in password:
#         if i in '0123456789':
#             flag = True
#             break
#         if i in 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z':
#             flag = True
#             break
#         if i in 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z':
#             flag = True
#             break
#         if i in '!@#$%^&*()_+-=':
#             flag = False
#             break
#     if len(password) == 8: 
#         flag = True
#         return flag
#     else:
#         return False    

def is_valid_password(password):
    flag = True
    if len(password) != 8:
        flag = False
    if not any(char.isdigit() for char in password):
        flag = False
    if not any(char.isupper() for char in password):
        flag = False
    if not any(char.islower() for char in password):
        flag = False
    return flag



print(is_valid_password('z,qrE1IE'))


        
    
         