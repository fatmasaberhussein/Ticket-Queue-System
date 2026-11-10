from ticket_queue import Queue

# Create a Queue
queue = Queue()


# Ticket Queue System
while True:

    print("\n===== Ticket Queue System =====")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. View Next Customer")
    print("4. Show Queue")
    print("5. Show Queue Size")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        customer_name = " ".join(input("Enter customer name: ").split())
        if not customer_name:
            print("Customer name cannot be empty.")
 
        elif not all(part.isalpha() for part in customer_name.split()):
             print("Name must contain letters only.")

        else:
            queue.enqueue(customer_name)
            print("Customer added successfully.")

    elif choice == "2":
        served_customer = queue.dequeue()

        if served_customer is not None:
            print(f"Ticket #{served_customer['ticket_number']}")
            print(f"Served: {served_customer['customer_name']}")
            
    elif choice == "3":
        next_customer = queue.peek()

        if next_customer is not None:
            print(f"Ticket #{next_customer['ticket_number']}")
            print(f"Customer: {next_customer['customer_name']}")

    elif choice == "4":
        print("\n===== Current Queue =====")

        if queue.is_empty():
            print("The queue is empty.")

        else:
            for ticket in queue.items:
                print(f"Ticket #{ticket['ticket_number']}")
                print(f"Customer: {ticket['customer_name']}")
                print("----------------------")

    elif choice == "5":
        print(f"Queue size: {queue.size()}")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
