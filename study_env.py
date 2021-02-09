# import contextlib


# def stop_database():
#     print("systemctl stop mysql.service")


# def start_database():
#     print("systemctl start mysql.service")


# class DBHandler:
#     def __enter__(self):
#         stop_database()
#         return self

#     def __exit__(self, exc_type, ex_value, ex_traceback):
#         start_database()


# @contextlib.contextmanager
# def db_handler():
#     stop_database()
#     yield
#     start_database()

# class dbhandler_decorator(contextlib.ContextDecorator):
#     def __enter__(self):
#         stop_database()

#     def __exit__(self, exc_type, ex_value, ex_traceback):
#         start_database()


# @dbhandler_decorator()
# def db_backup():
#     print("sql_dump database")

############
# property
#############
# import re

# EMAIL_FROMAT = re.compile(r"[^@]+@[^@]+\.[^@]+")


# def is_valid_email(potentially_valid_email: str):
#    return re.match(EMAIL_FROMAT, potentially_valid_email) is not None


# class User:
#    def __init__(self, username):
#        self.username = username
#        self._email = None

#    @property
#    def email(self):
#        return self._email

#    @email.setter
#    def email(self, new_email):
#        if not is_valid_email(new_email):
#            raise ValueError(
#                f"Can't set {new_email} as it's not a valid email")
#        self._email = new_email


# def main():
#    u1 = User("mark")
#    u1.email = "a222@gamil.com"
#    print(u1.email)

###############
# iterable
##############
from datetime import timedelta, date


# class DateRangeIterable:
#     def __init__(self, start_date, end_date):
#         self.start_date = start_date
#         self.end_date = end_date
#         self._present_day = start_date

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self._present_day >= self.end_date:
#             raise StopIteration
#         today = self._present_day
#         self._present_day += timedelta(days=1)
#         return today


# def main():
#     r1 = DateRangeIterable(date(2018, 1, 1), date(2018, 1, 5))
#     print(", ".join(map(str, r1)))
#     print(max(r1))

# class DateRangeContainerIterable:
#     def __init__(self, start_date, end_date):
#         self.start_date = start_date
#         self.end_date = end_date

#     def __iter__(self):
#         current_day = self.start_date
#         while current_day < self.end_date:
#             yield current_day
#             current_day += timedelta(days=1)


# def main():
#     r1 = DateRangeContainerIterable(date(2018, 1, 1), date(2018, 1, 5))
#     print(", ".join(map(str, r1)))
#     print(max(r1))


#############
# __contains__

#############

# Simplify the under function
# def mark_coordinate(grid, coord):
#     if 0 <= coord.x < grid.width and 0 <= coord.y < grid.height:
#         grid[coord] = MARKED

# class Boundaries:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def __contains__(self, coord):
#         x, y = coord
#         return 0 <= x < self.width and 0 <= y < self.height


# class Grid:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.limits = Boundaries(width, height)

#     def __contains__(self, coord):
#         return coord in self.limits


#############
# Mixin
#############

# class BaseTokenizer:

#     def __init__(self, str_token):
#         self.str_token = str_token

#     def __iter__(self):
#         yield from self.str_token.split("-")


# class UpperIterableMixin:
#     def __iter__(self):
#         return map(str.upper, super().__iter__())


# class LowerterableMixin:
#     def __iter__(self):
#         return map(str.lower, super().__iter__())


# class Tokenizer(LowerterableMixin, UpperIterableMixin, BaseTokenizer):
#     pass


# def main():
#     tk = Tokenizer("28a2329b-fd3f-4672")
#     print(list(tk))


############
# OCP(Open Close Principle)
###########

# Origianl
# class Event:
#     def __init__(self, raw_data):
#         self.raw_data = raw_data


# class UnknowEvent(Event):
#     """無法用資料來辨識的事件類型"""


# class LoginEvent(Event):
#     """使用者剛剛進入系統的事件"""


# class LogoutEvent(Event):
#     """使用者剛剛離開系統的事件"""


# class SystemMonitor:
#     def __init__(self, event_data):
#         self.event_data = event_data

#     def identify_event(self):
#         if (
#             self.event_data["before"]["session"] == 0
#             and self.event_data["after"]["session"] == 1
#         ):
#             return LoginEvent(self.event_data)
#         elif (
#             self.event_data["before"]["session"] == 1
#             and self.event_data["after"]["session"] == 0
#         ):
#             return LogoutEvent(self.event_data)

#         return UnknowEvent(self.event_data)

# # Use 多型
# class Event:
#     def __init__(self, raw_data):
#         self.raw_data = raw_data

#     @staticmethod
#     def meets_condition(event_data: dict):
#         return False


# class UnknowEvent(Event):
#     """無法用資料來辨識的事件類型"""


