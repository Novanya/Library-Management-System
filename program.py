import csv
from collections import Counter
from datetime import datetime

def create_book_file():
    with open("book.csv", "w", newline="") as f:
        fieldnames = ['book_id', 'title', 'isbn', 'copies', 'availability', 'price']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

def create_student_file():
    with open("student.csv", "w", newline="") as f:
        fieldnames = ['student_id', 'name', 'age', 'badge',
                      'program', 'department', 'email',
                      'phone', 'address',
                      'number_of_books_issued', 'issued_books']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


def create_transaction_file():
    with open("transactions.csv", "w", newline="") as f:
        fieldnames = ['date', 'book_id', 'student_id', 'type']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

def main_program():

    while True:
        print("Welcome to the Library Management System. Please select an option to continue.")
        print("""
              Library Management System      
        1. Add Book
        2. Update Book Details
        3. Search Book
        4. View All Books
        5. Add Student
        6. Issue Book
        7. Return Book
        8. View Issue Trend Report
        9. Exit
        10.View Transactions
        
        """)
        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        if choice == 1:
            add_book()
        elif choice == 2:
            update_book()
        elif choice == 3:
            search_book()
        elif choice == 4:
            view_all_books()
        elif choice == 5:
            add_student()
        elif choice == 6:
            issue_book()
        elif choice == 7:
            return_book()
        elif choice == 8:
            view_issue_trend_report()
        elif choice == 9:
            print("Existing the system")
            break
        elif choice == 10:
            view_transactions()
        else:
            print("Invalid choice.")

def add_book():
    book_id = 1
    isbn = (input("Enter ISBN number: "))
    book_name = input("Enter book name: ")
    book_copies = int(input("Enter number of book copies: "))
    book_price = float(input("Enter book price: "))
    availability = input("Enter availability: ")

    try:
        with open("book.csv", "r") as file:
            books = list(csv.DictReader(file))

    except FileNotFoundError:
            print("book.csv not found. Creating file...")
            create_book_file()
            books = []
    if books:
        last_id_num = max(int(book['book_id'][1:]) for book in books)
    else:
        last_id_num = 0
    new_id_num = last_id_num+1
    book_id = f"B{new_id_num:03}"
    new_book = {
        'book_id': book_id,
        'title': book_name,
        'isbn': isbn,
        'copies': book_copies,
        'availability': availability,
        'price': book_price
    }
    books.append(new_book)
    print(new_book)

    with open("book.csv", "w", newline="") as f:
        fieldnames = ['book_id', 'title', 'isbn', 'copies', 'availability', 'price']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)



def update_book():
    book_isbn = input("Enter ISBN number: ")
    try:
        with open("book.csv", "r") as file:
            books = list(csv.DictReader(file))
            if books:
                filtered_books = list(filter(lambda book: book['isbn'] == str(book_isbn), books))
                if filtered_books:
                    print("The book isbn is", filtered_books[0]['isbn'])
                    for key,value in filtered_books[0].items():
                        print(key,": ", value)
                    print("Which value to change?")
                    print("""
                    1:Title
                    2:isbn
                    3:copies
                    4:availability
                    5:price""")
                    try:
                        choice = int(input("Enter your choice: "))

                        if choice in [1,2,3,4,5]:
                            new_value = input("Which value to replace with old value?")
                            if choice == 1:
                                filtered_books[0]["title"]=new_value
                            elif choice == 2:
                                filtered_books[0]["isbn"]=new_value
                            elif choice == 3:
                                filtered_books[0]["copies"]=int(new_value)
                            elif choice == 4:
                                filtered_books[0]["availability"]=new_value
                            elif choice == 5:
                                filtered_books[0]["price"]=float(new_value)

                            print("Updated value:", filtered_books[0])

                            book_id_to_update = filtered_books[0]['book_id']
                            index = next(i for i, book in enumerate(books) if book['book_id'] == book_id_to_update)
                            books[index] = filtered_books[0]

                        elif choice not in [1,2,3,4,5]:
                            print("Invalid choice.")
                            return
                    except ValueError:
                        print("Please enter a valid number.")

                    with open('book.csv', 'w', newline="") as f:
                        fieldnames = ['book_id', 'title', 'isbn', 'copies', 'availability', 'price']
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(books)
                        print("The book isbn is", filtered_books[0]['isbn'])
                        print("""Values updated:""")
                        print(filtered_books[0])
                        filtered_books = []
                else:
                    print("No books found.")


    except FileNotFoundError:
        print("book.csv not found. Creating file...")
        create_book_file()
        books = []


def search_book():
    book_isbn = input("Enter ISBN number: ")
    try:
        with open("book.csv", "r") as file:
            books = list(csv.DictReader(file))
            if books:
                filtered_books = list(filter(lambda book: book['isbn'] == book_isbn, books))
                if filtered_books:
                    print("The book isbn is", filtered_books[0]['isbn'])
                    for key,value in filtered_books[0].items():
                        print(key, value)
                else:
                    print("There is no available book under the ISBN number",book_isbn)

    except FileNotFoundError:
        print("book.csv not found. Creating file...")
        create_book_file()
        books = []


