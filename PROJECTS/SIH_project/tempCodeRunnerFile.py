if flights:
        selected_index = int(input("Enter the number of the flight you want to select: ")) - 1
        selected_flight = flights[selected_index]
        generate_invoice(selected_flight)
    else:
        print("No flights found.")