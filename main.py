from queue import Queue

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
        customer_name = input("Enter customer name: ")
        queue.enqueue(customer_name)
        print("Customer added successfully.")

    elif choice == "2":
        served_customer = queue.dequeue()

        if served_customer is not None:
            print(f"Served: {served_customer}")

    elif choice == "3":
        next_customer = queue.peek()

        if next_customer is not None:
            print(f"Next customer: {next_customer}")

    elif choice == "4":
        print(f"Queue: {queue.items}")

    elif choice == "5":
        print(f"Queue size: {queue.size()}")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
