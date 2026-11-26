import csv
import os

FILENAME = "tickets.csv"
HEADERS = ["ID", "User", "Issue", "Priority", "Status"]

def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)

def add_ticket():
    user = input("Enter user's name: ")
    issue = input("Describe the IT issue: ")
    
    
    priority = input("Enter priority (Low, Medium, High) [Default: Medium]: ").strip().capitalize()
    if priority not in ["Low", "Medium", "High"]:
        print("Invalid or empty priority. Setting to Medium.")
        priority = "Medium"
    
    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
        ticket_id = len(rows)

    with open(FILENAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([ticket_id, user, issue, priority, "Open"])
    
    print(f"Ticket #{ticket_id} ({priority} priority) added successfully!\n")

def list_tickets(only_open=False):
    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        if len(rows) <= 1:
            print("No tickets found.\n")
            return

        header = rows[0]
        data_rows = rows[1:]

       
        if only_open:
            data_rows = [row for row in data_rows if row[4] == "Open"]
            title = "--- OPEN TICKETS ---"
        else:
            title = "--- ALL TICKETS ---"

        if not data_rows:
            print("No matching tickets found.\n")
            return

        print(f"\n{title}")
        print(f"{header[0]:<5} | {header[1]:<15} | {header[2]:<25} | {header[3]:<10} | {header[4]}")
        print("-" * 75)
        for row in data_rows:
            print(f"{row[0]:<5} | {row[1]:<15} | {row[2]:<25} | {row[3]:<10} | {row[4]}")
        print("-" * 75 + "\n")

def close_ticket():
    target_id = input("Enter the Ticket ID to close: ")
    updated_rows = []
    found = False

    with open(FILENAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == target_id and row[0] != "ID":
                row[4] = "Closed" 
                found = True
            updated_rows.append(row)

    if found:
        with open(FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print(f"Ticket #{target_id} is now Closed.\n")
    else:
        print(f"Ticket #{target_id} not found.\n")

def main():
    initialize_csv()
    while True:
        print("1. Add Ticket")
        print("2. List All Tickets")
        print("3. List Open Tickets Only")
        print("4. Close Ticket")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_ticket()
        elif choice == "2":
            list_tickets(only_open=False)
        elif choice == "3":
            list_tickets(only_open=True)
        elif choice == "4":
            close_ticket()
        elif choice == "5":
            print("Exiting tracker.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
