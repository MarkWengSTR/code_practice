# def identity(f):
#     return f

# _functions = {}


# def register(f):
#     global _functions
#     _functions[f.__name__] = f
#     return f


# @register
# def foo():
#     return 'bar'


# foo()
# print(_functions)

# ===============

# class Store(object):
#     def get_food(self, username, food):
#         if username != 'admin':
#             raise Exception("This user is not allowed to get food")
#         return self.storage.get(food)

#     def put_food(self, username, food):
#         if username != 'admin':
#             raise Exception("This user is not allowed to get food")
#         self.storage.put(food)

# ------------


# def check_is_admin(username):
#     if username != 'admin':
#         raise Exception("This user is not allowed to get food")


# class Store(object):
#     def get_food(self, username, food):
#         check_is_admin(username)
#         return self.storage.get(food)

#     def put_food(self, username, food):
#         check_is_admin(username)
#         self.storage.put(food)

# ------------


# def check_is_admin(f):
#     def wrapper(*arg, **kwargs):
#         if kwargs.get('username') != 'admin':
#             raise Exception("This user is not allowed to get food")
#         return f(*arg, **kwargs)
#     return wrapper


# class Store(object):
#     @check_is_admin
#     def get_food(self, username, food):
#         return self.storage.get(food)

#     @check_is_admin
#     def put_food(self, username, food):
#         self.storage.put(food)

# ------

def check_user_is_not(username):
    def user_check_deco(f):
        def wrapper(*arg, **kwargs):
            if kwargs.get('username') != username:
                raise Exception("This user is not allowed to get food")
            return f(*arg, **kwargs)
        return wrapper
    return user_check_deco


class Store(object):
    @check_user_is_not('admin')
    @check_user_is_not('user1234')
    def get_food(self, username, food):
        return self.storage.get(food)
