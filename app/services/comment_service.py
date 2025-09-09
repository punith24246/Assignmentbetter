from app.models import db, Comment

def create_comment(task_id, content):
    new_comment = Comment(task_id=task_id, content=content)
    db.session.add(new_comment)
    db.session.commit()
    return new_comment

def edit_comment(comment_id, content):
    comment = Comment.query.get(comment_id)
    if comment:
        comment.content = content
        db.session.commit()
    return comment

def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return True
    return False

def get_comments(task_id):
    return Comment.query.filter_by(task_id=task_id).all()