def view_all_books():
    try:
        with open("book.csv", "r") as file:
            books = list(csv.DictReader(file))
            if books:
                for book in books:
                        for key,value in book.items():
                            print(key,": ", value)
                        print("==========================================")
            else:
                print("No books found.")

    except FileNotFoundError:
        print("book.csv not found. Creating file...")
        create_book_file()
        books = []


def add_student():
    students = []
    student_id = input("Enter student ID: ")

    try:
        with open("student.csv", "r") as file:
            students = list(csv.DictReader(file))
            if students:
                filtered = list(filter(lambda student: student['student_id'] == str(student_id), students))
                if filtered:
                    print(student_id, " is already registered")
                    return

    except FileNotFoundError:
        print("student.csv not found. Creating file...")
        create_student_file()

    name = input("Enter student name: ")
    age = input("Enter student age: ")
    badge = input("Enter student badge: ")
    program = input("Enter student program: ")
    department=input("Enter student department: ")
    email = input("Enter student email: ")
    phone = input("Enter student phone: ")
    address = input("Enter student address: ")
    number_of_books_issued = input("Enter number of books issued: ")
    issued_books = []
    while True:
        issued_book = input("Enter issued book name (type 'stop' to finish): ")
        if issued_book.lower() == "stop":
            break
        issued_books.append(issued_book)

    new_student = {
        'student_id': str(student_id),
        'name': name,
        'age': age,
        'badge': badge,
        'program': program,
        'department': department,
        'email': email,
        'phone': phone,
        'address': address,
        'number_of_books_issued': number_of_books_issued,
        "issued_books":",".join(issued_books)

    }

    with open("student.csv", "a", newline="") as file:
        fieldnames = ['student_id', 'name', 'age', 'badge', 'program', 'department', 'email', 'phone', 'address',
                      'number_of_books_issued','issued_books']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if students == []:
            writer.writeheader()
        writer.writerow(new_student)

    print(f"Student {name} with ID {student_id} added successfully.")


def issue_book():
    book_id = input("Enter book id: ")
    try:
        with open("book.csv", "r") as file:
            books = list(csv.DictReader(file))
            filtered_books = list(filter(lambda book: book['book_id'] == book_id, books))
            if not filtered_books:
                print("Book not found.")
                return
            for (key,value) in filtered_books[0].items():
                print(key, value)
            if int(filtered_books[0]["copies"]) < 1:
                print("Not Available")
                return
            student_id = input("Enter student ID: ")
            try:
                with open('student.csv', 'r', newline="") as file:
                    students = list(csv.DictReader(file))
            except FileNotFoundError:
                print("student.csv not found. Creating file...")
                create_student_file()
                return
            filter_students = list(filter(lambda student: student['student_id'] == str(student_id), students))
            if not filter_students:
                print("Invalid student ID.")
                return
            if int(filter_students[0]["number_of_books_issued"]) >= 3:
                print("Limit exceeded.")
                return
            book_index = next(i for i, s in enumerate(books) if s['book_id'] == book_id)
            student_id_to_update = filter_students[0]['student_id']
            index = next(i for i, s in enumerate(students) if s['student_id'] == student_id_to_update)
            issued_list = students[index]["issued_books"].split(",") if students[index]["issued_books"] else []
            if books[book_index]["title"] in issued_list:
                print("Student already issued this book.")
                return
            choice = input("Type yes to continue...")
            if choice.lower() == "yes":
                try:
                    with open("transactions.csv", "a", newline="") as file:
                        fieldnames = ['date', 'book_id', 'student_id', 'type']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        if file.tell() == 0:
                            writer.writeheader()
                        current_date = datetime.now().strftime("%d/%m/%Y")
                        writer.writerow({
                            'date': current_date,
                            'book_id': book_id,
                            'student_id': student_id,
                            'type': '1'
                        })
                except FileNotFoundError:
                    create_transaction_file()
                    with open("transactions.csv", "a", newline="") as file:
                        fieldnames = ['date', 'book_id', 'student_id', 'type']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        if file.tell() == 0:
                            writer.writeheader()
                        current_date = datetime.now().strftime("%d/%m/%Y")
                        writer.writerow({
                            'date': current_date,
                            'book_id': book_id,
                            'student_id': student_id,
                            'type': '1'
                        })
                students[index]["number_of_books_issued"] = str(int(students[index]["number_of_books_issued"]) + 1)
                books[book_index]["copies"] = str(int(books[book_index]["copies"]) - 1)
                if int(books[book_index]["copies"]) == 0:
                    books[book_index]["availability"] = "not available"
                issued_list.append(books[book_index]["title"])
                students[index]["issued_books"] = ",".join(issued_list)
                with open('student.csv', 'w', newline="") as file:
                    fieldnames = ['student_id', 'name', 'age', 'badge',
                                  'program', 'department', 'email',
                                  'phone', 'address',
                                  'number_of_books_issued','issued_books']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(students)

                with open('book.csv', 'w', newline="") as f:
                    fieldnames = ['book_id', 'title', 'isbn', 'copies', 'availability', 'price']
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(books)
    except FileNotFoundError:
        print("book.csv not found. Creating file...")
        create_book_file()
        books = []
        return