# class LoginEvent(Event):
#     @staticmethod
#     def meets_condition(event_data: dict):
#         return (
#             event_data["before"]["session"] == 0
#             and event_data["after"]["session"] == 1
#         )


# class LogoutEvent(Event):
#     @staticmethod
#     def meets_condition(event_data: dict):
#         return (
#             event_data["before"]["session"] == 1
#             and event_data["after"]["session"] == 0
#         )


# class Transaction(Event):
#     @staticmethod
#     def meets_condition(event_data: dict):
#         return event_data["after"].get("transaction") is not None


# class SystemMonitor:
#     def __init__(self, event_data):
#         self.event_data = event_data

#     def identify_event(self):
#         for event_cls in Event.__subclasses__():
#             try:
#                 if event_cls.meets_condition(self.event_data):
#                     return event_cls(self.event_data)
#             except KeyError:
#                 continue
#         return UnknowEvent(self.event_data)


# def main():
#     ll = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
#     print(ll.identify_event().__class__.__name__)

#     ll = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
#     print(ll.identify_event().__class__.__name__)

#     ll = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
#     print(ll.identify_event().__class__.__name__)

#     ll = SystemMonitor({"after": {"transaction": "No.2"}})
#     print(ll.identify_event().__class__.__name__)

################
# decorator
################

# # decorator_function_1
# class ControlledException(Exception):
#     """General Exception"""

#     def retry(operation):
#         @wraps(operation)
#         def wrapped(*args, **kwargs):
#             last_raised = None
#             RETRIES_LIMIT = 3
#             for _ in range(RETRIES_LIMIT):
#                 try:
#                     return operation(*args, **kwargs)
#                 except ControlledException as e:
#                     logger.info("retrying %s", operation.__qualname__)
#                     last_raised = e
#             raise last_raised
#         raise wrapped

#     @retry
#     def run_operation(task):
#         return task.run()

# # =======
# class LoginEventSerializer:
#     def __init__(self, event):
#         self.event = event

#     def serialize(self) -> dict:
#         return{
#             "username": self.event.username,
#             "password": "**redacted**",
#             "ip": self.event.ip,
#             "timestamp": self.event.timestamp.strftime("%Y-%m-%d %H:%M")
#         }


# class LoginEvent:
#     SERIALIZER = LoginEventSerializer

#     def __init__(self, username, password, ip, timestamp):
#         self.username = username
#         self.password = password
#         self.ip = ip
#         self.timestamp = timestamp

#     def serialize(self) -> dict:
#         return self.SERIALIZER(self).serialize()

# # ======
# import datetime


# def hide_field(field) -> str:
#     return "**redacted**"


# def format_time(field_timestamp: datetime) -> str:
#     return field_timestamp.strftime("%Y-%m-%d %H:%M")


# def show_original(event_field):
#     return event_field


# class EventSerializer:
#     def __init__(self, serialization_fields: dict) -> None:
#         self.serialization_fields = serialization_fields

#     def serialize(self, event) -> dict:
#         return {
# field: transformation(getattr(event, field))
# for field, transformation in self.serialization_fields.items()
#         }


# class Serialization:
#     def __init__(self, **transformations):
#         self.serializer = EventSerializer(transformations)

#     def __call__(self, event_class):
#         def serialize_method(event_instance):
#             return self.serializer.serialize(event_instance)
#         event_class.serialize = serialize_method
#         return event_class


# @Serialization(
#     username=show_original,
#     password=hide_field,
#     ip=show_original,
#     timestamp=format_time
# )
# =======
# @retry(arg1, arg2...)

# import logger
# RETRIES_LIMIT = 3


# def with_retry(retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
#     allowed_exceptions = allowed_exceptions or (ControlledException, )

#     def retry(operation):
#         @wraps(operation)
#         def wrapped(*args, **kwargs):
#             last_raised = None
#             for _ in range(retries_limit):
#                 try:
#                     return operation(*args, **kwargs)
#                 except allowed_exceptions as e:
#                     logger.info("retrying %s", operation.__qualname__)
#                     last_raised = e
#             raise last_raised
#         return wrapped
#     return retry

# # decorator_parameterized_1.py


# @with_retry()
# def run_operation(task):
#     return task.run()


# @with_retry(retries_limit=5)
# def run_with_custom_retries_limit(task):
#     return task.run()


# @with_retry(allowed_exceptions=(AttributeError, ))
# def run_with_custom_exceptions(task):
#     return task.run()


# @with_retry(retries_limit=4, allowed_exceptions=(ZeroDivisionError, AttributeError))
# def run_with_custom_parameters(task):
#     return task.run()

# # with_retry rewrite in class


# class WithRetry:

