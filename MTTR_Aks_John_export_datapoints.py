import random
import matplotlib.pyplot as plt
from matplotlib.table import Table
import csv


def generate_random_mtbf_mttr():
    # Generate random MTBF and MTTR values in seconds
    mtbf = random.uniform(1000, 10000)  # Example: between 1000 and 10000 seconds
    mttr = random.uniform(10, 300)  # Example: between 10 and 300 seconds
    return mtbf, mttr


def simulate_parallel_flows(num_machines, num_simulations, runtime):
    # Initialize lists to store data for each flow
    flow1_downtimes = []
    flow2_downtimes = []

    for _ in range(num_simulations):
        # Generate random MTBF and MTTR values for each machine in each flow
        mtbf_mttr_flow1 = [
            generate_random_mtbf_mttr() for _ in range(num_machines // 2)
        ]
        mtbf_mttr_flow2 = [
            generate_random_mtbf_mttr() for _ in range(num_machines // 2)
        ]

        # Initialize variables to track total downtime for each flow
        total_downtime_flow1 = 0
        total_downtime_flow2 = 0

        for _ in range(runtime):
            # Check if a machine in Flow 1 should fail
            for mtbf, mttr in mtbf_mttr_flow1:
                if random.random() < (1 / mtbf):
                    total_downtime_flow1 += mttr

            # Check if a machine in Flow 2 should fail
            for mtbf, mttr in mtbf_mttr_flow2:
                if random.random() < (1 / mtbf):
                    total_downtime_flow2 += mttr

        # Store total downtime for each flow
        flow1_downtimes.append(total_downtime_flow1)
        flow2_downtimes.append(total_downtime_flow2)

    return flow1_downtimes, flow2_downtimes


def main():

    # Input parameters

    num_machines = 10
    num_simulations = 50
    runtime_per_day = 8 * 3600  # 8 hours per day, converted to seconds
    num_days = 5

    flow1_downtimes, flow2_downtimes = simulate_parallel_flows(
        num_machines, num_simulations, runtime_per_day * num_days
    )


     # Create a table showing downtime data for both flows

    table_data = []
    for i in range(num_simulations):
        table_data.append([i, flow1_downtimes[i], flow2_downtimes[i]])

    # Prints done to the terminal

    print('\nRaw python list:\n')
    print(table_data)

    print('\nPython formated list\n')
    for row in table_data:
        print(str(row[0]).ljust(20), str(row[1]).ljust(20), str(row[2]).ljust(20))


    # Print to CSV

    fields = ['Simulation', 'Flow 1', 'Flow2'] # names of columns in CSV
    rows = table_data

    with open('Downtime_Two_Flows.csv', 'w') as f:
     
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(fields) # writes column headers (as defined in the variable above)
        write.writerows(rows)  # writes rows (data)

    
    # Create and plot chart

    # Calculate the time axis for the chart
    time_axis = [i for i in range(num_simulations)]

    # Plot downtime for each flow
    # plt.plot(time_axis, flow1_downtimes, label="Flow 1 Downtime")
    # plt.plot(time_axis, flow2_downtimes, label="Flow 2 Downtime")

    plt.scatter(time_axis, flow1_downtimes, label="Flow 1 Downtime")
    plt.scatter(time_axis, flow2_downtimes, label="Flow 2 Downtime")

    plt.xlabel("Simulation")
    plt.ylabel("Downtime (seconds)")
    plt.legend()
    plt.title(
        f"Downtime in Two Parallel Flows Over {num_days} Days and {num_simulations} Simulations"
    )

    plt.show()

   


if __name__ == "__main__":
    main()
