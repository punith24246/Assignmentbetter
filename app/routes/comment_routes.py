from flask import Blueprint, request, jsonify
from app.services.comment_service import create_comment, edit_comment, delete_comment, get_comments

comment_bp = Blueprint('comments', __name__, url_prefix='/api/comments')

@comment_bp.route('', methods=['POST'])
def add_comment():
    data = request.json
    task_id = data.get('task_id')
    content = data.get('content')
    if not task_id or not content:
        return jsonify({'error': 'Missing data'}), 400

    comment = create_comment(task_id, content)
    return jsonify({'id': comment.id, 'task_id': comment.task_id, 'content': comment.content}), 201


@comment_bp.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.json
    content = data.get('content')
    if not content:
        return jsonify({'error': 'Missing content'}), 400

    comment = edit_comment(comment_id, content)
    if comment:
        return jsonify({'id': comment.id, 'task_id': comment.task_id, 'content': comment.content})
    return jsonify({'error': 'Comment not found'}), 404


@comment_bp.route('/<int:comment_id>', methods=['DELETE'])
def remove_comment(comment_id):
    success = delete_comment(comment_id)
    if success:
        return jsonify({'message': 'Deleted successfully'}), 200
    return jsonify({'error': 'Comment not found'}), 404


@comment_bp.route('/task/<int:task_id>', methods=['GET'])
def list_comments(task_id):
    comments = get_comments(task_id)
    return jsonify([{'id': c.id, 'task_id': c.task_id, 'content': c.content, 'timestamp': c.timestamp.isoformat()} for c in comments])
