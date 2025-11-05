# =========================================
# Node 클래스
#  - 단순 연결 리스트 구성 요소
# =========================================
class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    # 현재 노드 뒤에 새 노드 삽입
    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    # 현재 노드 다음 노드 삭제 후 반환
    def popNext(self):
        deleted = self.link
        if deleted is not None:
            self.link = deleted.link
        return deleted


# =========================================
# Book 클래스
#  - 책 정보 저장
# =========================================
class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    # 출력용
    def print_info(self):
        print(f"[{self.book_id}] {self.title} / {self.author} / {self.year}")


# ======================================
# LinkedList 클래스
#  - Book 객체 저장
# =======================================
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    # 맨 앞 삽입 
    def insert_front(self, node):
        node.link = self.head
        self.head = node

    # 책 제목 Book 객체 반환
    def find_by_title(self, title):
        cur = self.head
        while cur is not None:
            if cur.data.title == title:
                return cur.data
            cur = cur.link
        return None

    # 책 제목 위치 반환
    def find_pos_by_title(self, title):
        cur = self.head
        pos = 0
        while cur is not None:
            if cur.data.title == title:
                return pos
            cur = cur.link
            pos += 1
        return -1

    # 책 번호 중복 확인
    def exists_book_id(self, book_id):
        cur = self.head
        while cur is not None:
            if cur.data.book_id == book_id:
                return True
            cur = cur.link
        return False

    # 해당 위치 노드 삭제
    def pop_pos(self, pos):
        if self.isEmpty():
            return None

        if pos == 0:
            deleted = self.head
            self.head = self.head.link
            return deleted.data

        cur = self.head
        # pos-1 위치까지 이동
        for _ in range(pos - 1):
            if cur is None:
                return None
            cur = cur.link

        deleted = cur.popNext()
        if deleted is None:
            return None

        return deleted.data

    # 전체 출력
    def print_all(self):
        if self.isEmpty():
            print("현재 등록된 도서 없음.")
            return

        cur = self.head
        while cur is not None:
            cur.data.print_info()
            cur = cur.link


# =======================================
# BookManagement
# ======================================
class BookManagement:
    def __init__(self):
        self.list = LinkedList()

    # 도서 추가
    def add_book(self, book_id, title, author, year):
        if self.list.exists_book_id(book_id):
            print("이미 존재하는 책 번호입니다.")
            return

        new_book = Book(book_id, title, author, year)
        new_node = Node(new_book)
        self.list.insert_front(new_node)

        print("도서가 추가되었습니다.")

    # 도서 삭제 (제목)
    def remove_book(self, title):
        pos = self.list.find_pos_by_title(title)
        if pos == -1:
            print("해당 제목의 도서를 찾을 수 없습니다.")
            return

        self.list.pop_pos(pos)
        print("도서가 삭제되었습니다.")

    # 도서 조회 (제목)
    def search_book(self, title):
        book = self.list.find_by_title(title)
        if book is None:
            print("오류: 해당 제목의 도서를 찾을 수 없습니다.")
        else:
            print("검색 결과:")
            book.print_info()

    # 전체 출력
    def display_books(self):
        print("\n전체 도서 목록:")
        self.list.print_all()

    # 프로그램 실행
    def run(self):
        while True:
            print("\n===== 메뉴 =====")
            print("1. 도서 추가")
            print("2. 도서 삭제 (제목)")
            print("3. 도서 조회 (제목)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")

            select = input("번호 선택: ")

            if select == "1":
                try:
                    book_id = int(input("책 번호: "))
                except:
                    print("숫자를 입력해야 합니다.")
                    continue
                title = input("책 제목: ")
                author = input("저자: ")
                year = input("출판 연도: ")
                self.add_book(book_id, title, author, year)

            elif select == "2":
                title = input("삭제할 책 제목: ")
                self.remove_book(title)

            elif select == "3":
                title = input("조회할 책 제목: ")
                self.search_book(title)

            elif select == "4":
                self.display_books()

            elif select == "5":
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다.")


# =======================================
# 실행
# =========================================
if __name__ == "__main__":
    manager = BookManagement()
    manager.run()