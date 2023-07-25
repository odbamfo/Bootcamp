''' Minimum value index'''


def min_index(listLength):
    my_list = list()
    while len(my_list) < listLength:  # any range
        test = input()
        i = int(test)
        my_list.append(i)

    sorted_list = sorted(my_list)
    smallest_element = sorted_list[0]
    smallest_index = my_list.index(smallest_element)

    print("Smallest element is:", sorted_list[0])
    return smallest_index


listLength = int(input('How many characters will you be evaluating:'))
result = min_index(listLength)
print(result)

''' Maximum value index'''


def max_index(listLength):
    my_list = list()
    while len(my_list) < listLength:  # any range
        test = input()
        i = int(test)
        my_list.append(i)

    sorted_list = sorted(my_list)
    largest_element = sorted_list[listLength - 1]
    largest_index = my_list.index(largest_element)

    print("Largest element is:", sorted_list[listLength - 1])
    return largest_index


listLength = int(input('How many characters will you be evaluating:'))
result = max_index(listLength)
print(result)

'''çomparison code'''


def smaller_indices(listLength):
    print("Enter the values for the first list")
    my_list1 = list()
    while len(my_list1) < listLength:  # any range
        test = input()
        i = int(test)
        my_list1.append(i)

    print("Enter the values for the second list")
    my_list2 = list()
    while len(my_list2) < listLength:  # any range
        test = input()
        i = int(test)
        my_list2.append(i)

    index = 0
    my_list3 = list()
    while index < listLength:
        if my_list1[index] < my_list2[index]:
            my_list3.append(index)
        index += 1

    return my_list3


listLength = int(input('How many characters will be in both lists:'))
result = smaller_indices(listLength)
print(result)

''' Pairwise'''


def pairwise_product(listLength):
    print("Enter the values for the first list")
    my_list1 = list()
    while len(my_list1) < listLength:  # any range
        test = input()
        i = int(test)
        my_list1.append(i)

    print("Enter the values for the second list")
    my_list2 = list()
    while len(my_list2) < listLength:  # any range
        test = input()
        i = int(test)
        my_list2.append(i)

    product_list = list()
    for i in range(listLength):
        product = my_list1[i] * my_list2[i]
        product_list.append(product)

    return product_list


listLength = int(input('How many characters will be in both lists:'))
result = pairwise_product(listLength)
print(result)

'''Ratio'''


def pairwise_ratio(listLength):
    print("Enter the values for the first list")
    my_list1 = list()
    while len(my_list1) < listLength:  # any range
        test = input()
        i = int(test)
        my_list1.append(i)

    print("Enter the values for the second list")
    my_list2 = list()
    while len(my_list2) < listLength:  # any range
        test = input()
        i = int(test)
        my_list2.append(i)

    ratio_list = list()
    for i in range(listLength):
        ''''if my_list1[index] > my_list2[index]:'''
        ratio = my_list1[i] / my_list2[i]
        ratio_list.append(ratio)

    return ratio_list


listLength = int(input('How many characters will be in both lists:'))
result = pairwise_ratio(listLength)
print(result)




'''List 2'''

import pandas as pd

def read_data_from_file(file_name):
    country_data = pd.read_excel(file_name)
    country_names = country_data['Country Name'].tolist()
    populations = country_data['Population'].tolist()
    literacy_rates = country_data['Literacy'].tolist()
    mobile_subscriptions = country_data['Mobile'].tolist()
    internet_users = country_data['Internet'].tolist()
    electricity_production = country_data['Elect. Production'].tolist()
    electricity_consumption = country_data['Elect. Consumption'].tolist()
    country_index_mapping = {country: index for index, country in enumerate(country_names)}

    return country_names, populations, literacy_rates, mobile_subscriptions, internet_users, electricity_production, electricity_consumption, country_index_mapping

def query_country_info(country_names, populations, literacy_rates, mobile_subscriptions, internet_users, electricity_production, electricity_consumption, country_index_mapping):
    user_input = input("Hello! What country would you like information on? ")
    country_index = country_index_mapping.get(user_input)
    if country_index is not None:
        population = populations[country_index]
        literacy_rate = literacy_rates[country_index]
        mobile_subscription = mobile_subscriptions[country_index]
        internet_user = internet_users[country_index]

        print(f"{user_input} has a population of {population:,} and a literacy rate of {literacy_rate:.2f}%.")
        print(f"The estimate of the number of mobile subscriptions is {mobile_subscription:,}, while that of internet users is {internet_user:,}.")

        # Add additional information if needed based on the data file
    else:
        print("Country not found in the data.")

def get_country_info(country_names, populations, mobile_subscriptions, internet_users):
    # Initialize empty lists to store mobile subscriptions per capita and internet users per capita
    mobile_subscriptions_per_capita = []
    internet_users_per_capita = []

    # Calculate mobile subscriptions per capita and internet users per capita using a loop
    for i in range(len(country_names)):
        mobile_sub_per_capita = mobile_subscriptions[i] / populations[i]
        internet_users_per_cap = internet_users[i] / populations[i]

        # Append the calculated values to the respective lists
        mobile_subscriptions_per_capita.append(mobile_sub_per_capita)
        internet_users_per_capita.append(internet_users_per_cap)

    # Return the country name, mobile subscriptions per capita, and internet users per capita
    return country_names, mobile_subscriptions_per_capita, internet_users_per_capita

