from todo.core.filters import ObjectFieldFilterBackend


class UserFilterBackend(ObjectFieldFilterBackend):
    filter_field = 'user_id'
