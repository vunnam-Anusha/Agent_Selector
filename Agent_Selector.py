#!/usr/bin/env python
# coding: utf-8

import pandas as pd

Agent_Selection_Mode = ["All available", "Least busy", "Random"]
def Agent(path_to_data):
    x = input("Select Agent selection mode between (all available, least busy, random)?")
    y = input("Select the role of issue (for multiple separate by comma )?")

    # Get Data from CSV File
    data = pd.read_csv(path_to_data)

    Role = data['Role'].unique().tolist()


    x = x.lower()            # to handle any case

    # Always return "Available agents"
    AvailableAgents = data[data['Availability'] == "Available"]

    # Filter by ROle

    if ',' in y:                                       #Multiple Roles
        multipleRoles = []
        for i in y.split(','):
            multipleRoles.append(i.strip().title())

        AvailableAgents = AvailableAgents[AvailableAgents['Role'].isin(multipleRoles)]
    else:
        AvailableAgents = AvailableAgents[AvailableAgents['Role'] == y]

    # Mode logic performed here

    if x == "All Available".lower():
        return AvailableAgents
    elif x == "Least Busy".lower():
        AgentList = AvailableAgents[
            AvailableAgents['Available_since_in_hours'] == max(AvailableAgents['Available_since_in_hours'])]
    elif x == "Random".lower():
        AgentList = AvailableAgents.sample(4)
    else:
        return 'specified Mode - {} not found. please enter another Mode.'.format(x)

    return AgentList

#This is a funtion call
Agent("D:\\Support Genie\\Data.csv")


