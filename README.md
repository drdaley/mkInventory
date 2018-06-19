# mkInventory
mkInventory employs hotkeys, along with a CAS database search function to streamline inventory data entry.

Runs in python 3, requires the cirpy python library

mkInventory.py is the main script
mkInvDefs.py is for specifying list options that appear in the script.

Script begins by either creating or opening (in append mode) “output.csv”
Script will attempt to find a chemical name based on user-input of the CAS number (The CAS numbers available are based on commonchemistry.org) Hitting enter without entering a CAS number will take the user directly to manual name entry.
If a name is found, user selects the name to use from a list.
If no name is found, user is given the option to manually enter a name
User selects phase from a list
User enters the amount (without units)
User selects the units from a list
User enters the location the chemical is stored (if locations have been entered during this session, the user can select one of these from a list.)
