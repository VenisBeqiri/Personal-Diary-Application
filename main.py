import os
from datetime import datetime

class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self, title, content):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {'date': date, 'title': title, 'content': content}
        self.entries.append(entry)
        print("Entry added!")

    def view_entries(self):
        if not self.entries:
            print("No entries found.")
            return
        for i, entry in enumerate(self.entries, start=1):
            print(f"{i}. {entry['date']} - {entry['title']}")
            print(f"   {entry['content']}\n")

    def generate_html(self):
        html_content = "<html><head><title>Diary Entries</title></head><body>"
        html_content += "<h1>My Diary</h1>"
        
        if not self.entries:
            html_content += "<p>No entries found.</p>"
        else:
            for entry in self.entries:
                html_content += f"<h2>{entry['title']}</h2>"
                html_content += f"<p><em>{entry['date']}</em></p>"
                html_content += f"<p>{entry['content']}</p><hr>"
        
        html_content += "</body></html>"

        with open("diary_entries.html", "w") as file:
            file.write(html_content)
        
        print("HTML summary generated: diary_entries.html")


def main():
    diary = Diary()
    
    while True:
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Generate HTML Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter the title of the entry: ")
            content = input("Enter the content of the entry: ")
            diary.add_entry(title, content)
        elif choice == '2':
            diary.view_entries()
        elif choice == '3':
            diary.generate_html()
        elif choice == '4':
            print("Exiting diary application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
