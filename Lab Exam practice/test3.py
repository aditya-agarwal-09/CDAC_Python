def get_string(prompt : str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Error: Enter valid string")

def valid_price() -> float:
    try:
        while True:
            val = float(input("Enter price: "))
            if val > 0.0:
                return val
            print("Error:enter valid price.")
    except ValueError:
        print("Error: enter valid price.")

def valid_count() -> int:
    try:
        while True:
            val = int(input("Enter count: "))
            if val > 0:
                return val
            print("Erro:enter valid count.")
    except ValueError:
        print("Error: enter valid count.")


def add_book_entry(catalog: list[dict], next_id : int) -> int:
    try:
        print("\n---Enroll new entry---")
        title = get_string("Enter book title: ")
        name = get_string("Enter author name: ")
        genre = get_string("enter genre name: ")
        price = valid_price()
        count = valid_count()

        new_book = {
            "id" : next_id,
            "title" : title,
            "name" : name,
            "genre" : genre,
            "price" : price,
            "count" : count
        }
        catalog.append(new_book)
        print("Successful:New book added.")
    except Exception as e:
        print("Error adding new entry.")

def render_catalog(catalog:list[dict]) -> None:

    ...
    try:
        print("\n ----RENDER CATALOG----")
        if not catalog:
            print("Catalog is empty.")
        print(f"{'id':<10}{'title':<12}{'name':<15}{'genre':<12}{'price':<10}{'count':<8}")
        for c in catalog:
            print(f"{c['id']:<10}{c['title']:<12}{c['name']:<15}{c['genre']:<12}{c['price']:<10}{c['count']:<8}")
    except Exception as e:
        print("Error rendering catalog: {e}")

def query_books(catalog:list[dict]) -> None:

    try:
        print("\n----QUERY BOOKS----")
        query = get_string("Enter id or name or title to search: ").lower()
        matches = []
        if not query:
            print("Error:Please enter query.")
        for c in catalog:
            if query.isdigit() and c['id'] == int(query):
                matches.append(query)
            elif query in c['name'].lower() or query in c['title'].lower():
                matches.append(query)
        render_catalog(matches)
    except Exception as e:
        print("Error searching query: {e}")

def modify_book_details(catalog : list[dict]) -> None:
    ...
    print("")
    cid = int(input("Enter id for modifying : "))
    target = None
    


def main():
    ...
    catalog = [

        {"id": 1,"title": "Python Programming","name":"John Zelle","genre":"Technical","price":569,"count":5},
        {"id": 2,"title": "Clean Code","name":"Robert Martin","genre":"Technical","price":469,"count":10},
        {"id": 3,"title": "The Great Gatsby","name":"F. Scott Fitzgerald","genre":"Fiction","price":888,"count":18},
    ]
    next_id = 4

    while True:
        print('-'* 60)
        print("Book catalog")
        print('='* 60)
        print("[1]Add Book    [2]Render Catalog")

        choice = input("enter choice (1-8): ")

        if choice == '1':
            add_book_entry(catalog,next_id)
        elif choice == '2':
            render_catalog(catalog)
        elif choice == '3':
            query_books(catalog)

main()