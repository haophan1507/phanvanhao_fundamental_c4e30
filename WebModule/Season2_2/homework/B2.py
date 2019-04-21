import pymongo

client = pymongo.MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')

db = client.c4e

new_post = {
    'title' : 'Tôi Yêu Em',
    'author' : 'Puskin',
    'content' :'''Tôi yêu em: đến nay chừng có thể 
                Ngọn lửa tình chưa hẳn đã tàn phai 
                Nhưng không để em bận lòng thêm nữa 
                Hay hồn em phải gợn bóng u hoài

                Tôi yêu em âm thầm, không hy vọng 
                Lúc rụt rè, khi hậm hực lòng ghen 
                Tôi yêu em, yêu chân thành, đằm thắm 
                Cầu em được người tình như tôi đã yêu em'''
}
db.posts.insert_one(new_post)