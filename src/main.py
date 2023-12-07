# import pandas as pd
# import numpy as np
import json
import time
import random


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.states = {
            "sleep": False,
            "poisoned": False,
            "paralyzed": False,
            "hunger": False,
            # Add more states as needed
        }

    def toggle_state(self, state_names):
        # Toggle the specified state
        for state_name in state_names:
            if state_name in self.states:
                self.states[state_name] = not self.states[state_name]
                print(f"{state_name} state toggled to {self.states[state_name]}")
            else:
                print(f"State '{state_name}' does not exist.")


def read_events(event_tag):
    # Specify the path to your JSON file
    json_file_path = "events/events.json"

    # Open and read the JSON file
    with open(json_file_path, "r") as file:
        data = json.load(file)

    # Now 'data' contains the contents of your JSON file as a Python dictionary
    # You can access specific information using dictionary keys
    selected_events = [
        event for event in data["events"] if event["event_tag"] == event_tag
    ]

    events = data["events"]
    return selected_events
    # Example: Print the text of each event
    # for event in events:
    #    event_id = event["event_id"]
    #    event_text = event["text"]
    #    print(f"Event {event_id}: {event_text}")


def initialize_event(event_data):
    event_no = int(input("What's the event number? "))
    print(event_data[event_no]["text"])
    time.sleep(3)
    for i in range(len(event_data[event_no]["options"])):
        print(
            "\n",
            event_data[event_no]["options"][i]["option_id"],
            ".",
            event_data[event_no]["options"][i]["text"],
        )
        time.sleep(1)
    while True:
        try:
            choice = int(input("\nMake your choice (1 or 2): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if choice not in {1, 2}:
            print("Not a valid choice. Please enter 1 or 2.")
        elif choice == 1:
            print("Outcome:", event_data[event_no]["options"][0]["outcome"][0])
            break  # Exit the loop after printing the outcome
        elif choice == 2:
            if random.random() < 0.5:
                print("Outcome:", event_data[event_no]["options"][1]["outcome"][0])
            else:
                print("Outcome:", event_data[event_no]["options"][1]["outcome"][1])
            break  # Exit the loop after printing the outcome


if __name__ == "__main__":
    ply1 = Player("playerName")
    # ply1.toggle_state(["sleep", "hunger", "asda"])
    data = read_events("forest")
    initialize_event(data)
