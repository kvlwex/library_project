from flask import Flask, request, jsonify
from server.database import init_db, db_session
from server.models import Book, User, Borrow
from datetime import datetime

app = Flask(__name__)
init_db()

@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    book = Book(
        title=data["title"],
        author=data["author"],
        isbn=data["isbn"],
        status="available",
        available_copies=data["available_copies"]
    )
    db_session.add(book)
    db_session.commit()
    return jsonify(book.to_dict()), 201

@app.route("/borrow", methods=["POST"])
def borrow_book():
    data = request.json
    book = Book.query.get(data["book_id"])
    if book.available_copies < 1:
        return jsonify({"error": "Book not available"}), 400
    borrow = Borrow(
        user_id=data["user_id"],
        book_id=data["book_id"],
        borrow_date=datetime.now(),
        return_date=None
    )
    book.available_copies -= 1
    db_session.add(borrow)
    db_session.commit()
    return jsonify(borrow.to_dict()), 200

@app.route("/return", methods=["POST"])
def return_book():
    data = request.json
    borrow = Borrow.query.filter_by(user_id=data["user_id"], book_id=data["book_id"], return_date=None).first()
    if not borrow:
        return jsonify({"error": "No active borrow found"}), 404
    borrow.return_date = datetime.now()
    book = Book.query.get(data["book_id"])
    book.available_copies += 1
    db_session.commit()
    return jsonify(borrow.to_dict()), 200

if __name__ == '__main__':
    app.run(debug=True)