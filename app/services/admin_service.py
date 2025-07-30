from app.models.user import User

class AdminService:
    def get_users(self):
        users = list(User.find_all())
        for user in users:
            user['_id'] = str(user['_id'])
        return {'users': users}, 200

    def update_user_role(self, user_id, data):
        User.update_role(user_id, data['role'])
        return {'message': 'User role updated successfully'}, 200

    def get_roles(self):
        # Example roles data
        roles = [
            {'id': 1, 'name': 'Admin'},
            {'id': 2, 'name': 'Editor'},
            {'id': 3, 'name': 'Viewer'}
        ]
        return {'roles': roles}, 200

    def create_role(self, data):
        # Logic to create a new role
        return {'message': 'Role created successfully'}, 201
