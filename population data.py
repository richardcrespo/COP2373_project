"""
Program: Florida Population Growth Simulator
Author: Richard Crespo
Date: April 2026

Description:
This program creates a SQLite database named population_RC.
It stores population data for 10 Florida cities starting in 2025.
It then simulates 20 years of population growth/decline at random rates.
Finally, it allows the user to choose a city and displays a matplotlib
graph of its population change over time.
"""

import sqlite3
import random
import matplotlib.pyplot as plt


# FUNCTION 1: Create database, table, and insert 2025 data

def create_database():
    conn = sqlite3.connect("population_RC.db")
    cur = conn.cursor()

    # Create table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # 10 Florida cities with estimated 2025 populations
    cities_2025 = {
        "Miami": 460000,
        "Orlando": 320000,
        "Tampa": 420000,
        "Jacksonville": 980000,
        "St. Petersburg": 265000,
        "Tallahassee": 205000,
        "Fort Lauderdale": 185000,
        "Sarasota": 58000,
        "Gainesville": 145000,
        "Pensacola": 55000
    }

    # Insert 2025 data
    for city, pop in cities_2025.items():
        cur.execute("INSERT INTO population VALUES (?, ?, ?)", (city, 2025, pop))

    conn.commit()
    conn.close()
    print("Database created and 2025 data inserted.")



# FUNCTION 2: Simulate 20 years of population growth/decline

def simulate_population():
    conn = sqlite3.connect("population_RC.db")
    cur = conn.cursor()

    # Get list of cities
    cur.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cur.fetchall()]

    for city in cities:
        # Get 2025 population
        cur.execute("SELECT population FROM population WHERE city=? AND year=2025", (city,))
        pop = cur.fetchone()[0]

        # Simulate 20 years (2026–2045)
        for year in range(2026, 2046):
            # Random growth/decline rate between -2% and +4%
            rate = random.uniform(-0.02, 0.04)
            pop = int(pop * (1 + rate))

            cur.execute("INSERT INTO population VALUES (?, ?, ?)", (city, year, pop))

    conn.commit()
    conn.close()
    print("20-year population simulation completed.")



# FUNCTION 3: Plot population growth for a selected city

def plot_city_population():
    conn = sqlite3.connect("population_RC.db")
    cur = conn.cursor()

    # Get list of cities
    cur.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cur.fetchall()]

    print("\nChoose a city to display population growth:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    choice = int(input("\nEnter the number of the city: "))
    selected_city = cities[choice - 1]

    # Retrieve population data
    cur.execute("SELECT year, population FROM population WHERE city=? ORDER BY year", (selected_city,))
    data = cur.fetchall()

    years = [row[0] for row in data]
    pops = [row[1] for row in data]

    conn.close()

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(years, pops, marker='o', linestyle='-', color='blue')
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()



# MAIN PROGRAM EXECUTION

def main():
    create_database()
    simulate_population()
    plot_city_population()


# Run the program
if __name__ == "__main__":
    main()