#     def __init__(self, retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
#         self.retries_limit = retries_limit
#         self.allowed_exceptions = allowed_exceptions or (ControlledException, )

#     def __call__(self, operation):
#         @wrap(operation)
#         def wrapped(*args, **kwargs):
#             last_raised = None
#             for _ in range(retries_limit):
#                 try:
#                     return operation(*args, **kwargs)
#                 except allowed_exceptions as e:
#                     logger.info("retrying %s", operation.__qualname__)
#                     last_raised = e
#             raise last_raised
#         return wrapped

# =======
# reuse decorator

# import logging
# from functools import wraps

# logger = logging.getLogger(__name__)


# class DBDriver:
#     def __init__(self, dbstring):
#         self.dbstring = dbstring

#     def execute(self, query):
#         return f"query {query} at {self.dbstring}"


# def inject_db_driver(function):
#     @wraps(function)
#     def wrapped(dbstring):
#         return function(DBDriver(dbstring))
#     return wrapped


# @inject_db_driver
# def run_query(driver):
#     return driver.execute("test_function")

# # run_query = inject_db_driver(run_query)


# def main():
#     print(run_query("test_OK"))
#     print(help(run_query))

# ==================
# descriptor
# ==================

# import logging

# class DescriptorClass:
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         logging.warning("Call: %s.__get__(%r, %r)",
#                         self.__class__.__name__, instance, owner)
#         return instance


# class ClientClass:
#     descriptor = DescriptorClass()


# def main():
#     client = ClientClass()
#     client.descriptor

# ========

# # __set__(self, instance, value)
# class Validation:
#     def __init__(self, validation_function, error_msg: str):
#         self.validation_function = validation_function
#         self.error_msg = error_msg

#     def __call__(self, value):
#         if not self.validation_function(value):
#             raise ValueError(f"{value!r} {self.error_msg}")


# class Field:
#     def __init__(self, *validations):
#         self._name = None
#         self.validations = validations

#     def __set_name__(self, owner, name):
#         self._name = name

#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__[self._name]

#     def validation(self, value):
#         for validation in self.validations:
#             validation(value)

#     def __set__(self, instance, value):
#         self.validation(value)
#         instance.__dict__[self._name] = value


# class ClientClass:
#     descriptor = Field(
#         Validation(lambda x: isinstance(x, (int, float)), "is not a number"),
#         Validation(lambda x: x >= 0, "is not >= 0")
#     )


# jkdef main():
#     client = ClientClass()
#     client.descriptor = -42
#     print(client.descriptor)

# __delete__(self, instance)

# class ProtectedAttribute:
#     def __init__(self, requires_role=None) -> None:
#         self.permisson_required = requires_role
#         self._name = None

#     def __set_name__(self, owner, name):
#         self._name = name

#     def __set__(self, user, value):
#         if value is None:
#             raise ValueError(f"{self._name} can't be set to None")
#         user.__dict__[self._name] = value

#     def __delete__(self, user):
#         if self.permisson_required in user.permissons:
#             user.__dict__[self._name] = None
#         else:
#             raise ValueError(
#                 f"User {user!s} doesn't have {self.permisson_required}"
#                 "permisson"
#             )


# class User:
#     email = ProtectedAttribute(requires_role="admin")

#     def __init__(self, username: str, email: str, permisson_list: list = None) -> None:
#         self.username = username
#         self.email = email
#         self.permissons = permisson_list or []

#     def __str__(self):
#         return self.username


# def main():
#     admin = User("root", "root@d.com", ["admin"])
#     print(admin.email)

#     del admin.email
#     print(admin.email)

#     user = User("user", "user1@d.com", ["email", "helpdesk"])
#     print(user.email)
#     del user.email

# ======
# __set_name__
# =====
# import logging


# class DescriptorWithName:
#     def __init__(self, name):
#         self.name = name

#     def __get__(self, instance, value):
#         if instance is None:
#             return self
#         logging.warning("getting %r attribute from $r", self.name, instance)
#         return instance.__dict__[self.name]

#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value


# class ClientClass:
#     descriptor = DescriptorWithName("descriptor")


# def main():
#     client = ClientClass()
#     client.descriptor = "value"
#     print(client.descriptor)

# =========
# # descriptor example
# # Original - no descriptor
# class Traveller:
#     def __init__(self, name, current_city):
#         self.name = name
#         self._current_city = current_city
#         self._cities_visited = [current_city]

#     @property
#     def current_city(self):
#         return self._current_city

#     @current_city.setter
#     def current_city(self, new_city):
#         if new_city != self._current_city:
#             self._cities_visited.append(new_city)
#         self._current_city = new_city

#     @property
#     def cities_visited(self):
#         return self._cities_visited

# # With descriptor

# class HistoryTracedAttribute:
#     def __init__(self, trace_attribute_name) -> None:
#         self.trace_attribute_name = trace_attribute_name  # [1]
#         self._name = None

#     def __set_name__(self, owner, name):
#         self._name = name

#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__[self._name]
#         # return instance.__dict__[self.trace_attribute_name]

#     def __set__(self, instance, value):
#         self._track_change_in_value_for_instance(instance, value)
#         instance.__dict__[self._name] = value

#     def _track_change_in_value_for_instance(self, instance, value):
#         self._set_default(instance)  # [2]
#         if self._needs_to_track_change(instance, value):
#             instance.__dict__[self.trace_attribute_name].append(value)

#     def _needs_to_track_change(self, instance, value) -> bool:
#         try:
#             current_value = instance.__dict__[self._name]
#         except KeyError:  # [3]
#             return True
#         return value != current_value  # [4]

#     def _set_default(self, instance):
#         instance.__dict__.setdefault(self.trace_attribute_name, [])  # [6]


# class Traveller:
#     current_city = HistoryTracedAttribute("cities_visited")  # [1]

#     def __init__(self, name, current_city):  # [1]
#         self.name = name
#         self.current_city = current_city  # [5]


# def main():
#     alice = Traveller("Alice", "Barcelona")
#     alice.current_city = "Paris"
#     alice.current_city = "Brussels"
#     alice.current_city = "Amsterdam"

#     print(alice.current_city)

# ========
# Analysis descriptor
# ========
# class MyClass:
#     def method(self, ...):
#         self.x = 1

# # equal to


# class MyClass:
#     def method(myclass_instance, ...):
#         myclass_instance.x = 1

# class Method:
#     def __init__(self, name):
#         self.name = name

#     def __call__(self, instance, arg1, arg2):
#         print(f"{self.name}: {instance} called with {arg1} and {arg2}")


# class MyClass:
#     method = Method("Internal Call")


# def main():
#     instance = MyClass()

#     print(Method("External call")(instance, "first", "second"))
#     print(instance.method("first", "second"))  # will fail

# # Fixed
# from types import MethodType


# class Method:
#     def __init__(self, name):
#         self.name = name

#     def __call__(self, instance, arg1, arg2):
#         print(f"{self.name}: {instance} called with {arg1} and {arg2}")

#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return MethodType(self, instance)


# class MyClass:
#     method = Method("Internal Call")


# def main():
#     instance = MyClass()

#     print(Method("External call")(instance, "first", "second"))
#     print(instance.method("first", "second"))

# ==================
# # generator - yield (lazy computation)
# ==================

# classic iteration
# class NumberSequence:
#     def __init__(self, start=0):
#         self.current = start

#     def next(self):
#         current = self.current
#         self.current += 1
#         return current


# def main():
#     seq = NumberSequence()
#     seq.next()  # 0
#     seq.next()  # 1
#     # fail NumberSequence() not suport iteration
#     list(zip(NumberSequence(), "abcdef"))

# fixed iteration

# class SequenceOfNumbers:
#     def __init__(self, start=0):
#         self.current = start

#     def __next__(self):
#         current = self.current
#         self.current += 1
#         return current

#     def __iter__(self):
#         return self


# class PurchasesStats:
#     def __init__(self, purchases):
#         self.purchases = iter(purchases)
#         self.min_price: float = None
#         self.max_price: float = None
#         self._total_purchases_price: float = 0.0
#         self._total_purchases = 0
#         self._initialize()

#     def _initialize(self):
#         try:
#             first_value = next(self.purchases)
#         except StopIteration:
#             raise ValueError("no values provided")

#         self.min_price = self.max_price = first_value
#         self._update_avg(first_value)

#     def process(self):
#         for purchase_value in self.purchases:
#             self._update_min(purchase_value)
#             self._update_max(purchase_value)
#             self._update_avg(purchase_value)
#         return self

#     def _update_min(self, new_value: float):
#         if new_value < self.min_price:
#             self.min_price = new_value

#     def _update_maz(self, new_value: float):
#         if new_value > self.min_price:
#             self.max_price = new_value

#     @property
#     def avg_price(self):
#         return self._total_purchases_price / self._total_purchases

#     def _update_avg(self, new_value: float):
#         self._total_purchases_price += new_value
#         self._total_purchases += 1

#     def __str__(self):
#         return (
#             f"{self.__class__.__name__}({self.min_price})"
#             f"{self.max_price}({self.avg_price})"
#         )

# def load_purchases(filename):
#     with open(filename) as f:
#         for line in f:
#             *_, price_raw = line.partition(',')
#             yield float(price_raw)


if __name__ == "__main__":
    main()
