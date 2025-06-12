from incident_handler import log_incident, resolve_incident, list_open_incidents

def simulate_workflow():
    while True:
        print("\n1. Log Incident\n2. Resolve Incident\n3. View Open Incidents\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = int(input("Enter Student ID: "))
            issue = input("Describe the issue: ")
            log_incident(student_id, issue)
            print("Incident logged.")

        elif choice == "2":
            incident_id = int(input("Enter Incident ID to resolve: "))
            resolution = input("Enter resolution details: ")
            resolve_incident(incident_id, resolution)
            print("Incident resolved.")

        elif choice == "3":
            list_open_incidents()

        elif choice == "4":
            break

        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    simulate_workflow()