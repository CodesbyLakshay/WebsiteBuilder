from app.models.website import Website
from bson import ObjectId

class WebsiteService:
    def get_websites(self):
        websites = list(Website.find_all())
        for website in websites:
            website['_id'] = str(website['_id'])
        return {'websites': websites}, 200

    def get_website(self, id):
        website = Website.find_by_id(id)
        if website:
            website['_id'] = str(website['_id'])
            return {'website': website}, 200
        return {'message': 'Website not found'}, 404

    def create_website(self, data):
        website_id = Website.insert(data)
        return {'message': 'Website created successfully', 'id': str(website_id)}, 201

    def update_website(self, id, data):
        Website.update(id, data)
        return {'message': 'Website updated successfully'}, 200

    def delete_website(self, id):
        Website.delete(id)
        return {'message': 'Website deleted successfully'}, 200