def return_book():
    book_id = input("Enter book id: ")
    try:
        with open("book.csv", "r") as file:
            books = list(csv.DictReader(file))
            filtered_books = list(filter(lambda book: book['book_id'] == book_id, books))
            if not filtered_books:
                print("Invalid book id.")
                return
            for (key, value) in filtered_books[0].items():
                print(key, value)
            student_id = input("Enter student ID: ")
            try:
                with open('student.csv', 'r', newline="") as file:
                    students = list(csv.DictReader(file))
            except FileNotFoundError:
                print("student.csv not found. Creating file...")
                create_student_file()
                return
            filter_students = list(filter(lambda student: student['student_id'] == str(student_id), students))
            if not filter_students:
                print("Invalid student ID.")
                return
            if int(filter_students[0]["number_of_books_issued"]) <1:
                print("No book issued")
                return
            issued_list = filter_students[0]["issued_books"].split(",") if filter_students[0][
                "issued_books"] else []
            if filtered_books[0]["title"] not in issued_list:
                print("Book not issued.")
                return

            choice = input("Type yes to continue...")
            if choice.lower() == "yes":
                try:
                    with open("transactions.csv", "a", newline="") as file:
                        fieldnames = ['date', 'book_id', 'student_id', 'type']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        if file.tell() == 0:
                            writer.writeheader()
                        current_date = datetime.now().strftime("%d/%m/%Y")
                        writer.writerow({
                            'date': current_date,
                            'book_id': book_id,
                            'student_id': student_id,
                            'type': '2'
                        })
                except FileNotFoundError:
                    create_transaction_file()
                    with open("transactions.csv", "a", newline="") as file:
                        fieldnames = ['date', 'book_id', 'student_id', 'type']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        current_date = datetime.now().strftime("%d/%m/%Y")
                        writer.writerow({
                            'date': current_date,
                            'book_id': book_id,
                            'student_id': student_id,
                            'type': '2'
                        })
                book_index = next(i for i, s in enumerate(books) if s['book_id'] == book_id)
                books[book_index]["copies"] = str(int(books[book_index]["copies"]) + 1)
                student_id_to_update = filter_students[0]['student_id']
                index = next(i for i, s in enumerate(students) if s['student_id'] == student_id_to_update)
                students[index]["number_of_books_issued"] = str(int(students[index]["number_of_books_issued"]) - 1)

                if books[book_index]["title"] in issued_list:
                    issued_list.remove(books[book_index]["title"])
                students[index]["issued_books"] = ",".join(issued_list)

                if int(books[book_index]["copies"]) > 0:
                    books[book_index]["availability"] = "available"
                with open('student.csv', 'w', newline="") as file:
                    fieldnames = ['student_id', 'name', 'age', 'badge',
                                  'program', 'department', 'email',
                                  'phone', 'address',
                                  'number_of_books_issued','issued_books']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(students)

                with open('book.csv', 'w', newline="") as f:
                    fieldnames = ['book_id', 'title', 'isbn', 'copies', 'availability', 'price']
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(books)
    except FileNotFoundError:
        print("book.csv not found. Creating file...")
        create_book_file()
        books = []
        return
def view_transactions():
    try:
        with open("transactions.csv", "r") as file:
            transactions = list(csv.DictReader(file))

        print("\n--- Transaction Records ---")

        for t in transactions:
            status = "Issued" if t["type"] == "1" else "Returned"
            print(f"Date: {t['date']} | Book ID: {t['book_id']} | Student ID: {t['student_id']} | Status: {status}")

        print("----------------------------\n")

    except FileNotFoundError:
        print("transactions.csv not found.")

def view_issue_trend_report():
    try:
        with open("student.csv", "r") as file:
            students = list(csv.DictReader(file))

        issued_books = []
        for student in students:
            if student["issued_books"]:
                issued_books += student["issued_books"].split(",")

        if not issued_books:
            print("No books have been issued yet.")
            return

        book_counts = Counter(issued_books)

        print("\n--- Book Issue Trend Report ---")
        for book, count in book_counts.most_common():
            print(f"{book}: {count} times issued")
        print("-------------------------------\n")

    except FileNotFoundError:
        print("student.csv not found. Creating file...")
        create_student_file()
        return


main_program()