def create_output_file(file_name, country_names, mobile_subscriptions_per_capita, internet_users_per_capita):
    # Open a new file for writing
    with open(file_name, 'w') as file:
        # Write the header row
        file.write("Country Name\tMobile Subscriptions per Capita\tInternet Users per Capita\n")

        # Write the data rows using string formatting for alignment
        for country, mobile_sub, internet_user in zip(country_names, mobile_subscriptions_per_capita, internet_users_per_capita):
            file.write(f"{country}\t\t{mobile_sub:.2f}\t\t\t\t{internet_user:.2f}\n")


def compute_report(country_names, populations, literacy_rates, mobile_subscriptions, internet_users, electricity_production, electricity_consumption):
    total_population_africa = sum(populations)

    # Most populous and least populous African countries
    most_populous_country_index = populations.index(max(populations))
    most_populous_country = country_names[most_populous_country_index]
    least_populous_country_index = populations.index(min(populations))
    least_populous_country = country_names[least_populous_country_index]

    # Countries with the highest and lowest literacy rates
    highest_literacy_index = literacy_rates.index(max(literacy_rates))
    highest_literacy_country = country_names[highest_literacy_index]
    lowest_literacy_index = literacy_rates.index(min(literacy_rates))
    lowest_literacy_country = country_names[lowest_literacy_index]

    # Compute the "average" literacy rate in Africa
    total_literacy_weighted = 0
    for i in range(len(country_names)):
        total_literacy_weighted += literacy_rates[i] * populations[i]
    average_literacy_rate_africa = total_literacy_weighted / total_population_africa

    # Countries with the highest and lowest number of mobile subscriptions per capita
    mobile_subscriptions_per_capita = []
    for i in range(len(country_names)):
        mobile_sub_per_capita = mobile_subscriptions[i] / populations[i]
        mobile_subscriptions_per_capita.append(mobile_sub_per_capita)

    highest_mobile_subscription_index = mobile_subscriptions_per_capita.index(max(mobile_subscriptions_per_capita))
    highest_mobile_subscription_country = country_names[highest_mobile_subscription_index]
    lowest_mobile_subscription_index = mobile_subscriptions_per_capita.index(min(mobile_subscriptions_per_capita))
    lowest_mobile_subscription_country = country_names[lowest_mobile_subscription_index]

    # Countries with the highest and lowest numbers of internet users per capita
    internet_users_per_capita = []
    for i in range(len(country_names)):
        internet_users_per_cap = internet_users[i] / populations[i]
        internet_users_per_capita.append(internet_users_per_cap)

    highest_internet_users_index = internet_users_per_capita.index(max(internet_users_per_capita))
    highest_internet_users_country = country_names[highest_internet_users_index]
    lowest_internet_users_index = internet_users_per_capita.index(min(internet_users_per_capita))
    lowest_internet_users_country = country_names[lowest_internet_users_index]

    # Countries that produce more electricity than they consume (electricity exporters)
    electricity_exporters = []
    for i in range(len(country_names)):
        if electricity_production[i] > electricity_consumption[i]:
            electricity_exporters.append(country_names[i])

    # Print the computed information
    print(f"Total population of Africa: {total_population_africa:,}")
    print(f"Most populous country: {most_populous_country} (Population: {max(populations):,})")
    print(f"Least populous country: {least_populous_country} (Population: {min(populations):,})")
    print(f"Highest literacy rate: {highest_literacy_country} (Literacy Rate: {max(literacy_rates)}%)")
    print(f"Lowest literacy rate: {lowest_literacy_country} (Literacy Rate: {min(literacy_rates)}%)")
    print(f"Average literacy rate in Africa: {average_literacy_rate_africa:.2f}%")
    print(
        f"Highest mobile subscriptions per capita: {highest_mobile_subscription_country} (Subscriptions: {max(mobile_subscriptions_per_capita):.2f})")
    print(
        f"Lowest mobile subscriptions per capita: {lowest_mobile_subscription_country} (Subscriptions: {min(mobile_subscriptions_per_capita):.2f})")
    print(
        f"Highest internet users per capita: {highest_internet_users_country} (Internet Users: {max(internet_users_per_capita):.2f})")
    print(
        f"Lowest internet users per capita: {lowest_internet_users_country} (Internet Users: {min(internet_users_per_capita):.2f})")
    print("Countries that produce more electricity than they consume (Electricity Exporters):")
    for country in electricity_exporters:
        print(f"- {country}")


# Replace 'CountryData

# Replace 'CountryData.xlsx' with the actual file name
file_name = 'C:\\Users\\owure\\OneDrive\\Pictures\\Scans\\CountryData.xlsx'
country_names, populations, literacy_rates, mobile_subscriptions, internet_users, electricity_production, electricity_consumption, country_index_mapping = read_data_from_file(file_name)

# Call the query_country_info function
query_country_info(country_names, populations, literacy_rates, mobile_subscriptions, internet_users, electricity_production, electricity_consumption, country_index_mapping)

# Call the get_country_info function
country_names, mobile_subscriptions_per_capita, internet_users_per_capita = get_country_info(country_names, populations, mobile_subscriptions, internet_users)

# Create the output file
output_file_name = 'C:\\Users\\owure\\OneDrive\\Pictures\\Scans\\CountryDataOutput.txt'
create_output_file(output_file_name, country_names, mobile_subscriptions_per_capita, internet_users_per_capita)

# Compute and report additional information
compute_report(country_names, populations, literacy_rates, mobile_subscriptions, internet_users, electricity_production, electricity_consumption)
print(f"\nData written to file: {output_file_name}")
